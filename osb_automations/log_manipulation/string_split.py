import re

my_start_ts="30/May/2019:00:59:06"
my_end_ts="30/May/2019:00:59:06"
start_date_lst=re.split(':|/',my_start_ts)
end_date_lst=re.split(':|/',my_end_ts)
start_hour=start_date_lst[3]
start_min=start_date_lst[4]
start_sec=start_date_lst[5]
end_hour=end_date_lst[3]
end_min=end_date_lst[4]
end_sec=end_date_lst[5]
