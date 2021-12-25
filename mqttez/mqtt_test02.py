import paho.mqtt.client as mqtt  # import the client1
import time

# broker_address = "192.168.1.184"
broker_address = "saplay.cloud.shiftr.io"  # use external broker
client = mqtt.Client("PT1")  # create new instance
client.username_pw_set(username="saplay", password="lLH036OTCfVqF7hD")

# client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message

topics = [("events/ended", 0), ("presence", 1)]
topic_ack = []
print("connecting to broker")
try:
    client.connect(broker_address)
except:
    print("sorry can't connect!")
    sys.exit(1)

client.loop_start()  # start loop
while not client.connected_flag:
    print("in wait loop")
    time.sleep(1)

print("subscribing " + str(topics))
for r in topics:
    try:
        r = client.subscribe(t)
        if r[0] == 0:
            logging.info("subscribed to topic " +
                         str(t[0]) + "return code" + "...")
            topic_ack.append([t[0], r[1], 0])
        else:
            logging.info("error on subscribing " + str(r))
            client.loop.stop()
            sys.exit(1)
    except Exception as e:
        logging.info("error on subsdcribing " + str(e))
        client.loop.stop()
        sys.exit(1)
print("waiting for all subs")
while not(check_subs()):
    time.sleep(1)

msg = "off"
print("publishing topic = " + topics[0][0], " message= ", msg)
client.publish(topics[0][0], msg)
time.sleep(4)
client.loop_stop()
client.disconnect()


client.publish(
    "sam/url", "http://www.phonomena.net/test/videotest-02.mp4")  # publish

client.publish(
    "sa1/url", "http://www.phonomena.net/test/linell.mp3")  # publish

client.publish(
    "sai/url", "http://www.phonomena.net/test/videotest-01.mp4")  # publish

client.subscribe("events/ended", 1)


# while True:
#     pass
