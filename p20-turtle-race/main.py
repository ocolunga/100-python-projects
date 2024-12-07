import os
import sys

os.environ["TCL_LIBRARY"] = os.path.join(os.path.dirname(sys.executable), "..", "lib", "tcl8.6")

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)


screen.exitonclick()