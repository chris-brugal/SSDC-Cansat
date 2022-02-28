import csv
import string
import time
import random
import pandas as pd

TEAM_ID = "1063" #this is the final and correct team id
PACKET_TYPE = 67
PACKET_TYPE2 = 80

file = open('Flight_'+TEAM_ID+'_'+chr(PACKET_TYPE)+'.csv', 'w', newline='')
writer = csv.writer(file)

writer.writerow(["TEAM_ID","MISSION_TIME", "PACKET_COUNT","PACKET_TYPE","MODE", "TP_RELEASED", "ALTITUDE", 
"TEMP", "VOLTAGE", "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", "GPS_ALTITUDE", "GPS_SATS", 
"SOFTWARE_STATE", "CMD_ECHO"])

file.close()

i = 0
while i < 1000:

    i+=1

    with open('Flight_1063_C.csv', 'a', newline='') as file:
       # with open('Flight_'+TEAM_ID+'_'+chr(PACKET_TYPE2)+'.csv', 'w', newline='') as file2:
        
        writer = csv.writer(file)
       # writer2 = csv.writer(file2)

        #writer.writerow(["TEAM_ID", "MISSION_TIME", "PACKET_COUNT", "PACKET_TYPE", "MODE", "TP_RELEASED", "ALTITUDE", "TEMP", "VOLTAGE", "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", "GPS_ALTITUDE", "GPS_STATS", "SOFTWARE_STATE", "CMD_ECHO"])
        #writer2.writerow(["TEAM_ID", "MISSION_TIME", "PACKET_COUNT", "PACKET_TYPE", "TP_ALTITUDE", "TP_TEMP", "TP_VOLTAGE", "GYRO_R", "GYRO_P", "GYRO_Y", "ACCEL_R", "ACCEL_P", "ACCEL_Y", "MAG_R", "MAG_P", "MAG_Y", "POINTING_ERROR", "TP_SOFTWARE_STATE"])
        rand = random.randint(0,100)
        rand2 = random.randint(0,100)
        rand3 = random.randint(0,100)
        rand4 = random.randint(0,100)
        rand5 = random.randint(0,100)
        rand6 = random.randint(0,100)
        rand7 = random.randint(0,100)
        writer.writerow([1063,time.strftime("%H:%M:%S", time.localtime()) ,i/2, 'C', 'F', 'R', rand, rand2, rand3, time.strftime("%H:%M:%S", time.localtime()),
        rand4, rand5, rand6, rand7, 'Decent', 'CXON'])
        print (i)

    time.sleep(.01)