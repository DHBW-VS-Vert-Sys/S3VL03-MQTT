import paho.mqtt.client as mqtt

TOPIC = "test/topic"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Verbindung fehlgeschlagen: {reason_code}")
        return

    print("Mit MQTT-Broker verbunden!")
    client.subscribe(TOPIC)


def on_message(client, userdata, message):
    text = message.payload.decode("utf-8", errors="replace")
    print(f"Topic: {message.topic} | Nachricht: {text}")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)
client.loop_forever()

