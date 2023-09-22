import time
import datetime

start_date = datetime.datetime.strptime("9/23/23", "%m/%d/%y")
end_date = start_date + datetime.timedelta(days=7)
friday_in_milliseconds = int(round(end_date.timestamp() * 1000))
print(milliseconds)
