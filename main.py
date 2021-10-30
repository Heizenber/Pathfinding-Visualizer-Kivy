from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty
from colors import *
from queue import PriorityQueue

Builder.load_file("interface.kv")


class Spot(Widget):
    color = ListProperty(*get_color_from_hex(WHITE))
    startPresent = False
    endPresent = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        x, y = touch.pos
        if self.collide_point(x, y):
            if not Spot.startPresent and self.color != BLUE:
                self.color = RED
                Spot.startPresent = True

            elif not Spot.endPresent and self.color != RED:
                self.color = BLUE
                Spot.endPresent = True
            else:
                if self.color == BLACK:
                    self.color = WHITE
                elif self.color == RED:
                    self.color = WHITE
                    Spot.startPresent = False
                elif self.color == BLUE:
                    self.color = WHITE
                    Spot.endPresent = False
                else:
                    self.color = BLACK
            return
        else:
            return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        x, y = touch.pos
        if self.collide_point(x, y):
            self.color = BLACK
            return
        else:
            return super().on_touch_down(touch)


class Grid(GridLayout):
    pass


class Interface(BoxLayout):
    pass


class PathfindingApp(App):
    def build(self):
        return Interface()


if __name__ == "__main__":
    PathfindingApp().run()
