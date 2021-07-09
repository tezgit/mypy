from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Float_layout_Demo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.b1 = Button(
            text="Button1",
            size_hint=(0.4, 0.4),
            pos_hint={"x": 0.3, "y": 0.2}
        )
        self.add_widget(self.b1)

        self.b2 = Button(
            text="Button2",
            size_hint=(0.1, 0.2),
            pos_hint={"x": 0.8, "y": 0.7}
        )
        self.add_widget(self.b2)


class DemoApp(App):
    def build(self):
        return Float_layout_Demo()


DemoApp().run()
