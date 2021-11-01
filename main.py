from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from algorithms.AStarAlgorithm import aStarAlgo
from algorithms.DijkstraAlgorithm import dijkstraAlgo
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex, get_hex_from_color
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from threading import Thread
from colors import *
from queue import PriorityQueue

Builder.load_file("interface.kv")


algorithms = {"A* Algorithm": aStarAlgo, "Dijkstra": dijkstraAlgo}


class Spot(Widget):
    color = ListProperty(get_color_from_hex(WHITE))
    startPresent = False
    endPresent = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        x, y = touch.pos
        if self.collide_point(x, y):
            if not Spot.startPresent and get_hex_from_color(self.color) != BLUE:
                self.color = get_color_from_hex(RED)
                Spot.startPresent = True

            elif not Spot.endPresent and get_hex_from_color(self.color) != RED:
                self.color = get_color_from_hex(BLUE)
                Spot.endPresent = True
            else:
                if get_hex_from_color(self.color) == BLACK:
                    self.color = get_color_from_hex(WHITE)
                elif get_hex_from_color(self.color) == RED:
                    self.color = get_color_from_hex(WHITE)
                    Spot.startPresent = False
                elif get_hex_from_color(self.color) == BLUE:
                    self.color = get_color_from_hex(WHITE)
                    Spot.endPresent = False
                else:
                    if (
                        get_hex_from_color(self.color) != RED
                        or get_hex_from_color(self.color) != BLUE
                    ):
                        self.color = get_color_from_hex(BLACK)
            return True
        else:
            return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        x, y = touch.pos
        if self.collide_point(x, y):
            if (
                get_hex_from_color(self.color) != RED
                or get_hex_from_color(self.color) != BLUE
            ):
                self.color = get_color_from_hex(BLACK)
            return True
        else:
            return super().on_touch_down(touch)


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 34
        self.cols = 41
        self.spacing = 1
        self.grid = [self.add_widget(Spot()) for _ in range(self.rows * self.cols)]
        self.edge_y = Window.height / self.rows
        self.edge_x = Window.width / self.cols
        self.current = None
        self.open_set = []
        self.closed_set = []
        self.end = None

    def start(self):
        if Spot.startPresent and Spot.endPresent:
            Thread(
                target=algorithms[Interface.root.ids.text], args=(), daemon=True
            ).start()
        else:
            popup = Popup(
                title="Warning!",
                content=Label(
                    text="Place a starting and ending position\n"
                    "\t\tfor algorithm to start!"
                ),
                auto_dismiss=False,
            )
            popup.open()


class Interface(BoxLayout):
    pass


class PathfindingApp(App):
    def build(self):
        return Interface()


if __name__ == "__main__":
    PathfindingApp().run()
