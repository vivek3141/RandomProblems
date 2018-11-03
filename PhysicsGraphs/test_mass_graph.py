import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

y1 = [1.664, 1.01, 1.016]
x1 = [0.4, 0.9, 1.4]


def func(x, a, b, c):
    return a + b * np.exp(c * x)


def plot(x_data, y_data, color):
    initial = [1, 1, -1]
    t = curve_fit(func, x_data, y_data, initial, maxfev=1000000)
    print(t[0])
    xd = np.linspace(min(x_data), max(x_data), 100)
    fit = [func(x, *t[0]) for x in xd]
    fun = "{} + {}e^{}x".format(*list(map(lambda x: round(x, 2), t[0])))
    plt.plot(xd, fit, color=color, label=fun)


plt.title("Total Mass vs Acceleration")
plt.xlabel("Total Mass (kg)")
plt.ylabel(r"Acceleration $(\frac{m}{s^2})$")
plt.scatter(x1, y1, color="r")
plot(x1, y1, color="r")
plt.legend(loc="upper right")
plt.savefig("mass_2.png")
plt.show()
