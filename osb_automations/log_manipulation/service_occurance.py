from datetime import date
from datetime import timedelta
import datetime

import time
date1="30/May/2019:23:59:06"
print(date1)
type(date1)
print(timedelta(days=365, hours=8, minutes=15))
dt = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
dt = time.mktime(dt)
print(time.strftime("%d %b %Y %H:%M:%S", time.gmtime(dt)))
struct_time = time.strptime(date1, "%d/%b/%Y:%H:%M:%S")
print(struct_time)

mydate=['30/May/2019:00:59:06','30/May/2019:09:59:06']
start_time=time.strptime(mydate[0],"%d/%b/%Y:%H:%M:%S")
end_time=time.strptime(mydate[1],"%d/%b/%Y:%H:%M:%S")
now=start_time

hour=datetime.timedelta(hours=1)
while(now<=end_time):
    print(now)

    now+=hour

print(start_time)
print(end_time)




