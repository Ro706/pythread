
import winsound
from threading import Thread
import time
from time import strftime
from time import localtime
import datetime

def times():
    while True:
        time = strftime("%H:%M", localtime())
        print(time)
        if time =='12:07':
            winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
            break
        else:
            time.sleep(1)
            continue
def printf():
    n = 0
    while True:
        print('hello')
        time.sleep(1)
        n+=1
        if n == 10:
            print("Done")
            break
        else:
            continue
        
t1 = Thread(target=printf)
t1.start()
t2 = Thread(target=times)
t2.start()

    

