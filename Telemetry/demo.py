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

file = open('Flight_'+TEAM_ID+'_'+chr(PACKET_TYPE)+'.csv', 'w', newline='')
file2 = open('Flight_'+PAYLOAD_ID+'_'+chr(PACKET_TYPE2)+'.csv', 'w', newline='')

writer = csv.writer(file)
writer2 = csv.writer(file2)

writer.writerow(["TEAM_ID","MISSION_TIME", "T+ Time", "PACKET_COUNT","PACKET_TYPE","MODE", "TP_RELEASED", "ALTITUDE", 
"TEMP", "VOLTAGE", "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", "GPS_ALTITUDE", "GPS_SATS", 
"SOFTWARE_STATE", "CMD_ECHO"])

writer2.writerow(["PAYLOAD_ID", "MISSION_TIME", "T+ Time", "PACKET_COUNT", "PACKET_TYPE", "TP_ALTITUDE", "TP_TEMP", 
"TP_VOLTAGE", "GYRO_R", "GYRO_P", "GYRO_Y", "ACCEL_R", "ACCEL_P", "ACCEL_Y", "MAG_R", "MAG_P", "MAG_Y", 
"POINTING_ERROR", "TP_SOFTWARE_STATE"])

file.close()
file2.close()


i = 0
while i < 600:

    i+=1

    with open('Flight_1063_C.csv', 'a', newline='') as file:
       with open('Flight_'+PAYLOAD_ID+'_'+chr(PACKET_TYPE2)+'.csv', 'a', newline='') as file2:
        
            writer = csv.writer(file)
            writer2 = csv.writer(file2)

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


            writer2.writerow([PAYLOAD_ID,datetime.now().strftime("%H:%M:%S") ,  str(math.floor((datetime.now()-startTime).total_seconds())) ,4*i-3, 'C', rand7, rand5, rand, rand2, rand3, rand5,
            rand4, rand5, rand6, rand7, rand2, rand, rand4, 'Decent'])

            writer2.writerow([PAYLOAD_ID,datetime.now().strftime("%H:%M:%S") ,  str(math.floor((datetime.now()-startTime).total_seconds())+0.25) ,4*i-2, 'C', rand7, rand5, rand, rand2, rand3, rand5,
            rand4, rand5, rand6, rand7, rand2, rand, rand4, 'Decent'])

            writer2.writerow([PAYLOAD_ID,datetime.now().strftime("%H:%M:%S") ,  str(math.floor((datetime.now()-startTime).total_seconds())+0.5) ,4*i-1, 'C', rand7, rand5, rand, rand2, rand3, rand5,
            rand4, rand5, rand6, rand7, rand2, rand, rand4, 'Decent'])

            writer2.writerow([PAYLOAD_ID,datetime.now().strftime("%H:%M:%S") ,  str(math.floor((datetime.now()-startTime).total_seconds())+0.75) ,4*i, 'C', rand7, rand5, rand, rand2, rand3, rand5,
            rand4, rand5, rand6, rand7, rand2, rand, rand4, 'Decent'])
            print (i)

    time.sleep(1)