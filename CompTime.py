# Write a program that compares two different time given
import time
import datetime as dt
print(time.ctime(time.time()))
timetuple= time.localtime(time.time())
print("The year is ",timetuple[0])
h =int(input("Enter the first hour : [e.g 2 0r 16]"))
m =int(input("Enter the minute: [e.g 35]"))
s =int(input("Enter the second: [e.g 54]"))
b = dt.time(h, m, s)
h1=int(input("Enter the hour to be compared: [e.g 4 or 23]"))
m1=int(input("Enter the minute to be compared: [e.g 15]"))
s1=int(input("Enter the second to be compared: [e.g 26]"))
c=dt.time(h1,m1,s1)
if c > b:
    print(f"{c} is ahead of {b} ")
elif b ==c:
    print("Both are the same")
else:
    print(f"{b} is ahead of {c} ")