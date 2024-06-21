import paho.mqtt.client as paho
import time

class Broker:
    """
    Creates an object that subscribes to MQTT topics and triggers
    a custom method upon receiving a message.

    ### Args:
    - host: The address of the host.
    - username: Username credential.
    - password: Password credential.
    - topicSubList (list[str]): List of topics to subscribe to.
    - messageHandler (function): Triggered when a message is received.
    - client_id: Unique client identifier.
    """
    def __init__(
        self,
        host,
        username: str,
        password: str,
        topicSubList: list[str],
        messageHandler: callable,
        client_id: str
    ) -> None:
        self.client_id = client_id  # Store the client ID
        self.received_message = None  # Initialize a variable to store the last received message
        self.client = paho.Client(client_id=client_id, clean_session=True)
        self.client.username_pw_set(username, password)
        
        # Wrap the provided message handler to check for own messages
        def wrapped_message_handler(client, userdata, message):
            received_msg = message.payload.decode('utf-8')
            if self.client_id in received_msg:
                print(f"Ignored own message: {received_msg}")
                return
            self.received_message = received_msg  # Store the last received message
            messageHandler(client, userdata, message)
        
        self.client.on_message = wrapped_message_handler
        
        self.client.on_connect = self.on_connect
        
        if self.client.connect(host) != 0:
            raise RuntimeError("Couldn't connect to the MQTT host")
        
        self.topicSubList = topicSubList
        
        try:
            # Check for a successful subscription.
            self.client.loop_start()
        except Exception as error:
            print(error)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            for topic in self.topicSubList:
                if self.client.subscribe(topic)[0] != paho.MQTT_ERR_SUCCESS:
                    print(f"Couldn't subscribe to the topic: {topic}")
        else:
            print(f"Failed to connect to MQTT broker, return code: {rc}")
    
    def publish(self, topic, message):
        message_with_id = f"{message}: {self.client_id}"
        result = self.client.publish(topic, message_with_id)
        if result.rc == paho.MQTT_ERR_SUCCESS:
            print(f"Successfully published message: {message_with_id} to topic: {topic}")
        else:
            print(f"Failed to publish message: {message_with_id}, return code: {result.rc}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected from the MQTT broker")

# Define the message handler function
def messageHandler(client, userdata, message):
    # This function will be called when a message is received
    received_msg = message.payload.decode('utf-8')
    print(f"Received message on topic {message.topic}: {received_msg}")
    
    # Write the received message to a text file
    with open("mqtt_messages.txt", "a") as f:
        f.write(f"{received_msg}\n")

# Generate a unique client ID
client_id = f"MQTT_Client_ID_{time.time()}"

# Instantiate the Broker class with the provided arguments
broker = Broker(
    "mqtt.ics.ele.tue.nl",  # MQTT broker host
    "Student149",  # Username
    "ju2Shahn",  # Password
    ["/pynqbridge/77/send", "/pynqbridge/77/recv"],  # Topics
    messageHandler,  # Message handler function
    client_id  # Client ID
)

# broker = Broker(
#     "mqtt.ics.ele.tue.nl",  # MQTT broker host
#     "Student147",  # Username
#     "eereej6E",  # Password
#     ["/pynqbridge/76/send", "/pynqbridge/76/recv"],  # Topics
#     messageHandler,  # Message handler function
#     client_id  # Client ID
# )

# Define the array with the specified elements

# while True:
#     # Print the current element
#     print(elements[index])
    
#     # Move to the next element
#     index += 1
    
#     # Reset index to 0 if it exceeds the array length
#     if index >= len(elements):
#         index = 0

# Keep the script running to listen for incoming messages
index = 0
try:
    while True:
        elements = [
        "blue block",
        "green block",
        "obstacle detected",
        "black block",
        "white block",
        "cliff",
        "boundary detected"
        ]

        # Move to the next element
        index += 1
        
        # Reset index to 0 if it exceeds the array length
        if index >= len(elements):
            index = 0
        broker.publish("/pynqbridge/77/send", {elements[index]})  # Publish message to topic
        time.sleep(5)
except KeyboardInterrupt:
    # Ensure to disconnect the broker after listening
    broker.disconnect()
    print("Listener stopped")

# Access the last received message
# print("Last received message:", broker.received_message)
