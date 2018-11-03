import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np

x1 = [0.618, 1.07, 1.548]
y1 = [0.49, 0.98, 1.47]
slope = (y1[0] - y1[2]) / (x1[0] - x1[2])


def func(x, a, b):
    return (a * x) + b


def plot(x1, y1, color):
    x = np.linspace(min(x1), max(x1), 300)
    power_smooth = spline(x1, y1, x)
    plt.plot(x, power_smooth, color=color)


plt.title("Acceleration vs Accelerating Force")
plt.xlabel(r"Acceleration $(\frac{m}{s^2})$")
plt.ylabel("Accelerating Force (N)")
plt.scatter(x1, y1, color="b")
plt.plot(x1, y1, color="b", label="y = {}x + {}".format(round(slope, 2), round(y1[0] - slope * x1[0], 2)))
plt.legend(loc="upper left")
plt.savefig("./Graphsacceleration.png")
plt.show()
