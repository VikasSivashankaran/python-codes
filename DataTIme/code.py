import datetime
 
# Get current date and time
now = datetime.datetime.now()
 
# Get date from now
date = now.date()
 
# Get time from now
time = now.time()
 
# Get datetime from now
datetime_now = now.date()
 
# Find difference between two datetimes
difference = datetime.datetime.now() - datetime.datetime(2017, 7, 1)

print("difference - ", difference)
 
# Create a timezone aware datetime
tz_aware_datetime = datetime.datetime(2017, 7, 1, tzinfo=datetime.timezone.utc)

print("tz_aware_datetime - ", tz_aware_datetime)
