from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Grid_Layout_Demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 1

        self.l1 = Label(
            text="click the button below"
        )
        self.add_widget(self.l1)

        self.b1 = Button(
            text="Click Me",
            background_color=(200, 200, 0),
            color=(0, 0, 1, 1)
        )
        self.add_widget(self.b1)


class DemoApp(App):
    def build(self):
        return Grid_Layout_Demo()


DemoApp().run()
