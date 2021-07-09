from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from pythonosc.udp_client import SimpleUDPClient
from pythonosc import dispatcher
from pythonosc import osc_server

oscdestIP = "127.0.0.1"  # "192.168.0.170"
port = 9999
client = SimpleUDPClient(oscdestIP, port)  # Create client
# test send
client.send_message("/test/floatparam", 123.23)   # Send float message


class Demo(GridLayout):

    slid1val = ObjectProperty(None)
    slid2val = ObjectProperty(None)

    def on_slid1(self):
        sv = self.slid1.value
        # print("slider value is {}".format(self.slid.value))
        self.slid1val.text = str(self.slid1.value)
        client.send_message("/kivyOSC/slider1", sv)

    def on_slid2(self):
        # print("slider value is {}".format(self.slid.value))
        sv = self.slid2.value
        self.slid2val.text = str(self.slid2.value)
        client.send_message("/kivyOSC/slider2", sv)


class kivyOSCApp(App):
    def build(self):
        return Demo()


kivyOSCApp().run()
