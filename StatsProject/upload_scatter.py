from data import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np




def func(x, a, b):
    return (x * a) + b

def plot(info, x_data, y_data, color):
    i = [1, 1]
    t = curve_fit(func, x_data, y_data, i)
    residuals = np.array(y_data) - (func(np.array(x_data), *t[0]))
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((np.array(y_data)-np.mean(np.array(y_data)))**2)
    r2 = (1 - (ss_res / ss_tot)) * 100
    r_squared = round(r2, 2)

    print(t[0])
    xd = np.linspace(min(x_data), max(x_data), 100)
    line = [func(x, *t[0]) for x in xd]
    rounded = list(map(lambda x: round(x, 1), t[0]))
    l = "{}; {}x+ {}; R^2 = {}%".format(info, *rounded, r_squared)
    plt.scatter(x_data, y_data, color=color)
    plt.plot(xd, line, color=color, label=l)

plt.title("Number of People vs Download Speed")
plt.xlabel(r"Number of People")
plt.ylabel("Download Speed (Mbps)")
plot("Phone 1", x, d1, color="r")
plot("Phone 2", x, d2, color="g")
plot("Phone 4", x, d4, color="b")
plt.legend(loc="upper left")
plt.show()