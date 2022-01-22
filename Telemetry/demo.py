import csv
import string
import time
import random

TEAM_ID = "1063" #this is the final and correct team id
PACKET_TYPE = 67
PACKET_TYPE2 = 80


with open('Flight_'+TEAM_ID+'_'+chr(PACKET_TYPE)+'.csv', 'w', newline='') as file:
    with open('Flight_'+TEAM_ID+'_'+chr(PACKET_TYPE2)+'.csv', 'w', newline='') as file2:

        writer = csv.writer(file)
        writer2 = csv.writer(file2)

        #writer.writerow(["TEAM_ID", "MISSION_TIME", "PACKET_COUNT", "PACKET_TYPE", "MODE", "TP_RELEASED", "ALTITUDE", "TEMP", "VOLTAGE", "GPS_TIME", "GPS_LATITUDE", "GPS_LONGITUDE", "GPS_ALTITUDE", "GPS_STATS", "SOFTWARE_STATE", "CMD_ECHO"])
        writer2.writerow(["TEAM_ID", "MISSION_TIME", "PACKET_COUNT", "PACKET_TYPE", "TP_ALTITUDE", "TP_TEMP", "TP_VOLTAGE", "GYRO_R", "GYRO_P", "GYRO_Y", "ACCEL_R", "ACCEL_P", "ACCEL_Y", "MAG_R", "MAG_P", "MAG_Y", "POINTING_ERROR", "TP_SOFTWARE_STATE"])
        writer.writerow(["Time", "Count", "Altitude"])

        for i in range(1000):
            rand = random.randint(1,1000)
            writer.writerow([time.strftime("%H:%M:%S", time.localtime()),i ,rand])
            #time.sleep(0.1)

       # writer.writerow([time.strftime("%H:%M:%S", time.localtime()), 0, 0])
        #time.sleep(1)
        #writer.writerow([time.strftime("%H:%M:%S", time.localtime()), 0, 0])
        #time.sleep(1)
        #writer.writerow([time.strftime("%H:%M:%S", time.localtime()), 0, 0])