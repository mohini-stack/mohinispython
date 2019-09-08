import sys
print(len(sys.argv))
if(len(sys.argv) != 4 ):
    print("Please run script as : python "+ sys.argv[0]+"<start-time-stamp> <end-time-stamp> <service-name>")
    print("Example : python "+sys.argv[0]+"30/May/2019:00:59:06"+"30/May/2019:09:59:06"+"<service-name>")
    sys.exit(1)
start_date=sys.argv[1]
end_date=sys.argv[2]
print(start_date)
print(end_date)