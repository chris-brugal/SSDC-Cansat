import csv
import string
import time

TEAM_ID = "1000"
PACKET_TYPE = 67
PACKET_TYPE2 = 80


with open('Flight_'+TEAM_ID+'_'+chr(PACKET_TYPE)+'.csv', 'w', newline='') as file:
    with open('Flight_'+TEAM_ID+'_'+chr(PACKET_TYPE2)+'.csv', 'w', newline='') as file2:

        writer = csv.writer(file)
        writer2 = csv.writer(file2)

        writer.writerow(["TIME", "ALTITUDE", "Some other data"])

        writer.writerow([time.strftime("%H:%M:%S", time.localtime()), 0, 0])
        time.sleep(0.1)
        writer.writerow([time.strftime("%H:%M:%S", time.localtime()), 0, 0])
        time.sleep(3)
        writer.writerow([time.strftime("%H:%M:%S", time.localtime()), 0, 0])