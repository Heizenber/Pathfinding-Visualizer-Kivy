from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from algorithms.AStarAlgorithm import aStarAlgo
from algorithms.DijkstraAlgorithm import dijkstraAlgo
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from threading import Thread
from colors import *


Builder.load_file("interface.kv")


algorithms = {"A* Algorithm": aStarAlgo, "Dijkstra": dijkstraAlgo}


class Node(Widget):
    color = ListProperty(WHITE)
    startPresent = False
    endPresent = False

    def __init__(self, row, col, **kwargs):
        super().__init__(**kwargs)
        self.id = str(row) + "-" + str(col)
        self.row = row
        self.col = col
        self.distanceFromStart = float("inf")
        self.estimatedDistanceToEnd = float("inf")
        self.cameFrom = None

    def on_touch_down(self, touch):
        x, y = touch.pos
        if self.collide_point(x, y):
            if not Node.startPresent and get_hex_from_color(self.color) != BLUE:
                self.color = get_color_from_hex(RED)
                Node.startPresent = True

            elif not Node.endPresent and get_hex_from_color(self.color) != RED:
                self.color = get_color_from_hex(BLUE)
                Node.endPresent = True
            else:
                if touch.button == "right":
                    if get_hex_from_color(self.color) == BLACK:
                        self.color = get_color_from_hex(WHITE)
                # if get_hex_from_color(self.color) == BLACK:
                #     self.color = get_color_from_hex(WHITE)
                # elif get_hex_from_color(self.color) == RED:
                #     self.color = get_color_from_hex(WHITE)
                #     Node.startPresent = False
                # elif get_hex_from_color(self.color) == BLUE:
                #     self.color = get_color_from_hex(WHITE)
                #     Node.endPresent = False
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
        self.generate_grid()
        self.open_set = []
        self.closed_set = []

    def generate_grid(self):
        self.grid = [
            self.add_widget(Node(i, j))
            for j in range(self.cols)
            for i in range(self.rows)
        ]

    def start(self):
        if Node.startPresent and Node.endPresent:
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
    Window.clearcolor = get_color_from_hex(LIGHT_GRAY)
    PathfindingApp().run()
