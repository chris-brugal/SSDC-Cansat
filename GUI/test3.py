import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import csv

yArray = [[0]]
xArray = [[0]]
i=0

with open('Flight_1063_C.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if (i > 0):
            print (row[1])
            yArray.append([row[2]])
            xArray.append([row[1]])
        i+=1


fig, axis = plt.subplots()
line, = axis.plot([], [], '-ko')   #customize line (color, dots, etc)
axis.margins(0.05)                  #makes it more fluid

def init():                              #set first point
    line.set_data(xArray[:2],yArray[:2])
    return line,

def animate(i):                         #draws line
    win = 100                           #maximum window size
    imin = min(max(0, i - win), len(xArray) - win)      #gets current window range
    xdata = xArray[imin:i]          #gets x values between range
    ydata = yArray[imin:i]          #gets y values between range
    line.set_data(xdata, ydata)     #sets line
    axis.relim()                       #renumbers x axis
    axis.autoscale()                   #renumbers x axis
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=25)

plt.show()


#https://stackoverflow.com/questions/31922016/creating-a-live-plot-of-csv-data-with-matplotlib