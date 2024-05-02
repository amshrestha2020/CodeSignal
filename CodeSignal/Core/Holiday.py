# John Doe likes holidays very much, and he was very happy to hear that his country's government decided to introduce yet another one. He heard that the new holiday will be celebrated each year on the xth week of month, on weekDay.

# Your task is to return the day of month on which the holiday will be celebrated in the year yearNumber.

# For your convenience, here are the lists of months names and lengths and the list of days of the week names.

# Months: "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December".
# Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
# Days of the week: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday".
# Please, note that in leap years February has 29 days.

# Example

# For x = 3, weekDay = "Wednesday", month = "November", and yearNumber = 2016, the output should be
# solution(x, weekDay, month, yearNumber) = 16.

# The new holiday will be celebrated every November on the 3rd Wednesday of the month. In 2016 the 3rd Wednesday falls on the 16th of November.

# For x = 5, weekDay = "Thursday", month = "November", and yearNumber = 2016, the output should be
# solution(x, weekDay, month, yearNumber) = -1.

# There are only 4 Thursdays in November 2016.


from datetime import datetime, timedelta

def solution(x, week_day, month, year_number):
    # Mapping of week days and months to help with the datetime object creation
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Get the weekday and month as integer values
    week_day_num = week_days.index(week_day)
    month_num = months.index(month) + 1

    # Start at the first day of the month
    current_date = datetime(year_number, month_num, 1)

    # Find the first weekday of the month
    while current_date.weekday() != week_day_num:
        current_date += timedelta(days=1)

    # Skip to the xth occurrence of the weekday
    current_date += timedelta(weeks=x-1)

    # If we've moved onto the next month, return -1
    if current_date.month != month_num:
        return -1

    # Otherwise, return the day of the month
    return current_date.day
