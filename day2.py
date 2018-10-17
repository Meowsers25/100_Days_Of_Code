from datetime import datetime
from datetime import date
from datetime import timedelta
import os
import urllib.request
import time

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

# Bite 7 Parsing dates from logs

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()
# print(loglines)
for line in loglines:
  if line.startswith('ERROR'):
    new_date = line[6:25]
    damn = new_date.replace('T', ' ')
    date = datetime.strptime(damn, '%Y-%m-%d %H:%M:%S')
    print(type(date))
    print(date)
  elif line.startswith('WARNING'):
    new_date = line[8:27]
    damn = new_date.replace('T', ' ')
    date = datetime.strptime(damn, '%Y-%m-%d %H:%M:%S')
    print(type(date))
    print(date)
  else:
    new_date = line[5:24]
    damn = new_date.replace('T', ' ')
    date = datetime.strptime(damn, '%Y-%m-%d %H:%M:%S')
    print(type(date))
    print(date)


# # for you to code:

# def convert_to_datetime(line):
#     '''TODO 1:
#        Given a log line extract its timestamp and convert it to a datetime object. 
#        For example calling the function with:
#        INFO 2014-07-03T23:27:51 supybot Shutdown complete.
#        returns:
#        datetime(2014, 7, 3, 23, 27, 51)'''
#     pass


# def time_between_shutdowns(loglines):
#     '''TODO 2:
#        Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
#        timedelta between the first and last one. 
#        Return this datetime.timedelta object.'''
#     pass