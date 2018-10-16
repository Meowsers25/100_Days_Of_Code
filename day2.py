from datetime import datetime
from datetime import date
from datetime import timedelta

print(datetime.today())
print(date.today())

t = timedelta(days = 4, hours = 10)
print(t.days)


# This is Bite 67 Working with Datetimes

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)

def get_hundred_days_end_date():
  total_days = timedelta(days = 100)
  return str(start_100days + total_days)

print(get_hundred_days_end_date())

def get_days_between_pb_start_first_joint_pycon():
  return int((pycon_date - pybites_founded).days)

print(get_days_between_pb_start_first_joint_pycon())