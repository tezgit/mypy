from queue import Queue
import paho.mqtt.client as mqtt  # import the client1
import time
import pyg

q = Queue()
messages = []

broker_name = "saplay"  # saplay  # playatez
# >> mqtt://saplay:lLH036OTCfVqF7hD@saplay.cloud.shiftr.io
# >> mqtt://playatez:6EGKYTF2LrDvfJpp@playatez.cloud.shiftr.io
# >> mqtt://tngplay:mgtcePFrKT2lNXKe@tngplay.cloud.shiftr.io


vPlayers = ["VP1", "VP2", "VP3"]
vSequence = [0, 1, 2]
totplayers = len(vPlayers)
currSeq = -1
currFile = 1
maxSeq = 2
maxFiles = 2


def on_connect(client, userdata, flags, rc):
    client1.connected_flag = True
    # messages.append(m)
    # print(m)


def on_message(client1, userdata, message):
    global messages
    global msgflag

    msgflag = False
    # m = "message ", str(message.topic), str(message.payload.decode("utf-8"))
    m = str(message.topic), str(message.payload.decode("utf-8"))
    messages.append(m)  # put messages in list
    q.put(m)  # put messages on queue
    print(m)
    if(m[0] == "events/ended"):
        print("reached end of video " + m[1])
    print("messages list: " + str(messages))
    pyg.msgbar(1)
    v_play_next()


def on_publish(client, userdata, mid):
    global messages
    m = "on publish callback mid "+str(mid)
    # messages.append(m)


def on_subscribe(client, userdata, mid, granted_qos):
    m = "on_subscribe callback mid "+str(mid)


Q0S = 0
# broker_address="192.168.1.68"
broker_address = "tngplay.cloud.shiftr.io"  # use external broker
# broker_address = "saplay.cloud.shiftr.io"  # use external broker
# broker_address = "playatez.cloud.shiftr.io"  # use external broker
client1 = mqtt.Client("TNG1")  # create new instance
client1.username_pw_set(username="tngplay", password="mgtcePFrKT2lNXKe")
# client1.username_pw_set(username="saplay", password="lLH036OTCfVqF7hD")
# client1.username_pw_set(username="playatez", password="6EGKYTF2LrDvfJpp")

client1.on_connect = on_connect  # attach function to callback
client1.on_message = on_message  # attach function to callback
client1.on_publish = on_publish  # attach function to callback
# client1.on_subscribe =on_subscribe        #attach function to callback

time.sleep(1)
print("connecting to broker")
client1.connected_flag = False
client1.connect(broker_address)  # connect to broker
client1.subscribe("presence", 0)
client1.subscribe("events/ended", 0)
print("starting the loop")
client1.loop_start()  # start the loop
# print("subscribing events/ended = ", 0)  # Q0S)


while not client1.connected_flag:
    print("waiting for connect")
    time.sleep(0.5)
print("konnected jajaja!")


while not q.empty():
    message = q.get()
    print("queue: ", message)
while len(messages) > 0:
    print(messages.pop(0))
# client1.disconnect()
# client1.loop_stop()


def v_play_next():
    global vPlayers, vSequence, maxFiles, maxSeq, currFile, currSeq
    global client1

    print("xcurrSeq: " + str(currSeq) + " xcurrFile: " + str(currFile))

    if(currSeq < maxSeq):
        currSeq += 1

    else:
        currSeq = 0
        if(currFile <= maxFiles):
            currFile += 1
        else:
            currFile = 1

    print("currSeq: " + str(currSeq) + " currFile: " + str(currFile))

    # reshuffle_sequence()

    nextplayer = vPlayers[vSequence[currSeq]]
    print("nextplayer: " + nextplayer)

    nextFile = nextFileName(vSequence[currSeq]+1, currFile)
    print("nextFile: " + nextFile)

    client1.publish(nextplayer + "/url", nextFile)


# ---------- DO NOT TOUCH THIS -------------------------#


def nextFileName(nn, cs):
    file_dir = "http://www.phonomena.net/test/"
    if(cs < 10):
        ns = "0"+str(cs)
    else:
        ns = str(cs)
    myfilename = file_dir + "v_" + str(nn) + "_" + ns + ".mp4"
    print("myFileName: " + myfilename)
    return myfilename
