from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image


class Kivy_UI(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.rows = 4

        self.img = Image(
            source="domucha.png"
        )
        self.add_widget(self.img)
        ###
        self.lab = Label(
            text="Enter your name"
        )
        self.add_widget(self.lab)
        ###
        self.txtin = TextInput(
            text="...",
            font_size=40
        )
        self.add_widget(self.txtin)
        ###
        self.b1 = Button(
            text="submit",
        )
        self.b1.bind(on_press=self.call_back)
        self.add_widget(self.b1)
        ###
        self.popup = Popup(
            title="pop display",
            size=(200, 200),
            content=Label(
                text=""
            )
        )
        ###

    def call_back(self, elem):
        self.popup.content.text = self.txtin.text
        self.popup.open()


class DemoApp(App):
    def build(self):
        return Kivy_UI()


DemoApp().run()
