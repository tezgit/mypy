from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class DemoApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x="left",
            anchor_y="top"
        )
        but1 = Button(
            text="Anch Layout",
            size_hint=(.2, .2),
            background_color=(0.0, 200, 200),
            color=(0, 0, 0, 1)
        )
        layout.add_widget(but1)
        return layout


DemoApp().run()
