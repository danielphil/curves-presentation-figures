import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import helpers

f, ax = plt.subplots(1, 1, figsize=(5, 4))

p0 = (1, 1)
p1 = (4, 2)
t0 = (0, 10)
t1 = (3, 10)

x, y = helpers.getHermiteCurve(p0, p1, t0, t1, 10)

helpers.setGraphStyle(ax)
ax.plot(x, y, 'w')
ax.plot(x, y, 'co')
ax.set_xlim((0, 5))
ax.set_ylim((0, 5))

plt.tight_layout()
# facecolor='black' for a black background
plt.savefig('sequence_of_points.png', dpi=150, transparent=True)

f, ax = plt.subplots(1, 1, figsize=(5, 4))
helpers.setGraphStyle(ax)
x, y = helpers.getHermiteCurve(p0, p1, t0, t1, 100)

ax.plot(x, y, 'w')
ax.plot(x, y, 'co')
ax.set_xlim((0, 5))
ax.set_ylim((0, 5))

plt.tight_layout()
plt.savefig('sequence_of_points_100.png', dpi=150, transparent=True)