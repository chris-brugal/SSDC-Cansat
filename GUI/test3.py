import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

y = np.random.normal(0, 1, 1000000).cumsum(axis=0)
x = np.arange(y.size) + 1

fig, ax = plt.subplots()
line, = ax.plot([], [], 'k-')
ax.margins(0.05)

def init():
    line.set_data(x[:2],y[:2])
    return line,

def animate(i):
    win = 300
    imin = min(max(0, i - win), x.size - win)
    xdata = x[imin:i]
    ydata = y[imin:i]
    line.set_data(xdata, ydata)
    ax.relim()
    ax.autoscale()
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=25)

plt.show()


#https://stackoverflow.com/questions/31922016/creating-a-live-plot-of-csv-data-with-matplotlib