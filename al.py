
import winsound
from threading import Thread
from time import sleep 
from time import strftime
from time import localtime
import datetime

def times():
    alarm=input("Enter the alarm time:")
    while True:
        times = strftime("%H:%M", localtime())
        # print(times)
        if alarm == times:
            winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
            break
        else:
            sleep(1)
            continue
times()