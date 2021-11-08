from kivy.animation import Animation
from kivy.graphics import Ellipse, Color, Rectangle
from kivy.uix.widget import Widget
from colors import *


def animate_coloring(widget, color, *args):
    print(color)
    x_center, y_center = widget.center_x, widget.center_y
    size_x, size_y = widget.width * 0.1, widget.height * 0.1
    with widget.canvas:
        Color(BLACK)
        rect = Rectangle(
            size=(size_x, size_y), pos_hint={"center_x": x_center, "center_y": y_center}
        )
        rect
    anim = Animation(size=(widget.width, widget.height), duration=2)
    anim.start(rect)


# class Ellipse(Widget):
