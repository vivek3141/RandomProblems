import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np

x1 = [0.00, 4.48, 8.96, 13.44, 17.92, 22.41, 26.89, 31.37, 35.85, 40.33, 44.81]
y1 = [0.00, 2.89, 5.14, 6.74, 7.71, 8.03, 7.71, 6.74, 5.14, 2.89, 0.00]
x2 = [0.00, 2.10, 4.21, 6.31, 8.41, 10.52, 12.62, 14.72, 16.82, 18.93, 21.03]
y2 = [0.00, 0.58, 1.04, 1.36, 1.56, 1.62, 1.56, 1.36, 1.04, 0.58, 0.00]
x3 = [0.00, 3.84, 7.68, 11.52, 15.36, 19.20, 23.04, 26.88, 30.72, 34.56, 38.40]
y3 = [0.00, 3.07, 5.46, 7.17, 8.20, 8.54, 8.20, 7.17, 5.46, 3.07, 0.00]


def plot(x1, y1, color, label):
    x = np.linspace(min(x1), max(x1), 300)
    power_smooth = spline(x1, y1, x)
    plt.plot(x, power_smooth, color=color, label=label)


plt.title("Trajectory of Projectiles")
plt.xlabel("Horizontal Distance")
plt.ylabel("Vertical Distance")
plt.scatter(x1, y1, color="b")
plt.scatter(x2, y2, color="r")
plt.scatter(x3, y3, color="g")
plot(x1, y1, color="b", label="Kahn")
plot(x2, y2, color="r", label="Starr")
plot(x3, y3, color="g", label="Tharun")
plt.legend(loc="upper right")
plt.scatter([0], [0], color="black")
plt.savefig("./Graphs/trajec.png")
plt.show()
