import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure 
from matplotlib import animation
import matplotlib as mpl
import pandas as pd
mpl.rcParams['toolbar'] = 'None'

yArray = []
xArray = []
i=0


fig, axis = plt.subplots()
fig.set_size_inches(3, 3)
axis.set_title('Pointing Error (deg) vs Time (s)')
axis.set_xlabel('Time')
axis.set_ylabel('Altitude')
axis.margins(0.05)                  #makes it more fluid

plotlays, plotcols = [1], ["blue","red", "brown"]
lines = []
for index in range(1):
    lobj = axis.plot([],[],lw=2,color=plotcols[index])[0]
    lines.append(lobj)


def init():                              #set first point
    for line in lines:
        line.set_data([],[])
    return lines


def animate(i):                         #draws line

    data = pd.read_csv('Flight_1063_C.csv')
    xArray = data['PACKET_COUNT']
    yArray = data['ALTITUDE']
    gyro = data['GPS_LONGITUDE']
    temp = data['TEMP']

    win = 7                           #maximum window size
    imin = min(max(0, i - win), len(xArray) - win)      #gets current window range
    xdata = xArray[imin:i]          #gets x values between range
    ydata = yArray[imin:i]          #gets y values between range
    gyroData = gyro[imin:i]
    tempData = temp[imin:i]
    lines[0].set_data(xdata, ydata)     #sets line
    #lines[1].set_data(xdata, gyroData)
    #lines[2].set_data(xdata, tempData)
    axis.relim()                       #renumbers x axis
    axis.autoscale()   
                    #renumbers x axis
    return lines,

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=1000)

plt.show()


#https://stackoverflow.com/questions/31922016/creating-a-live-plot-of-csv-data-with-matplotlib