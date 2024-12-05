import turtle as t


# Trick to avoid a circular import
def stack():
    from renderer import stack as renderer_stack

    renderer_stack()


# Trick to avoid a circular import
def unstack():
    from renderer import unstack as renderer_unstack

    renderer_unstack()


LINE_SIZE = 50
ALPHABET = {
    "F": lambda: t.forward(LINE_SIZE),
    "f": lambda: t.forward(LINE_SIZE / 2),
    "[": lambda: stack(),
    "]": lambda: unstack(),
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
