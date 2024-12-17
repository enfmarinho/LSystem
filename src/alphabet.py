import turtle as t

LINE_SIZE = 30
ALPHABET = {
    "F": lambda: t.forward(LINE_SIZE),
    "f": lambda: t.forward(LINE_SIZE / 2),
    "G": lambda: t.forward(LINE_SIZE),
    "g": lambda: t.forward(LINE_SIZE / 2),
    "[": "This is an edge case",  # TODO improve this implementation avoiding this edge case
    "]": "This is an edge case",
    "r": lambda: t.color("red"),
    "g": lambda: t.color("green"),
    "b": lambda: t.color("blue"),
    "+": lambda angle: t.left(angle),
    "-": lambda angle: t.right(angle),
    "T": lambda current_width, width_increment: t.width(
        current_width + width_increment
    ),
    "t": lambda current_width, width_increment: t.width(
        current_width - width_increment
    ),
}
