from pgl import GWindow, GRect, GOval, GObject
from random import uniform


def generate_objects(size: int) -> dict[str, "GObject"]:
    """Generates the basic objects

    Objects are added to a dictionary for later access.
    """
    d = {}

    rough = GRect(0, 0, size, size)
    rough.set_filled(True)
    rough.set_color("darkgreen")
    d["rough"] = rough

    tee = GRect(0.1 * size, 0.7 * size, 0.2 * size, 0.2 * size)
    tee.set_filled(True)
    tee.set_color("green")
    d["tee"] = tee

    hole = GOval(
        uniform(0.5, 0.9) * size, uniform(0.1, 0.5) * size, 0.06 * size, 0.06 * size
    )
    hole.set_filled(True)
    hole.set_color("black")
    d["hole"] = hole

    ball = GOval((0.2 - 0.025) * size, (0.8 - 0.025) * size, 0.05 * size, 0.05 * size)
    ball.set_filled(True)
    ball.set_color("white")
    d["ball"] = ball

    bar = GRect(0.05 * size, 0.95 * size, 0, 0.025 * size)
    bar.set_filled(True)
    bar.set_color("red")
    d["power_bar"] = bar

    return d


def get_velocity_components_towards_mouse(
    ball_loc: tuple[float, float], mouse_loc: tuple[float, float], power: int | float
) -> tuple[float, float]:
    """Computes a new velocity for a ball to head towards the mouse.

    Returns a velocity that aims the ball towards the mouse with "power" speed.
    """
    bx, by = ball_loc
    mx, my = mouse_loc
    dist = ((mx - bx) ** 2 + (my - by) ** 2) ** (1 / 2)
    vx = (mx - bx) / dist * power
    vy = (my - by) / dist * power
    return vx, vy


SIZE = 600
gw = GWindow(SIZE, SIZE)
objs = generate_objects(SIZE)
for _, obj in objs.items():
    gw.add(obj)
