#!/usr/bin/env python

import sys
import datetime
from time import strptime

if len(sys.argv) != 2 :
    print(len(sys.argv))
    print("Usage : "+sys.argv[0]+" "+"<time-stamp>")
    print("Example :"+sys.argv[0]+" "+"Wed Aug 05 12:53:20 IST 2020")
    sys.exit()
mydate=sys.argv[1]
def date_differance(mydate):
    time1=sys.argv[1]
    time=time1.split(" ")

    time[1]=str(strptime(time[1],'%b').tm_mon).zfill(2)
    d1=time[2]+":"+time[1]+":"+time[5]

    d1=datetime.datetime.strptime(d1,'%d:%m:%Y')
    d2=(datetime.datetime.now()).strftime('%d:%m:%Y')
    d2=datetime.datetime.strptime(d2,'%d:%m:%Y')

    return ((d2-d1).days)
days=date_differance(mydate)
print(days)







