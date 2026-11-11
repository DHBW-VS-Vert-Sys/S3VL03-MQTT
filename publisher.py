# MQTT Publisher mit paho-mqtt
import paho.mqtt.client as mqtt


# Create a client and connect to the broker on this computer.
publisher = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
publisher.connect("localhost", 1883, 60)
# Run the network loop in the background so the publish can complete.
publisher.loop_start()
try:
    # Send a message to the same topic the subscriber listens to.
    print("Publishing message to test/topic")
    publish_info = publisher.publish("test/topic", "Hello MQTT")
    publish_info.wait_for_publish(timeout=10)
    if not publish_info.is_published():
        raise TimeoutError("Timed out publishing the message")
    print("Message published successfully")
finally:
    # Disconnect and stop the background network loop.
    publisher.disconnect()
    publisher.loop_stop()
