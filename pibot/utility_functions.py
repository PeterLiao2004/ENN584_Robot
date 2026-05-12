import numpy as np


def wrap_to_pi(x):
    while x < -np.pi:
        x += 2 * np.pi
    while x > np.pi:
        x -= 2 * np.pi
    return x


def wrap_to_180(x):
    while x < -180:
        x += 360
    while x > 180:
        x -= 360
    return x
