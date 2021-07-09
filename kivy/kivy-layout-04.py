from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Page_layout_Demo(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.b1 = Button(
            text="Button1",
        )
        self.add_widget(self.b1)

        self.b2 = Button(
            text="Button2",
        )
        self.add_widget(self.b2)

        self.b3 = Button(
            text="Button3",
        )
        self.add_widget(self.b3)


class DemoApp(App):
    def build(self):
        return Page_layout_Demo()


DemoApp().run()
