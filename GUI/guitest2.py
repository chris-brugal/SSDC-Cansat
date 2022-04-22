from asyncio.windows_events import NULL
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
import math

from pylab import *


brown = '#854803'
orange ='#f29411'

_VARS = {'window': False,
         'fig_agg0': False,
         'fig_agg1': False,
         'fig_agg2': False,
         'fig_agg3': False,
         'fig_agg4': False,
         'fig_agg5': False,
         'fig_agg6': False,
         'fig_agg7': False,
         'fig_agg8': False,
         'fig_agg9': False,

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


ID = 1063
PT1 = 'C'
PT2 = 'P'
SS1 = 'LAUNCH_AWAITING'
SS2 = 'LAUNCH_AWAITING'
PC1 = 0
PC2 = 0
MODE = 'S'
TP_DEPLOY = 'F'
CMD_ECHO = 'OFF'
GPS_SAT = 0


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

second_row = [[sg.Text('Packet Type 1: '+ PT1, size=(14), font='Any 16', background_color='#1B2838', key = 'PT1'),
               sg.Text('Mode: '+MODE, size=(7), font='Any 16', background_color='#1B2838', key = 'Mode'),
               sg.Text('GPS Time: ' + clock(), size=(18), font='Any 16', background_color='#1B2838', key='gpsTime'),
               sg.Text('Software State 1: '+SS1, size=(32), font='Any 16', background_color='#1B2838', key = 'SS1'),
               sg.Text('Packet Type 2: ' + PT2, size=(14), font='Any 16', background_color='#1B2838', key = 'PT2'),
               sg.Text('Software State 2: '+SS2, size=(32), font='Any 16', background_color='#1B2838', key = 'SS2')]]

third_row = [[sg.Text('Packet Count 1: '+str(PC1), size=(17), font='Any 16', background_color='#1B2838', key = 'PC1'),
               sg.Text('TP Deploy: '+TP_DEPLOY, size=(11), font='Any 16', background_color='#1B2838', key = 'TPD'),
               sg.Text('GPS Sat: ', size=(13), font='Any 16', background_color='#1B2838', key = 'GPS_SAT'),
               sg.Text('CMD Echo: '+CMD_ECHO, size=(31), font='Any 16', background_color='#1B2838', key = 'CMD_ECH'),
               sg.Text('Packet Count 2: '+str(PC2), size=(18), font='Any 16', background_color='#1B2838', key = 'PC2')]]

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

    global PC1
    global MODE
    global TP_DEPLOY
    global SS1
    global ID
    global CMD_ECHO
    global PT1
    global GPS_SAT

    if (PC1 > 7):
            data = pd.read_csv('liveDemo.csv', header=None, names=["TEAM_ID", "MISSION_TIME", "T+ Time", "PACKET_COUNT", 
        "PACKET_TYPE", "MODE", "TP_RELEASED", "ALTITUDE", "TEMP", "VOLTAGE", "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", 
        "GPS_ALTITUDE", "GPS_SATS", "SOFTWARE_STATE", "CMD_ECHO"], skiprows = PC1-6)
    else:
        data = pd.read_csv('liveDemo.csv')
    

    PC1 = data['PACKET_COUNT'][len(data)-1]
    #print(PC1)
    #print(data)

    tPlus = data['T+ Time']
    alt = data['ALTITUDE']
    temp = data['TEMP']
    volt = data['VOLTAGE']
    gpsLAT = data['GPS_LATITUDE']
    gpsLONG = data['GPS_LONGITUDE']
    gpsALT = data['GPS_ALTITUDE']

    GPS_SAT = data['GPS_SATS'][len(data)-1]
    ID = data['TEAM_ID'][len(data)-1]
    MODE = data['MODE'][len(data)-1]
    TP_DEPLOY = data['TP_RELEASED'][len(data)-1]
    SS1 = data['SOFTWARE_STATE'][len(data)-1]
    PT1 = data['PACKET_TYPE'][len(data)-1]
    CMD_ECHO = data['CMD_ECHO'][len(data)-1]

    _VARS['window']['PC1'].update('Packet Count 1: ' + str(PC1))
    _VARS['window']['Mode'].update('Mode: ' + MODE)
    _VARS['window']['TPD'].update('TP Deploy: ' + str(TP_DEPLOY))
    _VARS['window']['SS1'].update('Software State 1: ' + SS1)
    _VARS['window']['PT1'].update('Packet Type 1: ' + PT1)
    _VARS['window']['CMD_ECH'].update('CMD Echo: ' + CMD_ECHO)
    _VARS['window']['GPS_SAT'].update('GPS Sat: ' + str(GPS_SAT))

    return (tPlus, alt, temp, volt, gpsLAT, gpsLONG, gpsALT)

def getPayloadData():

        global PC2
        global PT2
        global SS2

        if (PC2 > 28):
            data = pd.read_csv('liveDemo.csv', header=None, names=["TEAM_ID", "MISSION_TIME", "T+ Time", "PACKET_COUNT", 
        "PACKET_TYPE", "MODE", "TP_RELEASED", "ALTITUDE", "TEMP", "VOLTAGE", "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", 
        "GPS_ALTITUDE", "GPS_SATS", "SOFTWARE_STATE", "CMD_ECHO"], skiprows = PC2-24)
        else:
            data = pd.read_csv('liveDemo2.csv')

        PC2 = data['PACKET_COUNT'][len(data)-1]

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

        SS2 = data['TP_SOFTWARE_STATE'][len(data)-1]
        PT2 = data['PACKET_TYPE'][len(data)-1]

        _VARS['window']['PC2'].update('Packet Count 2: ' + str(PC2))
        _VARS['window']['SS2'].update('Software State 2: ' + SS2)
        _VARS['window']['PT2'].update('Packet Type 2: ' + PT2)

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

    _VARS['pltAxis0'].set_xlabel('Time')
    _VARS['pltAxis1'].set_xlabel('Time')
    _VARS['pltAxis2'].set_xlabel('Time')
    _VARS['pltAxis3'].set_xlabel('Time')
    _VARS['pltAxis4'].set_xlabel('Time')
    _VARS['pltAxis5'].set_xlabel('Time')
    _VARS['pltAxis6'].set_xlabel('Time')
    _VARS['pltAxis7'].set_xlabel('Time')
    _VARS['pltAxis8'].set_xlabel('Time')
    _VARS['pltAxis9'].set_xlabel('Time')

def drawChart(graph):  # graph is the graph number set as an integer  THIS CREATES THE GRAPHS AND DRAWS THEM BLANK
    _VARS['pltFig'+str(graph)] = plt.figure()
    _VARS['pltsubFig'+str(graph)] = plt.subplot()
    _VARS['pltAxis'+str(graph)] = plt.subplot()
    if (graph == 9):
        setyAxis()
    _VARS['pltAxis'+str(graph)].margins(0.05)  
    _VARS['pltFig'+str(graph)].set_size_inches(3.5,3.5)
    _VARS['fig_agg'+str(graph)] = draw_figure(
        _VARS['window']['figCanvas'+str(graph)].TKCanvas, _VARS['pltFig'+str(graph)])

i=0
while (i < 10):
    drawChart(i)
    i+= 1


# Recreate Synthetic data, clear existing figre and redraw plot.

#create clock to keep track of frame in order to update graph??
#use panda to trigger new update in csv file and send to graph to update??

def updateCanChart():   #THIS TAKES ALL DATA AND GRAPHS IT

    canData = getCanData()

    canTPlus = canData[0]       #gets x values between range  THIS IS GETTING THE DATA AT PC1-7 to PC1 NOT THE ACTUAL VALUES
    canAlt = canData[1]          #gets y values between range
    canTemp = canData[2]
    canVolt = canData[3]
    gpsLat = canData[4]
    gpsLong = canData[5]
    gpsAlt = canData[6]

    _VARS['pltsubFig0'].plot(canTPlus, canAlt, '-k')

    _VARS['pltsubFig1'].plot(canTPlus, canTemp, '-k')

    _VARS['pltsubFig2'].plot(canTPlus, canVolt, '-k')

    _VARS['pltsubFig5'].plot(canTPlus, gpsLat, '-k')

    _VARS['pltsubFig6'].plot(canTPlus, gpsLong, '-k')

    _VARS['pltsubFig7'].plot(canTPlus, gpsAlt, '-k')

    _VARS['fig_agg0'].draw()
    _VARS['fig_agg1'].draw()
    _VARS['fig_agg2'].draw()
    _VARS['fig_agg5'].draw()
    _VARS['fig_agg6'].draw()
    _VARS['fig_agg7'].draw()

    

def updatePayloadChart():   #THIS TAKES ALL DATA AND GRAPHS IT

    payloadData = getPayloadData()

    payTPlus = payloadData[0]
    payAlt = payloadData[1]
    payTemp = payloadData[2]
    payVolt = payloadData[3]
    gyroR = payloadData[4]
    gyroP = payloadData[5]
    gyroY = payloadData[6]
    accelR = payloadData[7]
    accelP = payloadData[8]
    accelY = payloadData[9]
    magR = payloadData[10]
    magP = payloadData[11]
    magY = payloadData[12]
    pe = payloadData[13]

    _VARS['pltsubFig0'].cla()
    _VARS['pltsubFig1'].cla()
    _VARS['pltsubFig2'].cla()
    _VARS['pltsubFig3'].cla()
    _VARS['pltsubFig4'].cla()
    _VARS['pltsubFig5'].cla()
    _VARS['pltsubFig6'].cla()
    _VARS['pltsubFig7'].cla()
    _VARS['pltsubFig8'].cla()
    _VARS['pltsubFig9'].cla()


    updateCanChart()

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

    _VARS['pltsubFig9'].plot(payTPlus, pe, '-r')

    setyAxis()

    _VARS['fig_agg0'].draw()
    _VARS['fig_agg1'].draw()
    _VARS['fig_agg2'].draw()
    _VARS['fig_agg3'].draw()
    _VARS['fig_agg4'].draw()
    _VARS['fig_agg5'].draw()
    _VARS['fig_agg6'].draw()
    _VARS['fig_agg7'].draw()
    _VARS['fig_agg8'].draw()
    _VARS['fig_agg9'].draw()


# \\  -------- PYPLOT -------- //


_VARS['window'].maximize()

#updatePayloadChart(0)
i=0

canFileLength = 0          #initializing values
payloadFileLength = 0      #initializing values

while True:
    event, values = _VARS['window'].read(timeout=10)
    if event in (None, 'Close'):
        break

    _VARS['window']['time'].update(clock())
    _VARS['window']['gpsTime'].update('GPS Time: ' + clock())

    data = pd.read_csv('liveDemo.csv', usecols = ["PACKET_COUNT"])       #checks to see if line has been added to canister csv file
    if (len(data) >  canFileLength):
        canFileLength = len(data)
        updateCanChart()
        #update can chart here or update payload since it should do both?


    #data = pd.read_csv('liveDemo2.csv', usecols = ["PACKET_COUNT"])     #checks to see if line has been added to payload csv fle
    #if (len(data) >  payloadFileLength):
    #    payloadFileLength = len(data)
    #    updatePayloadChart()


    #updateCanChart(i,i+7)
    #updatePayloadChart(i)                              #not necessary once length checkers are working
    i+=1

_VARS['window'].close()

#https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms