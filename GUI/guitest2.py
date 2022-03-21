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

brown = '#854803'
orange ='#f29411'

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
global PC1 
PC1 = 0
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

def getCanData():  # get data from canister csv file
    data = pd.read_csv('Flight_1063_C.csv')
    global PC1 
    PC1 = data['PACKET_COUNT'][PC1 + 1]
    print(PC1)
    PCC = data['PACKET_COUNT']
    ID = data['TEAM_ID'][PC1]
    MODE = data['MODE'][PC1]
    TP_DEPLOY = data['TP_RELEASED'][PC1]
    tPlus = data['T+ Time']
    alt = data['ALTITUDE']
    temp = data['TEMP']
    volt = data['VOLTAGE']
    gpsLAT = data['GPS_LATITUDE']
    gpsLONG = data['GPS_LONGITUDE']
    gpsALT = data['GPS_ALTITUDE']
    SS1 = data['SOFTWARE_STATE'][PC1]
    return (tPlus, alt, temp, volt, gpsLAT, gpsLONG, gpsALT)

def getPayloadData():
        data = pd.read_csv('Flight_5063_P.csv')
        tPlusP = data['T+ Time']
        altP = data['TP_ALTITUDE']
        tempP = data['TP_TEMP']
        voltP = data['TP_VOLTAGE']
        gyroR = data['GYRO_R']
        gyroP = data['GYRO_P']
        gyroY = data['GYRO_Y']
        accelR = data['ACCEL_R']
        accelP = data['ACCEL_P']
        accelY = data['ACCEL_Y']
        magR = data['MAG_R']
        magP = data['MAG_P']
        magY = data['MAG_Y']
        pe = data['POINTING_ERROR']
        return(tPlusP, altP, tempP, voltP, gyroR, gyroP, gyroY, accelR,
        accelP, accelY, magR, magP, magY, pe)

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

    canData = (getCanData)()
    win = 7                           #maximum window size
    imin = min(max(0, i - win), len(canData[0]) - win)      #gets current window range
    xdata = canData[0][imin:i]          #gets x values between range
    ydata = canData[1][imin:i]          #gets y values between range
    gyroData = canData[2][imin:i]
    tempData = canData[3][imin:i]
    lines[0].set_data(xdata, ydata)     #sets line
    #lines[1].set_data(xdata, gyroData)
    #lines[2].set_data(xdata, tempData)
    i = 0
    while (i < 10):
        _VARS['pltAxis'+str(i)].relim()                       #renumbers x axis
        _VARS['pltAxis'+str(i)].autoscale()   
                    #renumbers x axis
    return lines,

#x = 0
#while (x < 10):
#    anim = animation.FuncAnimation(_VARS['pltFig'+str(x)], animate, init_func=init, interval=1000)  #nees to be updated
#    x+=1

#plt.show()    #needs to be updated


# Recreate Synthetic data, clear existing figre and redraw plot.

#create clock to keep track of frame in order to update graph??
#use panda to trigger new update in csv file and send to graph to update??

def updateCanChart(start, end):   #THIS TAKES ALL DATA AND GRAPHS IT
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////
    #use t+ mission time instead of packet count since payload and canister are transmitting at different rates
    #so their graphs will will be moving faster/slower than the other????
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////

    canData = getCanData()
    canTPlus = canData[0][start:end]          #gets x values between range  THIS IS GETTING THE DATA AT PC1-7 to PC1 NOT THE ACTUAL VALUES
    canAlt = canData[1][start:end]          #gets y values between range
    canTemp = canData[2][start:end]
    canVolt = canData[3][start:end]
    gpsLat = canData[4][start:end]
    gpsLong = canData[5][start:end]
    gpsAlt = canData[6][start:end]


    _VARS['pltsubFig0'].plot(canTPlus, canAlt, '-k')

    _VARS['pltsubFig1'].plot(canTPlus, canTemp, '-k')

    _VARS['pltsubFig2'].plot(canTPlus, canVolt, '-k')

    _VARS['pltsubFig5'].plot(canTPlus, gpsLat, '-k')

    _VARS['pltsubFig6'].plot(canTPlus, gpsLong, '-k')

    _VARS['pltsubFig7'].plot(canTPlus, gpsAlt, '-k')

    i = 0
    while (i < 10):
        _VARS['pltAxis'+str(i)].relim()                       #renumbers x axis
        _VARS['pltAxis'+str(i)].autoscale()
        i+=1

def updatePayloadChart(start, end):   #THIS TAKES ALL DATA AND GRAPHS IT

    payloadData = getPayloadData()

    payTPlus = payloadData[0][start:end]
    payAlt = payloadData[1][start:end]
    payTemp = payloadData[2][start:end]
    payVolt = payloadData[3][start:end]
    gyroR = payloadData[4][start:end] 
    gyroP = payloadData[5][start:end] 
    gyroY = payloadData[6][start:end] 
    accelR = payloadData[7][start:end] 
    accelP = payloadData[8][start:end] 
    accelY = payloadData[9][start:end] 
    magR = payloadData[10][start:end] 
    magP = payloadData[11][start:end] 
    magY = payloadData[12][start:end] 
    pe = payloadData[13][start:end] 

    _VARS['pltsubFig0'].plot(payTPlus, payAlt, '-r')

    _VARS['pltsubFig1'].plot(payTPlus, payTemp, '-r')

    _VARS['pltsubFig2'].plot(payTPlus, payVolt, '-r')

    _VARS['pltsubFig3'].plot(payTPlus, gyroR, orange)
    _VARS['pltsubFig3'].plot(payTPlus, gyroP, '-m')
    _VARS['pltsubFig3'].plot(payTPlus, gyroY, brown)

    _VARS['pltsubFig4'].plot(payTPlus, accelR, orange)
    _VARS['pltsubFig4'].plot(payTPlus, accelP, '-m')
    _VARS['pltsubFig4'].plot(payTPlus, accelY, brown)

    _VARS['pltsubFig8'].plot(payTPlus, magR, orange)
    _VARS['pltsubFig8'].plot(payTPlus, magP, '-m')
    _VARS['pltsubFig8'].plot(payTPlus, magY, brown)

    _VARS['pltAxis9'].plot(payTPlus, pe, '-r')


# \\  -------- PYPLOT -------- //


_VARS['window'].maximize()

updateCanChart(0,7)
updatePayloadChart(0,7)
time.sleep(1)
updateCanChart(1,8)
updatePayloadChart(1,8)

while True:
    event, values = _VARS['window'].read(timeout=10)
    _VARS['window']['time'].update(clock())
    _VARS['window']['gpsTime'].update('GPS Time: ' + clock())


    if event in (None, 'Close'):
        break

_VARS['window'].close()