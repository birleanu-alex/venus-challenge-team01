import sys
import json
import math
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
# from mqtt import Broker
import time
import numpy as np

from app_ui import Ui_MainWindow

'''
# Define the message handler function
def messageHandler(client, userdata, message):
    # This function will be called when a message is received
    # Implement your message handling logic here
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")

# Generate a unique client ID
client_id = f"MQTT_Client_ID_{time.time()}"

# Instantiate the Broker class with the provided arguments
broker = Broker(
    "mqtt.ics.ele.tue.nl",  # MQTT broker host
    "Student01",  # Username
    "epuo8ieF",  # Password
    ["/pynqbridge/1/send", "/pynqbridge/1/recv"],  # Topics
    messageHandler,  # Message handler function
    client_id  # Client ID
)
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [4, 5]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_motor_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def on_motor_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_sensor_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def on_sensor_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_logs_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def on_logs_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

def read_commands(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def calculate_position(x, y, direction, value):
    if direction == 'N':
        y += value
    elif direction == 'E':
        x += value
    elif direction == 'S':
        y -= value
    elif direction == 'W':
        x -= value
    return x, y

#####Read text######

def process_commands(commands):
    directions = ['N', 'E', 'S', 'W']
    current_direction_index = 0
    x, y = 0, 0

    xperimeter = int(commands[1])
    yperimeter = int(commands[2])

    robot_data = {
        "corners": [],
        "borders": [],
        "hills": [],
        "valleys": [],
        "rocks": []
    }

    scale_x = xperimeter / 30
    scale_y = yperimeter / 30

    for command in commands[3:]:
        if command == 'r':
            current_direction_index = (current_direction_index + 1) % 4
        elif command == 'l':
            current_direction_index = (current_direction_index - 1) % 4
        elif command.isdigit():
            value = int(command)
            x, y = calculate_position(x, y, directions[current_direction_index], value)
        elif command == 'm':
            hill_position = (math.ceil(x / scale_x), math.ceil(y / scale_y))
            robot_data["hills"].append(hill_position)
        elif command == 'c':
            valley_position = (math.ceil(x / scale_x), math.ceil(y / scale_y))
            robot_data["valleys"].append(valley_position)
        elif ',' in command:
            color, size_descriptor = command.split(',')
            size = 5 if size_descriptor.strip() == 'big' else 2
            rock_position = (math.ceil(x / scale_x), math.ceil(y / scale_y))
            robot_data["rocks"].append({
                "position": rock_position,
                "size": size,
                "color": color.strip()
            })

    return robot_data

def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

########Draw map#######

# Function to load data from a JSON file
def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Load robot data from calculated.json
robot_data = load_data_from_file('calculated.json')

def draw_map(data):
    fig, ax = plt.subplots()

    # Plot corners
    if "corners" in data and data["corners"]:
        corners = np.array(data["corners"])
        if corners.ndim == 2 and corners.shape[1] == 2:
            ax.plot(corners[:, 0], corners[:, 1], 'ks', label='Corners')

    # Plot borders
    if "borders" in data and data["borders"]:
        borders = np.array(data["borders"])
        if borders.ndim == 2 and borders.shape[1] == 2:
            ax.plot(borders[:, 0], borders[:, 1], 'k-', label='Borders')

    # Plot hills
    if "hills" in data and data["hills"]:
        hills = np.array(data["hills"])
        if hills.ndim == 2 and hills.shape[1] == 2:
            ax.plot(hills[:, 0], hills[:, 1], 'y^', label='Hills')

    # Plot valleys
    if "valleys" in data and data["valleys"]:
        valleys = np.array(data["valleys"])
        if valleys.ndim == 2 and valleys.shape[1] == 2:
            ax.plot(valleys[:, 0], valleys[:, 1], 'mv', label='Valleys')

    # Plot rocks
    if "rocks" in data:
        for rock in data["rocks"]:
            position = rock["position"]
            size = rock["size"] * 15  # Adjust size for plotting
            color = rock["color"]
            ax.scatter(position[0], position[1], s=size, c=color, label=f'Rock (Size {rock["size"]}, Color {color})')

    # Add labels, legend, and grid
    ax.set_xlabel('X coordinate')
    ax.set_ylabel('Y coordinate')
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())
    ax.grid(True)
    ax.set_title('Robot Map')

    plt.show()

########Draw map done######

if __name__ == "__main__":

    app = QApplication(sys.argv)

    with open('style.qss', 'r') as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()



    ###Read text####
    # Read commands from the text file
    commands = read_commands('test.txt')

    # Process the commands to generate the robot data
    robot_data = process_commands(commands)

    # Save the robot data to a JSON file
    save_to_json(robot_data, 'calculated.json')

    # Output the JSON data for verification
    print(json.dumps(robot_data, indent=4))
    ###Draw map####
    draw_map(robot_data)


    # try:

    #     while not robot_sopped:
    #         # receive the message from the robot
    #         broker.publish("/pynqbridge/1/recv", "sample")
    #         time.sleep(1)

    #         # data processing from the commands

    #         # displaying the map

    # except KeyboardInterrupt:
    #     print("Program has been stopped by user.")

    sys.exit(app.exec())