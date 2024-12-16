import turtle as t
from collections import namedtuple

from alphabet import ALPHABET

WIDTH_INCREMENT = 1


class Renderer:
    def __init__(self, angle):
        self.m_stack = []
        self.current_line_width = 2
        self.angle = angle

    def __del__(self):
        t.exitonclick()

    def stack(self):
        State = namedtuple("State", ["position", "direction", "color", "tickness"])
        state = State(
            position=t.position(),
            direction=t.heading(),
            color=t.pencolor(),
            tickness=t.pensize(),
        )
        self.m_stack.append(state)
        self.position = t.position()
        self.heading = t.heading()
        self.color = t.color()

    def unstack(self):
        current_state = self.m_stack.pop()
        t.setposition(current_state.position)
        t.setheading(current_state.direction)
        t.color(current_state.color)
        t.pensize(current_state.tickness)

    def render(self, l_system):
        for variable in l_system:
            if variable == "[":
                self.stack()
            elif variable == "]":
                self.unstack()
            elif variable == "+" or variable == "-":
                ALPHABET[variable](self.angle)
            elif variable == "T" or variable == "t":
                ALPHABET[variable](self.current_line_width, WIDTH_INCREMENT)
            else:
                ALPHABET[variable]()
