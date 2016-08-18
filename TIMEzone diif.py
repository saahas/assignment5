import pytz
import datetime

eastern = timezone('US/Eastern')
utc = timezone('UTC')
datetime1 = utc.localize(datetime(2002, 10, 27, 18, 26, 23))
datetime2 = eastern.localize(datetime(2002, 10, 27, 14, 30, 00))
time_diff = (datetime2 - datetime1).total_seconds()
print(time_diff)