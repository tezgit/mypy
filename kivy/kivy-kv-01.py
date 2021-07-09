from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class Demo(GridLayout):
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    slidval = ObjectProperty(None)

    def on_click(self):
        print("my name is {} and I am {} years old".format(
            self.name.text, self.age.text))

        self.name.text = ""
        self.age.text = ""
        # self.age.slid = ""

    def on_slid(self):
        # print("slider value is {}".format(self.slid.value))
        self.slidval.text = str(self.slid.value)


class MyFirstApp(App):
    def build(self):
        return Demo()


MyFirstApp().run()
