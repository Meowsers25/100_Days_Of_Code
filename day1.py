# Day 1 0f pyBites 100 days of code challenge

from datetime import datetime
from datetime import date

print(datetime.today()) # date and time
print(date.today()) # just date

today = datetime.today()
print(today)
print(type(today)) # today is a datetime object

today_date = date.today()
print(today_date)
print(type(today_date)) # today_date is a date object  

# can pick apart further
print(today_date.month)
print(today_date.day)  
print(today_date.year) 

print(today.hour)  
print(today.minute)
print(today.second)

christmas = date(2018, 12, 25) # assign date to variable
print(christmas)
print(christmas - today_date)

if christmas != today_date:
  print('There are ' + str((christmas - today_date).days) + ' days until Christmas.')
else:
  print('It\'s Christmas')

k_bday = date(2018, 10, 15)
print(k_bday)


# is not did not work for me, but != did
if k_bday != today_date:
  print('Awwwww, sorry.......')
else:
  print('Happy Birthday!!!!')