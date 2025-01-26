# Program to find number of hours
# Between to Dates

from datetime import datetime
dateformat = "%Y-%m-%d %H:%M:%S"

d1 = datetime.strptime(input("Enter 1st date  in this format Full Year/month/day hour:minute:second"),dateformat)
d2 = datetime.strptime(input("Enter 1st date  in this format Full Year/month/day hour:minute:second" ),dateformat)

time_diff = d1 - d2

print(time_diff)