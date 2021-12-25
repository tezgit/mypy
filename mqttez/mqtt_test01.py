import paho.mqtt.client as mqtt  # import the client1
# broker_address = "192.168.1.184"
broker_address = "saplay.cloud.shiftr.io"  # use external broker
# broker_address = "playatez.cloud.shiftr.io"  # use external broker
client = mqtt.Client("PT1")  # create new instance
client.username_pw_set(username="saplay", password="lLH036OTCfVqF7hD")
# client.username_pw_set(username="playatez", password="6EGKYTF2LrDvfJpp")

client.connect(broker_address)  # connect to broker

client.publish(
    "sa1/url", "http://www.phonomena.net/test/v_1_01.mp4")  # publish
client.publish("sa1/command", "loop")
client.publish(
    "sa2/url", "http://www.phonomena.net/test/v_2_01.mp4")  # publish
client.publish("sa2/command", "loop")
client.publish(
    "sa3/url", "http://www.phonomena.net/test/v_3_01.mp4")  # publish
client.publish("sa3/command", "loop")

# client.publish("sam/command", "noloop")
client.publish(
    "sam/url", "http://www.phonomena.net/test/v_2_01.mp4")  # publish

# client.publish("sai/command", "noloop")
client.publish(
    "sai/url", "http://www.phonomena.net/test/v_3_01.mp4")  # publish

client.subscribe("events/ended", 1)


# while True:
#     pass
