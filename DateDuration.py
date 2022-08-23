# Write a python program to return the duration of two dates given.
import datetime as dt
y1 = int(input("Enter the first year: "))
m1 = int(input("Enter the first month: "))
d1 = int(input("Enter the first day: "))
y2 = int(input("Enter the second year: "))
m2 = int(input("Enter the second month:"))
d2 = int(input("Enter the second day: "))
day1 = dt.date(y1, m1,d1)
day2 = dt.date(y2, m2, d2)
if day2 > day1:
    duration = day2 - day1
    print(f"{day2} is {duration}  ahead of {day1}")
elif day1 > day2:
    duration = day1 - day2
    print(f"{day1} is {duration}  after  {day2}")
else:
    day1=day2
    print("Both are the same day")