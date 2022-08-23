# Create a simple thread program to create a countdown from an number entered.
#import modules
import _thread as trd
import time
#define function for the thread.
def countDown(delay):
    count = int(input(f"Enter Duration: "))
    print("******Countdown starts********")
    while count:
        time.sleep(delay)
        print(f"{count}")
        count -=1
    print("Time Up!!")
# create the thread.
try:
    trd.start_new_thread(countDown, (1, ))
except:
    print("Thread can not be started")
#run the thread.
while 1:
    pass