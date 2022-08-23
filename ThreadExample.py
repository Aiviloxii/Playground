# import modules
import _thread as thread
import time
# define function for the thread
def greet(threadName, delay):
    count = 1
    while count <= 5:
        time.sleep(delay)
        print(f"{count}-{threadName}  Welcome to Python Programming -- {time.ctime(time.time())}")
        count += 1
    print(f"End of thread {threadName}")
# create the thread
try:
    thread.start_new_thread(greet,("First", 2, ))
    thread.start_new_thread(greet, ("Second", 3))
except:
    print("Error, thread can not start")
# run thread
while 1:
    pass