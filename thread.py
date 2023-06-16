import time 
from threading import Thread

def do_this():
    print('do this')
    time.sleep(2)
    print('done')
def do_that():
    print('do that')
    time.sleep(3)
    print('done')
    
t1 = Thread(target=do_this)
t1.start()
t2=Thread(target=do_that)
t2.start()