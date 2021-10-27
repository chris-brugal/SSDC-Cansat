from time import time
import PySimpleGUI as sg
from datetime import date

from time import gmtime, strftime
strftime("%Y-%m-%d %H:%M:%S", gmtime())
'2009-01-05 22:14:39'


"""
    Dashboard using blocks of information.

    Copyright 2020 PySimpleGUI.org
"""


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

top_banner = [[sg.Text('Dashboard'+ ' '*45, font='Any 20', background_color=DARK_HEADER_COLOR),
               sg.Text(date.today().strftime("%B %d, %Y") + " " + strftime("%H:%M:%S", gmtime()), font='Any 20', background_color=DARK_HEADER_COLOR)]]

top  = [[sg.Text('Current Status?', size=(50,1), justification='c', pad=BPAD_TOP, font='Any 20')],
            [sg.T(f'{i*25}-{i*34}') for i in range(7)],]

block_2 = [[sg.Text('Altimeter', font='Any 20')],
            [sg.T('Current Altitude')],
            [sg.Image(r'C:\Users\maxep\OneDrive\Documents\Cansat Files\altimeter_test.png')]  ] #picture to altimeter

block_3 = [[sg.Text('Block 3', font='Any 20')],
            [sg.Input(), sg.Text('Some Text')],
            [sg.Button('Send'), sg.Button('Exit')]  ] #does nothing

block_4 = [[sg.Text('Speedometer', font='Any 20')],
            [sg.T('Current Velocity')],
            [sg.Image(r'C:\Users\maxep\OneDrive\Documents\Cansat Files\speedometer_test.png')]  ] #picture to speedometer

block_5 = [[sg.Text('Block 5', font='Any 20')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')]]


layout = [[sg.Column(top_banner, size=(1020, 60), pad=(0,0), background_color=DARK_HEADER_COLOR)],
          [sg.Column(top, size=(980, 90), pad=BPAD_TOP)],

          [sg.Column([[sg.Column(block_2, size=(450,320), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_5, size=(450,200), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_3, size=(450,200),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
                    
                    sg.Column(block_4, size=(420, 420), pad=BPAD_RIGHT)]]


         # [sg.Column([[sg.Column(block_4, size=(450, 280), pad=BPAD_RIGHT_INSIDE)],
        #              [sg.Column(block_5, size=(450, 280), pad=BPAD_RIGHT_INSIDE)]], pad=BPAD_RIGHT, background_color=BORDER_COLOR)]]]


        

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, grab_anywhere=True)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()
