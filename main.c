#include <libpynq.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stepper.h>
#include <string.h>
#include <iic.h>
#include <tcs3472.h>
#include <vl53l0x.h>
#include <pthread.h>
#include <fcntl.h>
#include <unistd.h>

#define speed_m 30000
#define speed_r 60000
#define integration_time_ms 60
#define pred_distance 700 // distance in msec
#define valley_width 700  // distance in msec for width of valley

bool movement = false;			 // we could use pointers, but it would complicate main algorithm code
tcs3472 sensorC = TCS3472_EMPTY; // color sensor variable (needed in initialize and tape_detect)
vl53x sensorD;
static char *last_received_message = "placeholder"; // Global Var to store last message

// creating threads
pthread_t thread1;
pthread_t thread2;

// prototypes
void initialise();
void destroy();
void move_start();
void move_pred();
int move_stop();
void rotate(int angle);
void calibrate_border_path();
int tape_detect();
int distance_sens();
void scanTrip(bool report_data);
bool obstacleEncountered();
char *type_obstacle();
void avoidObstacle();
void send_message(const char *message);
void receive_messages();
void *threaded_receive_messages();
char *get_msg();

int main(void)
{
	initialise();
	// initialising the switchbox for the UART

	uart_init(UART0);		 // initialize UART 0
	uart_reset_fifos(UART0); // flush FIFOs of UART 0

	// once the start command has been received,
	// the robots initiate start searching for the border
	receive_messages(); // This will run indefinitely

	// // while the border has not been encountered yet,
	// // the robots will move forward and avoid any obstacles
	printf("start scanTrip\n");
	scanTrip(false);
	printf("stop scanTrip\n");
	// // once the robot encountered the border for the first time
	// // it now starts to find the first corner and then starts scanning the surface
	// // first the robot aligns perpendicularly with the border and then turns
	printf("start calibrating\n");
	sleep_msec(3000);
	calibrate_border_path();
	printf("stop calibrating\n");
	printf("start rotate\n");
	rotate(90);
	printf("stop rotate\n");
	printf("start scanTrip");
	scanTrip(false);
	printf("stop scanTrip\n");

	// // // after the robot is set on the right path it
	// // // moves alongside the border until it detects the first corner

	///////////////////// SCANNING AREA PHASE /////////////////////

	send_message("start_GUI");
	while (1)
	{
		// now that the robot arrived at one corner, it has to
		// start the scanning phase by first rotating in the correct direction
		rotate(90);
		scanTrip(true);

		// once the border is detected, the robot turns 90 degs
		// and checks first for an obstacle
		rotate(90);
		if (tape_detect())
			break;
		else if (obstacleEncountered())
		{
			type_obstacle();
			avoidObstacle();
			send_message("object"); // Hyunwoo
		}
		else if (!obstacleEncountered())
		{
			move_pred();
			move_stop();
		}
	}

	//////////////////////////////// FINAL SIDE SNAKE/SCAN ////////////////////////////////
	rotate(90);
	scanTrip(true);
	printf("exit_success\n");
	fflush(NULL);
	uart_reset_fifos(UART0);
	uart_destroy(UART0);

	// clean up after use
	send_message("stop_GUI");
	destroy();
	pynq_destroy();
	return EXIT_SUCCESS;
	//////////////////////////////// ROBOT STOPS ////////////////////////////////
}

void initialise()
{
	pynq_init();
	stepper_init();
	stepper_enable();
	switchbox_init();
	switchbox_set_pin(IO_AR_SCL, SWB_IIC0_SCL);
	switchbox_set_pin(IO_AR_SDA, SWB_IIC0_SDA);
	switchbox_set_pin(IO_AR0, SWB_UART0_RX);
	switchbox_set_pin(IO_AR1, SWB_UART0_TX);
	iic_init(IIC0);

	// I2C
	gpio_set_direction(IO_A5, GPIO_DIR_OUTPUT);
	gpio_set_level(IO_A5, GPIO_LEVEL_LOW);
	gpio_set_direction(IO_A0, GPIO_DIR_OUTPUT);
	gpio_set_level(IO_A0, GPIO_LEVEL_LOW);
	sleep_msec(100);
	gpio_set_level(IO_A0, GPIO_LEVEL_HIGH);
	sleep_msec(100);

	/* Distance sensor */
	int k;
	printf("DISTANCE SENS:\n");
	// Change the Address of the VL53L0X
	uint8_t addrNew = 0x69;
	uint8_t addrOld = 0x29;
	k = tofSetAddress(IIC0, addrOld, addrNew);
	printf("---Address Change: ");
	if (k != 0)
	{
		printf("Fail\n");
		return;
	}
	printf("Succes\n");

	k = tofPing(IIC0, addrNew);
	printf("---Sensor Ping: ");
	if (k != 0)
	{
		printf("Fail\n");
		return;
	}
	printf("Succes\n");

	// Initialize the sensor
	k = tofInit(&sensorD, IIC0, addrNew, 0); // set default range mode (up to 800mm)
	if (k != 0)
	{
		printf("Problem\n");
		return; // problem - quit
	}
	uint8_t model, revision;

	printf("VL53L0X (distance) device successfully opened.\n");
	tofGetModel(&sensorD, &model, &revision);

	gpio_set_level(IO_A5, GPIO_LEVEL_HIGH);
	sleep_msec(50);

	/* Color sensor */
	// Simple connection test
	uint8_t id = 0x29;
	int i = tcs_ping(IIC0, &id);
	printf("COLOR SENS:\n");
	printf("---Detection: ");
	if (i != TCS3472_SUCCES)
	{
		printf("Fail\n");
		return;
	}
	printf("Success\n");

	// Preconfigure sensor
	tcs_set_integration(&sensorC, tcs3472_integration_from_ms(integration_time_ms));
	tcs_set_gain(&sensorC, x4);
	i = tcs_init(IIC0, &sensorC);
	printf("---Sensor Init: ");
	if (i != TCS3472_SUCCES)
	{
		printf("Fail\n");
		return;
	}
	printf("Success\n");
	printf("TCS3472 (color) device successfully opened.\n");
	sleep_msec(integration_time_ms);
}

void destroy()
{
	stepper_destroy();
	iic_destroy(IIC0);
}

void *threaded_move_start()
{
	int *temp_count = malloc(sizeof(int));
	*temp_count = 0;
	stepper_set_speed(speed_m, speed_m);
	movement = true;
	do
	{
		stepper_steps(-30, -30);
		*temp_count += 30;
		while (stepper_steps_done() == false) // wait until motors are done executing movement
			sleep_msec(10);
	} while (movement == true);
	pthread_exit(temp_count);
}

void move_start()
{
	pthread_create(&thread1, NULL, threaded_move_start, NULL); // call function thread_move_start() to thread
	return;
}

void move_pred()
{
	move_start();
	sleep_msec(pred_distance);
	move_stop();
}

int move_stop()
{
	movement = false; // stop while loop in threaded_move_start

	int *temp;							   // we have to use a (temporary) pointer to save the address of the counter
	pthread_join(thread1, (void **)&temp); // return count_step when thread is finished
	int count_step = *temp;				   // move to regular integer to be able to pass the value after freeing address
	free(temp);
	while (stepper_steps_done() == false) // wait until motors are done executing movement
		sleep_msec(10);
	char str[100];
	sprintf(str, "%i", count_step);
	send_message(str);
	return count_step;
}

void rotate(int angle)
{
	int steps = 2500 * angle / 360;
	stepper_set_speed(speed_r, speed_r);
	stepper_steps(-steps, steps);
	do
	{
		sleep_msec(10);
	} while (stepper_steps_done() == false); // wait until motors are done executing 'motor_steps'

	// send code to GUI python script
	if (angle == 90)
		send_message("R");
	else if (angle == -90)
		send_message("L");
}

void calibrate_border_path() // !might be an issue when angle is too small at approach --> make sure tape is thick enough
{
	int angle = 0;

	// turn until no tape is detected (incr. of 3 degrees)
	while (tape_detect() == 1)
		rotate(3);
	printf("0\n");
	do
	{
		rotate(-3);
	} while (tape_detect() == 0);

	// turn the opposite direction until no tape is detected, whilst tracking angle
	sleep_msec(100);
	do
	{
		rotate(-3);
		angle += -3;
	} while (tape_detect() == 1);

	// divide angle by 2 and turn perpendicular to the tape
	rotate(-angle / 2);
}

int distance_sens()
{
	return tofReadDistance(&sensorD);
}

void scanTrip(bool report_data) // while the border has not been encountered yet, the robots will move forward and avoid any obstacles
{
	if (obstacleEncountered() == true) //&& strcmp(type_obstacle(), "none") != 0) // check before moving forward for an obstacle
	{
		printf("test");
		avoidObstacle();
		if (report_data == true)
			send_message("obstacle_detected");
	}
	printf("0\n");
	move_start();
	sleep_msec(100);
	while (tape_detect() == 0) // && strcmp(type_obstacle(), "valley") != 0) // next we check if the robot encounters the border or obstacles
	{
		printf("1\n");
		if (obstacleEncountered() == true)
		{
			printf("2\n");
			move_stop();
			avoidObstacle();
			if (report_data == true)
				send_message("object_detected");
			move_start();
		}
		printf("looped\n");
	}
	printf("test\n");
	move_stop();
}

bool obstacleEncountered()
{
	// return false;
	// for(int i = 0; i < 500; i ++)
	send_message("check_object");
	printf("check_object\n");
	sleep_msec(25);
	printf(".\n.\n");
	// char *temp_msg = msg;
	while (1)
	{
		char *msg = get_msg();
		// if(strcmp(msg, temp_msg) != 0)
		// printf("%s\n", msg);
		// temp_msg = msg;
		if (tape_detect() == 1 || strcmp(msg, "truee") == 0)
			return true;
		else if (tape_detect() == 0 && strcmp(msg, "false") == 0)
			return false;
	}
}

int tape_detect() // returns 1 for black, 0 for anything else; && ! check valley stuff
{
	tcsReading rgb;
	tcs_get_reading(&sensorC, &rgb);
	// printf("red:%d green:%d blue:%d\n", rgb.red, rgb.green, rgb.blue);
	// char *msg = get_msg();
	// printf("MQTT: %s\n", msg);
	if (rgb.green < 600 && rgb.blue < 600) // black !calibrate
	{
		printf("detected tape\n");
		return 1;
	}
	return 0;
}

void avoidObstacle() // !what if border is the obstacle that it encounters
{
	int x = 0;
	int y = 0;
	int angle = 0;
	while (1)
	{
		if (x == 0 && y == 2)
			break;
		if (obstacleEncountered() == true)
		{
			rotate(90);
			angle += 90;
			if (angle == 360)
				angle = 0;
		}
		else
		{
			move_pred(valley_width);
			switch (angle)
			{
			case 90:
				x -= 1;
				break;
			case 180:
				y -= 1;
				break;
			case 270:
				x += 1;
				break;
			case 0:
				y += 1;
				break;
			}
			rotate(-90);
			angle += -90;
			if (angle < 0)
				angle = 270;
		}
	}
}

char *type_obstacle()
{
	char *amessage = "type_object";
	send_message(amessage);
	char *something = "";
	sleep_msec(2000);
	// while(strcmp(something, "nonee") != 0 || strcmp(something, "valey") != 0 || strcmp(something, "smalr") != 0 || strcmp(something, "smalg") != 0 || strcmp(something, "sblue") != 0 || strcmp(something, "smalw") != 0 || strcmp(something, "sblac") != 0 || strcmp(something, "bigre") != 0 || strcmp(something, "biggr") != 0 || strcmp(something, "bblue") != 0 || strcmp(something, "bigwh") != 0 || strcmp(something, "bblac") != 0)
	// {
	something = get_msg();
	printf("%s\n", something);
	// }
	send_message(something);
	return something;
}

void send_message(const char *message)
{
	uint32_t length = strlen(message);
	uint8_t *len_bytes = (uint8_t *)&length; // Cast uint32_t to array of uint8_t
	printf("<< Outgoing Message: Size = %d\n", length);
	fflush(NULL); // Flush the terminal buffer
	for (uint32_t i = 0; i < 4; i++)
	{
		uart_send(UART0, len_bytes[i]); // Send payload length in bytes
	}
	for (uint32_t i = 0; i < length; i++)
	{
		uart_send(UART0, message[i]); // Send the payload bytes
	}
}

void receive_messages()
{
	pthread_create(&thread2, NULL, threaded_receive_messages, NULL);
}

void *threaded_receive_messages()
{
	while (1)
	{
		if (uart_has_data(UART0))
		{
			uint8_t read_len[4];
			for (uint32_t i = 0; i < 4; i++)
			{
				read_len[i] = uart_recv(UART0); // Read the payload length in bytes
			}
			uint32_t length = *((uint32_t *)read_len); // Cast array to uint32_t number.
			printf(">> Incoming Message: Length = %d\n", length);
			fflush(NULL); // Flush the terminal buffer
			uint32_t i = 0;
			char *buffer = (char *)malloc(sizeof(char) * (length + 1)); // +1 for null terminator
			while (i < length)
			{
				buffer[i] = (char)uart_recv(UART0); // Read the payload into memory
				i++;
			}
			buffer[length] = '\0'; // Null-terminate the string

			// Update the last received message
			if (strcmp(last_received_message, "placeholder") != 0)
			{
				free(last_received_message); // Free the previous message memory
			}
			last_received_message = buffer;

			printf("  >%s\n", last_received_message);
			fflush(NULL); // Flush the terminal buffer
		}
	}
}

char *get_msg()
{
	char *msg = malloc(6 * sizeof(char));
	strncpy(msg, last_received_message, 5);
	msg[5] = '\0';
	return msg;
}