import sys
import re

def init():
    if(len(sys.argv) != 4 ):
        print("Please run script as : python "+ sys.argv[0]+"<start-time-stamp> <end-time-stamp> <service-name>")
        print("Example : python "+sys.argv[0]+"30/May/2019:00:59:06"+"30/May/2019:09:59:06"+"<service-name>")
        sys.exit(1)
    start_date=sys.argv[1]
    end_date=sys.argv[2]
    print(start_date)
    print(end_date)
    return start_date,end_date
def time_split(start_date,end_date):
    my_start_ts = start_date
    my_end_ts = end_date
    start_date_lst = re.split(':|/', my_start_ts)
    end_date_lst = re.split(':|/', my_end_ts)
    start_hour = int(start_date_lst[3])
    start_min = int(start_date_lst[4])
    end_hour = int(end_date_lst[3])
    end_min = int(end_date_lst[4])
    return start_hour,start_min,end_hour,end_min

def time_loop(start_hour,start_min,end_hour,end_min):
    totat_start_minutes=start_hour*60+start_min
    total_end_minutes=end_hour*60+end_min
    time_stamp=[""]
    for min in range(totat_start_minutes,total_end_minutes+1):
        time_stamp_hour=str('{:02}'.format(int(min/60)))
        time_stamp_min=str('{:02}'.format(min%60))
        #print(str(time_stamp_hour)+":"+str(time_stamp_min))
        temp=str(time_stamp_hour)+":"+str(time_stamp_min)
        time_stamp.append(str(temp))
    return time_stamp
start_date,end_date=init()
start_hour,start_min,end_hour,end_min=time_split(start_date,end_date)
time_stamp=time_loop(start_hour,start_min,end_hour,end_min)