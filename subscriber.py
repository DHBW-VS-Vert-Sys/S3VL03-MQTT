# MQTT Subscriber mit paho-mqtt
import paho.mqtt.client as mqtt


def on_connect(client, userdata, connect_flags, reason_code, properties):
    # This callback runs after connecting to the broker; subscribe to receive
    # every message published on this topic.
    print(f"Connected with result code {reason_code}")
    client.subscribe("test/topic")


def on_message(client, userdata, msg):
    # MQTT payloads arrive as bytes, so decode them before printing as text.
    print(f"{msg.topic} {msg.payload.decode()}")


# Create the MQTT client and register the functions called for broker events.
subscriber = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Connect to the broker on this computer (localhost), using the standard port.
subscriber.connect("localhost", 1883, 60)
try:
    # Keep handling network traffic and incoming messages until Ctrl+C.
    subscriber.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    # Close the connection cleanly when the program stops.
    subscriber.disconnect()
