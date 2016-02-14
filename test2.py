import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(-0.1, 1.1), ylim=(9, 21), xlabel='u')
ax.grid()


frameCount = 50
x = np.linspace(0, 1, frameCount);
y = np.add(np.multiply(x, 10), 10)

line, = ax.plot(x, y, lw=2)
dots, = ax.plot([], [], 'go', ms=20)

time_text = ax.text(0.02, 0.95, 'u = ', transform=ax.transAxes)

def init():
    dots.set_data([], [])
    return dots,
    
def animate(i):
    time_text.set_text('u = %.2f' % x[i])
    dots.set_data(x[i], y[i])
    return dots,

plt.tight_layout()

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frameCount, interval=100)
anim.save('basic_animation.gif', writer='imagemagick')
#plt.show()
