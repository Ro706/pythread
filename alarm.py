
import winsound
from threading import Thread
from time import sleep 
from time import strftime
from time import localtime
import datetime
alarm = input("Enter a time :")
def times():
    while True:
        times = strftime("%H:%M", localtime())
        # print(times)
        if times ==alarm:
            winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
            break
        else:
            sleep(1)
            continue
def printf():
    n = 0
    while True:
        print('hello')
        sleep(1)
        n+=1
        if n == 100:
            print("Done")
            break
        else:
            continue
        
t1 = Thread(target=printf)
t1.start()
t2 = Thread(target=times)
t2.start()



