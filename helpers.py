import math
import numpy as np

def hermite(p0, p1, t0, t1, u):
    u2 = math.pow(u, 2)
    u3 = math.pow(u, 3)
    
    return (2 * u3 - 3 * u2 + 1) * p0 + (-2 * u3 + 3 * u2) * p1 + (u3 - 2 * u2 + u) * t0 + (u3 - u2) * t1

def getHermiteCurve(p0, p1, t0, t1, steps):
    u = np.linspace(0, 1, steps)
    x = np.vectorize(lambda u: hermite(p0[0], p1[0], t0[0], t1[0], u))(u)
    y = np.vectorize(lambda u: hermite(p0[1], p1[1], t0[1], t1[1], u))(u)
    return x, y
    
def setGraphStyle(ax):
    ax.spines['bottom'].set_color('#ffffff')
    ax.spines['top'].set_color('#ffffff') 
    ax.spines['right'].set_color('#ffffff')
    ax.spines['left'].set_color('#ffffff')
    
    ax.tick_params(axis='x', colors='#ffffff')
    ax.tick_params(axis='y', colors='#ffffff')
    ax.set_axis_bgcolor('black')
    
    ax.yaxis.label.set_color('#ffffff')
    ax.xaxis.label.set_color('#ffffff')
    
    ax.title.set_color('#ffffff')