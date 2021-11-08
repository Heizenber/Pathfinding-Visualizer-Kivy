from kivy.config import Config

Config.set("input", "mouse", "mouse,multitouch_on_demand")
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
from kivy.properties import ObjectProperty


Builder.load_file("interface.kv")


algorithms = {"A* Algorithm": aStarAlgo, "Dijkstra": dijkstraAlgo}


class Node(Widget):
    color = ListProperty(WHITE)
    startPresent = False
    endPresent = False

    def __init__(self, row, col, **kwargs):
        super().__init__(**kwargs)
        self.idx = str(row) + "-" + str(col)
        self.row = row
        self.col = col
        self.isStart = False
        self.isEnd = False
        self.distanceFromStart = float("inf")
        self.estimatedDistanceToEnd = float("inf")
        self.cameFrom = None

    def on_touch_down(self, touch):
        x, y = touch.pos
        if self.collide_point(x, y):
            if touch.button == "left":
                if self.color == WHITE:
                    if Node.startPresent == False:
                        self.color = BLUE
                        Node.startPresent = True
                        self.isStart = True
                    elif self.endPresent == False:
                        self.color = BROWN
                        Node.endPresent = True
                        self.isEnd = True
                    elif self.color != BLUE or self.color != RED:
                        self.color = BLACK
            elif touch.button == "right" and self.color != WHITE:
                if self.color == BLUE:
                    Node.startPresent = False
                    self.isStart = False
                elif self.color == BROWN:
                    Node.endPresent = False
                    self.isEnd = False
                self.color = WHITE

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        self.on_touch_down(touch)
        return super().on_touch_down(touch)

    def __lt__(self, other):
        return False


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
        self.matrix = [[Node(i, j) for j in range(self.cols)] for i in range(self.rows)]
        [self.add_widget(node) for row in self.matrix for node in row]
        self.grid = [self.matrix]

    def start(self, algorithm):
        if Node.startPresent and Node.endPresent:
            Thread(
                target=algorithms[algorithm],
                args=(self.grid),
                daemon=True,
            ).start()
        else:
            popup = Popup(
                title="\t\tWarning!",
                content=Label(
                    text="Place a starting and ending position\n"
                    "\t\tfor algorithm to start!"
                ),
                auto_dismiss=False,
            )
            popup.open()

    def clear(self):
        Thread(target=self.clear_widgets, daemon=True).start()
        Node.startPresent = False
        Node.endPresent = False
        self.generate_grid()


class Interface(BoxLayout):
    grid = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clear_grid(self):
        self.grid.clear()

    def start_algorithm(self):
        self.grid.start(self.ids.algorithm.text)


class PathfindingApp(App):
    def build(self):
        return Interface()


if __name__ == "__main__":
    Window.clearcolor = LIGHT_GRAY
    PathfindingApp().run()
