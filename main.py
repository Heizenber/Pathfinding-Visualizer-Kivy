from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from colors import *
from queue import PriorityQueue

Builder.load_file("interface.kv")


class Spot(Widget):
    pass


class Grid(GridLayout):
    pass


class Interface(BoxLayout):
    pass


class PathfindingApp(App):
    def build(self):
        return Interface()


if __name__ == "__main__":
    PathfindingApp().run()
