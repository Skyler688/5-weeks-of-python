import datetime as dt

now = dt.datetime.now()
print(now)
print("year:", now.year)
print("month:", now.month)
print("day:", now.day)
print("hour:", now.hour)
print("minute:", now.minute)
print("second:", now.second)
print("microsecond:", now.microsecond)
print("weekday:", now.weekday()) # monday = 0 / sunday = 6
print("isoweekday:", now.isoweekday()) # monday = 1 / sunday = 7

# you can create a date time object
my_date_obj = dt.datetime(year=2000, month=3, day=10) # if you do not pass the other peramiters it will default to 0
print("my date object:", my_date_obj)