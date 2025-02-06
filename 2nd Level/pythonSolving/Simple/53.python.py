# Get an Age from the user
# Covert Age in to Second, minutes, and hours

age = int(input("Enter an Age: "))

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
second_in_minutes = 60

age_in_hours = age * days_in_year * hours_in_day
age_in_minutes = age_in_hours * minutes_in_hour
age_in_second = age_in_minutes * second_in_minutes

print(f"your age in hour is: {age_in_hours}")
print(f"your age in minutes is: {age_in_minutes}")
print(f"your age in second is: {age_in_second}")