import paho.mqtt.client as mqtt  # import the client1
import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))


mqttBroker = "playatez.cloud.shiftr.io"
client = mqtt.Client("T13")
client.username_pw_set(username="playatez", password="6EGKYTF2LrDvfJpp")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("event/ended")
client.on_message = on_message

time.sleep(30)
client.loop_stop()
