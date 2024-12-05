import turtle as t

LINE_SIZE = 50
ALPHABET = {
    "F": lambda: t.forward(LINE_SIZE),
    "f": lambda: t.forward(LINE_SIZE / 2),
    "[": "",
    "]": "",
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
