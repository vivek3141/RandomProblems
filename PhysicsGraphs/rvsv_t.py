import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x1 = [0.7, 0.8, 0.9, 1.0]
y1 = [8.39, 9.114, 9.724, 10.09]

def func(x, a, b):
    return a * x + b

def plot(x_data, y_data, color):
    i = [1, 1]
    t = curve_fit(func, x_data, y_data, i)
    print(t[0])
    xd = np.linspace(min(x_data), max(x_data), 100)
    line = [func(x, *t[0]) for x in xd]
    rounded = list(map(lambda x: round(x, 2), t[0]))
    l = "{}x + {}".format(*rounded)
    plt.plot(xd, line, color=color, label=l)


plt.title("$r$ vs $v_t$")
plt.xlabel(r"$F$ (N)")
plt.ylabel("$v_t$ (m/s)")
plt.scatter(x1, y1, color="r")
plot(x1, y1, color="r")
plt.legend(loc="upper left")
plt.savefig("./Graphs/circle_2.png")
plt.show()
