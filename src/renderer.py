import turtle as t
from collections import namedtuple

from alphabet import ALPHABET


class Renderer:
    def __init__(self, angle, width_increment):
        self.m_stack = []
        self.current_width = 1
        self.angle = angle
        self.width_increment = width_increment

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
        for char in l_system:
            if char == "[":
                self.stack()
            elif char == "]":
                self.unstack()
            elif char == "+" or char == "-":
                ALPHABET[char](self.angle)
            elif char == "T" or char == "t":
                ALPHABET[char](self.current_width, self.width_increment)
            else:
                ALPHABET[char]()