import PySimpleGUI as sg
import time
import os
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure 
from matplotlib import animation
import matplotlib as mpl
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np



_VARS = {'window': False,
         'fig_agg': False,
         'pltFig0': False,
         'pltFig1': False,
         'pltFig2': False,
         'pltFig3': False,
         'pltFig4': False,
         'pltFig5': False,
         'pltFig6': False,
         'pltFig7': False,
         'pltFig8': False,
         'pltFig9': False,

         'pltsubFig0': False,
         'pltsubFig1': False,
         'pltsubFig2': False,
         'pltsubFig3': False,
         'pltsubFig4': False,
         'pltsubFig5': False,           #Needed????
         'pltsubFig6': False,
         'pltsubFig7': False,
         'pltsubFig8': False,
         'pltsubFig9': False,

         'pltAxis0': False,
         'pltAxis1': False,
         'pltAxis2': False,
         'pltAxis3': False,
         'pltAxis4': False,
         'pltAxis5': False,
         'pltAxis6': False,
         'pltAxis7': False,
         'pltAxis8': False,
         'pltAxis9': False}

# Helper Functions

ID = 1063
PT1 = 'C'
PT2 = 'P'
SS1 = 'LAUNCH_AWAITING'
SS2 = 'LAUNCH_AWAITING'
PC1 = 500
PC2 = 1687
MODE = 'S'
TP_DEPLOY = 'F'
CMD_ECHO = 'CMD,1000,ST,13:35:59'

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


directory = format(os.getcwd())

def clock():
    return (time.strftime("%H:%M:%S", time.gmtime()))

top_banner = [[sg.Text('gSat ID: '+str(ID), font='Any 26', background_color='#1B2838', border_width=(5), size=(40)),
               sg.Text(clock(), font='Any 22', background_color='#1B2838', key='time', border_width=(8), size=(10)),
               sg.Button('Calibrate', font='Any 16'),
               sg.Button('Connect', font='Any 16'),
               sg.Button('Close', font='Any 16')]]

second_row = [[sg.Text('Packet Type 1: '+ PT1, size=(14), font='Any 16', background_color='#1B2838'),
               sg.Text('Mode: '+MODE, size=(7), font='Any 16', background_color='#1B2838'),
               sg.Text('GPS Time: ' + clock(), size=(18), font='Any 16', background_color='#1B2838', key='gpsTime'),
               sg.Text('Software State 1: '+SS1, size=(32), font='Any 16', background_color='#1B2838'),
               sg.Text('Packet Type 2: ' + PT2, size=(14), font='Any 16', background_color='#1B2838'),
               sg.Text('Software State 2: '+SS2, size=(32), font='Any 16', background_color='#1B2838')]]

third_row = [[sg.Text('Packet Count 1: '+str(PC1), size=(17), font='Any 16', background_color='#1B2838'),
               sg.Text('TP Deploy: '+TP_DEPLOY, size=(11), font='Any 16', background_color='#1B2838'),
               sg.Text('GPS Sat: 105', size=(13), font='Any 16', background_color='#1B2838'),
               sg.Text('CMD Echo: '+CMD_ECHO, size=(31), font='Any 16', background_color='#1B2838'),
               sg.Text('Packet Count 2: '+str(PC2), size=(18), font='Any 16', background_color='#1B2838')]]

fourth_row = [[sg.Canvas(key='figCanvas0'),
               sg.Canvas(key='figCanvas1'),
               sg.Canvas(key='figCanvas2'),
               sg.Canvas(key='figCanvas3'),
               sg.Canvas(key='figCanvas4'),]]

fifth_row = [[sg.Canvas(key='figCanvas5'),
              sg.Canvas(key='figCanvas6'),
              sg.Canvas(key='figCanvas7'),
              sg.Canvas(key='figCanvas8'),
              sg.Canvas(key='figCanvas9'),]]

sixth_row = [[sg.Text('CMD', size=(8), font = 'Any 26', background_color='#1B2838'),
              sg.Input(size=(30)),
              sg.Button('Send',size=(18), font='Any 16'),
              sg.Text(' '*100),
              sg.Image(directory+'/GUI/images/Legend1.png')]]


layout = [[top_banner],
          [second_row],
          [third_row],
          [fourth_row],  #this is the graphs
          [fifth_row],   #this is also 5 graphs
          [sixth_row]]

_VARS['window'] = sg.Window('test window', layout, margins=(0,0), location=(0,0), finalize=True)

#<TEAM_ID>,< MISSION_TIME>, <PACKET_COUNT>,<PACKET_TYPE>,<MODE>, <TP_RELEASED>, <ALTITUDE>, 
# <TEMP>, <VOLTAGE>, < GPS_TIME>, <GPS_LATITUDE>, <GPS_LONGITUDE>, <GPS_ALTITUDE>, <GPS_SATS>, 
# <SOFTWARE_STATE>, <CMD_ECHO>

def getData():  # get data from canister csv file
    data = pd.read_csv('Flight_1063_C.csv')
    global PC1 
    PC1 +=1
    PCC = data['PACKET_COUNT']
    ID = data['TEAM_ID'][PC1]
    MODE = data['MODE'][PC1]
    TP_DEPLOY = data['TP_RELEASED'][PC1]
    alt = data['ALTITUDE']
    temp = data['TEMP']
    volt = data['VOLTAGE']
    gpsLAT = data['GPS_LATITUDE']
    gpsLONG = data['GPS_LONGITUDE']
    gpsALT = data['GPS_ALTITUDE']
    SS1 = data['SOFTWARE_STATE'][PC1]
    return (PCC, alt, temp, volt, gpsLAT, gpsLONG, gpsALT)

def setyAxis():      #only done once in drawchart function to set axies
    _VARS['pltAxis0'].set_ylabel('Altitude')
    _VARS['pltAxis1'].set_ylabel('Temperature')
    _VARS['pltAxis2'].set_ylabel('Voltage')
    _VARS['pltAxis3'].set_ylabel('Gyro')
    _VARS['pltAxis4'].set_ylabel('Acceleration')
    _VARS['pltAxis5'].set_ylabel('GPS LAT')
    _VARS['pltAxis6'].set_ylabel('GPS LONG')
    _VARS['pltAxis7'].set_ylabel('GPS ALT')
    _VARS['pltAxis8'].set_ylabel('MAG')
    _VARS['pltAxis9'].set_ylabel('PE')
    
    _VARS['pltAxis0'].set_title('Altitude (m) vs Time(s)')
    _VARS['pltAxis1'].set_title('Temp (c) vs Time(s)')
    _VARS['pltAxis2'].set_title('Voltage volts) vs Time(s)')
    _VARS['pltAxis3'].set_title('Gyro (deg) vs Time(s)')
    _VARS['pltAxis4'].set_title('Accel (m/s) vs Time(s)')
    _VARS['pltAxis5'].set_title('GPS LAT (deg) vs Time(s)')
    _VARS['pltAxis6'].set_title('GPS LONG (deg) vs Time(s)')
    _VARS['pltAxis7'].set_title('GPS ALT (deg) vs Time(s)')
    _VARS['pltAxis8'].set_title('Mag (gaus) vs Time(s)')
    _VARS['pltAxis9'].set_title('Pointing Error (deg) vs Time (s)')

def drawChart(graph):  # graph is the graph number set as an integer  THIS CREATES THE GRAPHS AND DRAWS THEM BLANK
    _VARS['pltFig'+str(graph)] = plt.figure()
    _VARS['pltsubFig'+str(graph)] = plt.subplot()
    _VARS['pltAxis'+str(graph)] = plt.subplot()
    if (graph == 9):
        setyAxis()
    _VARS['pltAxis'+str(graph)].set_xlabel('Time')
    _VARS['pltAxis'+str(graph)].margins(0.05)  
    _VARS['pltFig'+str(graph)].set_size_inches(3,3)
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'+str(graph)].TKCanvas, _VARS['pltFig'+str(graph)])

i=0
while (i < 10):
    drawChart(i)
    i+= 1

plotlays, plotcols = [1], ["blue","red", "brown"]

i = 0
lines = []
while (i < 1):
    for index in range(1):
       lobj = _VARS['pltAxis'+str(i)].plot([],[],lw=2,color=plotcols[index])[0]
       lines.append(lobj)
    i+=1


def init():                              #set first point
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):                       #draws line

    dataXY = (getData)()
    win = 7                           #maximum window size
    imin = min(max(0, i - win), len(dataXY[0]) - win)      #gets current window range
    xdata = dataXY[0][imin:i]          #gets x values between range
    ydata = dataXY[1][imin:i]          #gets y values between range
    gyroData = dataXY[2][imin:i]
    tempData = dataXY[3][imin:i]
    lines[0].set_data(xdata, ydata)     #sets line
    #lines[1].set_data(xdata, gyroData)
    #lines[2].set_data(xdata, tempData)
    i = 0
    while (i < 10):
        _VARS['pltAxis'+str(i)].relim()                       #renumbers x axis
        _VARS['pltAxis'+str(i)].autoscale()   
                    #renumbers x axis
    return lines,



# Recreate Synthetic data, clear existing figre and redraw plot.

#create clock to keep track of frame in order to update graph??
#use panda to trigger new update in csv file and send to graph to update??

def updateChart():   #THIS TAKES ALL DATA AND GRAPHS IT
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////
    #use t+ mission time instead of packet count since payload and canister are transmitting at different rates
    #so their graphs will will be moving faster/slower than the other????
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////

    data = getData()

    win = 7                           #maximum window size
    imin = min(max(0, PC1 - win), len(data[0]) - win)      #gets current window range
    #this needs to get the data where pc1-7 to pc is located
    pc = data[0][PC1-7:PC1]          #gets x values between range  THIS IS GETTING THE DATA AT PC1-7 to PC1 NOT THE ACTUAL VALUES
    alt = data[1][PC1-7:PC1]          #gets y values between range
    temp = data[2][PC1-7:PC1]

    x = 0
    while (x < 10):
        _VARS['pltsubFig'+str(x)].plot(pc, alt, '-k')
        _VARS['pltsubFig'+str(x)].plot(pc, temp, '-b')
        x+=1
    i = 0
    while (i < 10):
        _VARS['pltAxis'+str(i)].relim()                       #renumbers x axis
        _VARS['pltAxis'+str(i)].autoscale()
        i+=1

# \\  -------- PYPLOT -------- //


_VARS['window'].maximize()

updateChart()

while True:
    event, values = _VARS['window'].read(timeout=10)
    _VARS['window']['time'].update(clock())
    _VARS['window']['gpsTime'].update('GPS Time: ' + clock())

    if event in (None, 'Close'):
        break

_VARS['window'].close()