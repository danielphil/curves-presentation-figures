import numpy as np
import matplotlib.pyplot as plt

f, ax = plt.subplots(1, 1, figsize=(5, 4))

x = np.linspace(0, 10, 1000)
y = np.power(x, 2)
ax.plot(x, y)
ax.set_xlim((1, 5))
ax.set_ylim((0, 30))
ax.set_xlabel('my x label')
ax.set_ylabel('my y label')
ax.set_title('plot title goes here')

plt.tight_layout()
plt.savefig('output/labelled_plot.png', dpi=150, transparent=True)