import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.path import Path


points = np.array([[0, 0],
                   [1, 4],
                   [4, 4],
                   [4, 0],
                   [3, 0],
                   [3, 2],
                   [1, 2],
                   [1, 0],
                   [0, 0]])

x = points[:, 0]
y = points[:, 1]
plt.plot(x, y)
plt.grid(True)
plt.show()


fig_outline = Path(points)
x_min, x_max = np.min(x), np.max(x)
y_min, y_max = np.min(y), np.max(y)

fig_points = 0
n = 2000
for _ in range(n):
    x_rand = random.uniform(x_min, x_max)
    y_rand = random.uniform(y_min, y_max)

    if fig_outline.contains_point((x_rand, y_rand)):
        fig_points += 1

border_area = (x_max - x_min) * (y_max - y_min)
fig_area = (fig_points / n) * border_area
print(fig_area)
