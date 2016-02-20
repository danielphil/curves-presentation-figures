import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import helpers

f, ax = plt.subplots(1, 1, figsize=(5, 4))

p0 = (6, 6)
p1 = (9, 7)
t0 = (0, 10)
t1 = (3, 15)

ax.set_xlim((0, 12))
ax.set_ylim((0, 12))

frameCount = 360

t1_line_x = [p1[0], p1[0] + t1[0]]
t1_line_y = [p1[1], p1[1] + t1[1]]
t1_line, = ax.plot(t1_line_x, t1_line_y)
t0_line, = ax.plot([], [], lw=1)
line, = ax.plot([], [], lw=3)

lengths = np.concatenate((np.linspace(2.5, 5, frameCount / 2), np.linspace(5, 2.5, frameCount / 2)))

def init():
    line.set_data([], [])
    t0_line.set_data([], [])
    return line, t0_line
    
def animate(i):
    angle = np.pi / 180 * i;
    length = lengths[i]
    t0 = (length * np.cos(angle), length * np.sin(angle))
    x, y = helpers.getHermiteCurve(p0, p1, t0, t1, 100)
    line.set_data(x, y)
    
    t0_x = np.asarray([p0[0], p0[0] + t0[0]])
    t0_y = np.asarray([p0[1], p0[1] + t0[1]])
    t0_line.set_data(t0_x, t0_y)
    
    return line, t0_line

plt.tight_layout()

anim = animation.FuncAnimation(f, animate, init_func=init, frames=frameCount, interval=20)
anim.save('output/hermite_tangents.gif', writer='imagemagick')
