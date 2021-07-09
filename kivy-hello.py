from kivy.uix.button import Label
from kivy.app import App
# File name: hello.py
import kivy
kivy.require('1.7.0')


class HelloApp(App):
    def build(self):
        return Label(text='Hello World!')


if __name__ == "__main__":
    HelloApp().run()
