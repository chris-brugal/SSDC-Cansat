from asyncio.windows_events import NULL
import csv
import string
import time
import random
import pandas as pd
from datetime import datetime, timedelta
import math

TEAM_ID = "1063" #this is the final and correct team id
PAYLOAD_ID = "5063"  #payload id should be team id + 5000
PACKET_TYPE = 67
PACKET_TYPE2 = 80
startTime = NULL

file = open('liveDemo.csv', 'w', newline='')

writer = csv.writer(file)

writer.writerow(["TEAM_ID","MISSION_TIME", "T+ Time", "PACKET_COUNT","PACKET_TYPE","MODE", "TP_RELEASED", "ALTITUDE", 
"TEMP", "VOLTAGE", "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", "GPS_ALTITUDE", "GPS_SATS", 
"SOFTWARE_STATE", "CMD_ECHO"])


file.close()


i = 0
while i < 600:

    i+=1

    with open('liveDemo.csv', 'a', newline='') as file:
        
            writer = csv.writer(file)

            rand = random.randint(0,100)
            rand2 = random.randint(0,100)
            rand3 = random.randint(0,100)
            rand4 = random.randint(0,100)
            rand5 = random.randint(0,100)
            rand6 = random.randint(0,100)
            rand7 = random.randint(0,100)
            if (i == 1):
                startTime = datetime.now()
            writer.writerow([TEAM_ID,datetime.now().strftime("%H:%M:%S") , str(math.floor((datetime.now()-startTime).total_seconds())) ,i, 'C', 'F', 'R', rand, rand2, rand3, time.strftime("%H:%M:%S", time.localtime()),
            rand4, rand5, rand6, rand7, 'Decent', 'CXON'])

    time.sleep(1)