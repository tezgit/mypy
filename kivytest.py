from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from pythonosc.udp_client import SimpleUDPClient
from pythonosc import dispatcher
from pythonosc import osc_server
import random


oscdestIP = "127.0.0.1"  # "192.168.0.170"
port = 9999
client = SimpleUDPClient(oscdestIP, port)  # Create client
# test send
client.send_message("/test/floatparam", 123.11)   # Send float message
# Send message with int, float and string
# client.send_message("/test/moreparams", [1, 2., "hello"])
#########################################


class TestApp(App):
    def build(self):
        return Button(text='Hello World')

    def Lab(self):
        return Label(text='label test')

    def AppOSC(self):
        myrandnum = random.random()  # random float number between 0 and 1

        client.send_message("/app/sendmess", myrandnum)  # Send float message
        print("sent 2 xOSC test messages")


# pippo = TestApp()

# pippo.AppOSC()
# pippo.run()

TestApp().run()
TestApp().Lab()
TestApp().AppOSC()
