import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x1 = [3.23, 8.134, 13.034]
y1 = [0.344, 1.327, 2.084]


def func(x, a, b):
    return (x * a) + b


def plot(x_data, y_data, color):
    i = [1, 1]
    t = curve_fit(func, x_data, y_data, i)
    print(t[0])
    xd = np.linspace(min(x_data), max(x_data), 100)
    line = [func(x, *t[0]) for x in xd]
    rounded = list(map(lambda x: round(x, 3), t[0]))
    l = "{}x+ {}".format(*rounded)
    plt.plot(xd, line, color=color, label=l)


plt.title("$F_N$ vs $F_kf$")
plt.xlabel(r"$F_N$ (N)")
plt.ylabel("$F_kf$ (N)")
plt.scatter(x1, y1, color="b")
plot(x1, y1, color="b")
plt.legend(loc="upper left")
plt.savefig("./Graphs/friction_2.png")
plt.show()
