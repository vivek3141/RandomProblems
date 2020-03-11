import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x1 = [2.19, 4.85, 6.67, 8.97]
y1 = [0.071, 0.122, 0.172, 0.216]


plt.scatter(x1, y1)
data = curve_fit(lambda x, a, b: a * x + b, x1, y1, [1,1])
x_data = np.linspace(min(x1), max(x1))
y_data = [ data[0][0] * i + data[0][1] for i in x_data]
print(data[0])

plt.title("Object #1")
plt.plot(x_data, y_data, label=f"{round(data[0][0], 4)}x + {round(data[0][1], 4)}")
plt.legend(loc="upper left")
plt.ylabel(r"$\tau_{s} \ (N \cdot m)$")
plt.xlabel(r"$\alpha \ (m/s^2)$")
plt.show()


