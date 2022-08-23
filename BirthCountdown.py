# Write a program that returns the number of days remaining to a particular birthday selected.
import datetime as dt
by = int(input("Enter your birth Year:[e.g 2000] "))
bm = int(input("Enter your birth Month: [e.g 12] "))
bd = int(input("Enter your birth Day: [e.g 12 ]"))
birthday = dt.date(by, bm, bd)
tday=dt.date.today()
curBday = dt.date(tday.year,bm, bd)
if curBday > tday:
    day = curBday - tday
    print(f"You have {day} to your birthday")
elif curBday < tday:
    print("You have celebrated your birthday already")
else:
    curBday = tday
    print("Today is your birthday, Congratulations!!")
