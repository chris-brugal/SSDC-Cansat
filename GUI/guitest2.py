import PySimpleGUI as sg
import time

import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure 
from matplotlib import animation
import matplotlib as mpl
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np



_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False}

# Helper Functions


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


ID = 1063
PT1 = 'C'
PT2 = 'P'
SS1 = 'LAUNCH_AWAITING'
SS2 = 'LAUNCH_AWAITING'
PC1 = 1584
PC2 = 1687
MODE = 'S'
TP_DEPLOY = 'F'
CMD_ECHO = 'CMD,1000,ST,13:35:59'

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

layout = [[top_banner],
          [second_row],
          [third_row],
          [sg.Canvas(key='figCanvas')],
          [sg.Text('Graph')],
          [sg.Text('command box')]]

_VARS['window'] = sg.Window('test window', layout, margins=(0,0), location=(0,0), finalize=True)


def getData():
    data = pd.read_csv('Flight_1063_C.csv')
    xArray = data['Count']
    yArray = data['Altitude']
    gyro = data['Gyro']
    temp = data['Temp']
    return (xArray, yArray)



def drawChart():
    _VARS['pltFig'] = plt.figure()
    dataXY = (getData)()
    plt.plot(dataXY[0], dataXY[1], '-k')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])


# Recreate Synthetic data, clear existing figre and redraw plot.

def updateChart():
    _VARS['fig_agg'].get_tk_widget().forget()
    dataXY = makeSynthData()
    # plt.cla()
    plt.clf()
    plt.plot(dataXY[0], dataXY[1], '.k')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

# \\  -------- PYPLOT -------- //


drawChart()




_VARS['window'].maximize()

while True:
    event, values = _VARS['window'].read(timeout=10)
    _VARS['window']['time'].update(clock())
    _VARS['window']['gpsTime'].update('GPS Time: ' + clock())
    if event in (None, 'Close'):
        break

_VARS['window'].close()