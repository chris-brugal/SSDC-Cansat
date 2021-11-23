from time import time
from tkinter import Scale
from typing import Sized
import PySimpleGUI as sg
import datetime
from datetime import date
import time

from time import gmtime, strftime

from PySimpleGUI.PySimpleGUI import Sizer
strftime("%Y-%m-%d %H:%M:%S", gmtime())
'2009-01-05 22:14:39'


def clock():
    while True:
        return date.today().strftime("%B %d, %Y") + " " + strftime("%H:%M:%S", gmtime())
        time.sleep(1)  #currently does not refresh


theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

# sg.theme_add_new('Dashboard', theme_dict)     # if using 4.20.0.1+
sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT_INSIDE = (10,10)
BPAD_RIGHT = ((10,20), (10, 20))

top_banner = [[sg.Text('Dashboard'+ ' '*120, font='Any 20', background_color=DARK_HEADER_COLOR),
               sg.Text(clock(), font='Any 20', background_color=DARK_HEADER_COLOR)]]

top  = [[sg.Text('Current Status?', size=(50,1), justification='c', pad=BPAD_TOP, font='Any 20')],
            [sg.T(f'{i*25}-{i*34}') for i in range(7)],]

block_2 = [[sg.Text('Altimeter', font='Any 20')],
            [sg.T('Current Altitude')],
            [sg.Image(filename='GUI\Altimeter_test.png')]  ] #picture to altimeter

block_3 = [[sg.Text('Block 3', font='Any 20')],
            [sg.Input(), sg.Text('Some Text')],
            [sg.Button('Send'), sg.Button('CLOSE')]  ] #does nothing

block_4 = [[sg.Text('Speedometer', font='Any 20')],
            [sg.T('Current Velocity')],
            [sg.Image(filename='GUI\speedometer_test.png')]  ] #picture to speedometer

block_5 = [[sg.Text('Block 5', font='Any 20')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')]]


layout = [[sg.Column(top_banner, size=(1920, 60), pad=(0,0), background_color=DARK_HEADER_COLOR,justification='c')],
          [sg.Column(top, size=(1800, 90), pad=BPAD_TOP)],

          [sg.Column([[sg.Column(block_2, size=(450,300), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_5, size=(450,150), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_3, size=(450,150),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
                    
                    sg.Column(block_4, size=(420, 420), pad=BPAD_RIGHT)]]


         # [sg.Column([[sg.Column(block_4, size=(450, 280), pad=BPAD_RIGHT_INSIDE)],
        #              [sg.Column(block_5, size=(450, 280), pad=BPAD_RIGHT_INSIDE)]], pad=BPAD_RIGHT, background_color=BORDER_COLOR)]]]


        

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), location=(0,0), background_color=BORDER_COLOR, no_titlebar=True, grab_anywhere=True).finalize()
window.maximize()

while True:             # Event Loop
    event, values = window.read()
    window.refresh() #still does nothing for some reason and clock does not change
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
window.close()
