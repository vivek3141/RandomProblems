import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x1 = [6.0466,
10.9466,
15.8466]
y1 = [1.274,
2.254,
3.332]
slope = (y1[0] - y1[2]) / (x1[0] - x1[2])


def func(x, a, b):
    return (x * a) + b


def plot(x_data, y_data, color):
    i = [1, 1]
    t = curve_fit(func, x_data, y_data, i)
    print(t[0])
    xd = np.linspace(min(x_data), max(x_data), 100)
    line = [func(x, *t[0]) for x in xd]
    rounded = list(map(lambda x: round(x, 2), t[0]))
    l = "{}x+ {}".format(*rounded)
    plt.plot(xd, line, color=color, label=l)


plt.title("$F_k$ vs $F_n$ for Wood + Tape")
plt.xlabel("$F_k$ (N)")
plt.ylabel("$F_n$ (N)")
plt.scatter(x1, y1, color="b")
plot(x1, y1, color="b")
plt.legend(loc="upper left")
plt.savefig("./force_1.png")
plt.show()
