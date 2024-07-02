import datetime

now=datetime.datetime.now()
print(now)

date=lambda x:x.date()
print(date(now))

month=lambda x:x.month
print(month(now))

year= lambda x:x.year
print(year(now))

t=lambda x:x.time()
print(t(now))