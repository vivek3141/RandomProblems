import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import matplotlib

x1 = [0.95, 1.317, 1.742]
y1 = [1.548, 1.116, 0.844]


def func(x, a, b):
    return a / (b * x)


def plot(x_data, y_data, color):
    initial = [1, 1]
    t = curve_fit(func, x_data, y_data, initial)
    print(t[0])
    xd = np.linspace(min(x_data), max(x_data), 100)
    fit = [func(x, *t[0]) for x in xd]
    rounded = list(map(lambda x: round(x, 2), t[0]))
    print("{}/({}x)".format(*rounded))
    font = {'family': 'normal',
            'size': 16}

    matplotlib.rc('font', **font)
    plt.plot(xd, fit, color=color, label="$\\frac{" + str((rounded[0])) + "}{" + str((rounded[1])) + "x}$")


plt.title("Total Mass vs Acceleration")
plt.xlabel("Total Mass (kg)")
plt.ylabel(r"Acceleration $(\frac{m}{s^2})$")
plt.scatter(x1, y1, color="r")
plot(x1, y1, color="r")
plt.legend(loc="upper right")
plt.savefig("mass.png")
plt.show()
