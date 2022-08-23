# Write a python program that understands your timetable.
# It checks if your class is ongoing or if not, states time left till the next class.
import time as t
import datetime as dt
timetuple=t.asctime(t.localtime(t.time()))
print(timetuple)
ttp=t.localtime(t.time())
#print(ttp)
mon =ttp[6]==0 and ttp[3]==12 and ttp[4]==0 and ttp[5]==0
tue=ttp[6]==1 and ttp[3]==9 and ttp[4]==0 and ttp[5]==0
wed=ttp[6]==2 and ttp[3]==12 and ttp[4]==0 and ttp[5]==0
dDay =dt.datetime.today()
if timetuple == mon and timetuple < ttp[6]==0 and ttp[3]==14 and ttp[4]==0 and ttp[5]==0:
    print(f"Your Monday class is ongoing")

elif timetuple == tue and timetuple < ttp[6]==1 and ttp[3]==11 and ttp[4]==0 and ttp[5]==0:
    print(f"Your Tuesday class is ongoing")
elif timetuple == wed and timetuple < ttp[6]==0 and ttp[3]==12 and ttp[4]==0 and ttp[5]==0:
    print(f"Your Wednesday class is ongoing")
