import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

x1 = [0.95, 1.317, 1.742]
y1 = [1.548, 1.116, 0.844]


def plot(x_data, y_data, color):
    x = np.linspace(min(x_data), max(x_data), 100)
    f = interp1d(x_data, y_data, kind="quadratic")
    plt.plot(x, f(x), color=color, label="y = $0.68x^2-2.71x+3.51$")


plt.title("Total Mass vs Acceleration")
plt.xlabel("Total Mass (kg)")
plt.ylabel("Acceleration $(\\frac{m}{s^2})$")
plt.scatter(x1, y1, color="r")
plot(x1, y1,  color="r")
plt.legend(loc="upper right")
plt.savefig("mass.png")
plt.show()
