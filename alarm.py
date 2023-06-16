
import winsound
import time
from time import strftime
from time import localtime
import datetime
while True:
    time = strftime("%H:%M", localtime())
    print(time)
    if time =='12:00':
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
        break
    else:
        time.sleep(1)
        continue

