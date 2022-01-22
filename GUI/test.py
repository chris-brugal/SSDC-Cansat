import PySimpleGUI as sg
import math

from matplotlib import use as use_agg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import PySimpleGUI as sg

# Use Tkinter Agg
use_agg('TkAgg')

# PySimplGUI window
layout = [[sg.Graph((640, 480), (0, 0), (640, 480), key='Graph')]]
window = sg.Window('Matplotlib', layout, finalize=True)

# Default settings for matplotlib graphics
fig, ax = plt.subplots()

# Link matplotlib to PySimpleGUI Graph
canvas = FigureCanvasTkAgg(fig, window['Graph'].Widget)
plot_widget = canvas.get_tk_widget()
plot_widget.grid(row=0, column=0)

theta = 0   # offset angle for each sine curve
while True:

    event, values = window.read(timeout=10)

    if event == sg.WINDOW_CLOSED:
        break

    # Generate points for sine curve.
    x = [degree for degree in range(1080)]
    y = [math.sin((degree+theta)/180*math.pi) for degree in range(1080)]

    # Reset ax
    ax.cla()
    ax.set_title("Sensor Data")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_xscale('log')
    ax.grid()

    plt.plot(x, y)      # Plot new curve
    fig.canvas.draw()   # Draw curve really

    theta = (theta + 10) % 360  # change offset angle for curve shift on Graph

window.close()