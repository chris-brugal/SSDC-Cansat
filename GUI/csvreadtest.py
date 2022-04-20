from asyncio.windows_events import NULL
import csv
import string
import time
import random
import pandas as pd
from datetime import datetime, timedelta
import math
import pandas as pd

fileLength = 0

while True:
    data = pd.read_csv('liveDemo.csv')
    if (len(data) >  fileLength):
        fileLength = len(data)
        Packetcount = data['PACKET_COUNT'][fileLength-1]
        #print (data)
        print (Packetcount)
    
    time.sleep(.5)



#formula is length-1 = last index 
#header is not counted as a row so the first row of values is counted as index