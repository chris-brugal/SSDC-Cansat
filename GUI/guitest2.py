import PySimpleGUI as sg
import time

def clock():
    return (time.strftime("%H:%M:%S", time.gmtime()))

top_banner = [[sg.Text('gSat ID: 1063', font='Any 26', background_color='#1B2838', border_width=(5), size=(40)),
               sg.Text(clock(), font='Any 22', background_color='#1B2838', key='time', border_width=(8), size=(10)),
               sg.Button('Calibrate', font='Any 16'),
               sg.Button('Connect', font='Any 16'),
               sg.Button('Close', font='Any 16')]]

second_row = [[sg.Text('Packet Type 1: C', size=(14), font='Any 16', background_color='#1B2838'),
               sg.Text('Mode: F', size=(7), font='Any 16', background_color='#1B2838'),
               sg.Text('GPS Time: ' + clock(), size=(18), font='Any 16', background_color='#1B2838', key='gpsTime'),
               sg.Text('Software State 1: LAUNCH_AWAITING ', size=(32), font='Any 16', background_color='#1B2838'),
               sg.Text('Packet Type 2: P', size=(14), font='Any 16', background_color='#1B2838'),
               sg.Text('Software State 2: LAUNCH_AWAITING ', size=(32), font='Any 16', background_color='#1B2838')]]

third_row = [[sg.Text('Packet Count 1: 1510', size=(17), font='Any 16', background_color='#1B2838'),
               sg.Text('Tp Deploy: F', size=(10), font='Any 16', background_color='#1B2838'),
               sg.Text('GPS Sat: 105', size=(13), font='Any 16', background_color='#1B2838'),
               sg.Text('CMD Echo: CMD,1000,ST,13:35:59', size=(31), font='Any 16', background_color='#1B2838'),
               sg.Text('Packet Count 2: 1698', size=(18), font='Any 16', background_color='#1B2838')]]

layout = [[top_banner],
          [second_row],
          [third_row],
          [sg.Text('Graph')],
          [sg.Text('Graph')],
          [sg.Text('command box')]]

window = sg.Window('test window', layout, margins=(0,0), location=(0,0), finalize=True)

window.maximize()

while True:
    event, values = window.read(timeout=10)
    window['time'].update(clock())
    window['gpsTime'].update('GPS Time: ' + clock())
    if event in (None, 'Close'):
        break

window.close()