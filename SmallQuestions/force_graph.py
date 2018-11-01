import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x1 = [4.58, 9.48, 14.386]
y1 = [1.47, 2.45, 4.41]
slope = (y1[0] - y1[2]) / (x1[0] - x1[2])


def plot(x1, y1, color):
    i = [1,1]

    x = np.linspace(min(x1), max(x1), 300)
    plt.plot(x, line, color=color)


plt.title("Acceleration vs Accelerating Force")
plt.xlabel(r"Acceleration $(\frac{m}{s^2})$")
plt.ylabel("Accelerating Force (N)")
plt.scatter(x1, y1, color="b")
plt.plot(x1, y1, color="b", label="y = {}x + {}".format(round(slope, 2), round(y1[0] - slope * x1[0], 2)))
plt.legend(loc="upper left")
plt.savefig("force_1.png")
plt.show()
