import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

t2 = [10.48, 11.03, 11.63, 12.45]
t1 = [[11.65, 11.91], [10.36, 10.73], [7.82, 8.29]]
t_avg = [(i[0] + i[1])/2 for i in t1]
t12 = []

x1 = [0.98, 1.47, 2.45]
y = [[8.089, 7.913], [9.097, 8.793], [12.054, 11.368]]
y1 = [(i[0] + i[1])/2 for i in y]


def func(x, a, c):
    return a * x ** 2 + c

def plot(x_data, y_data, color):
    i = [1, 1]
    t = curve_fit(func, x_data, y_data, i)
    print(t[0])
    xd = np.linspace(min(x_data), max(x_data), 100)
    line = [func(x, *t[0]) for x in xd]
    rounded = list(map(lambda x: round(x, 2), t[0]))
    l = "{}x^2 + {}".format(*rounded)
    plt.plot(xd, line, color=color, label=l)


plt.title("$F$ vs $v_t$")
plt.xlabel(r"$F$ (N)")
plt.ylabel("$v_t$ (m/s)")
plt.scatter(x1, y1, color="y")
plot(x1, y1, color="y")
plt.legend(loc="upper left")
plt.savefig("./Graphs/circle_1.png")
plt.show()


print(t_avg)
print()
