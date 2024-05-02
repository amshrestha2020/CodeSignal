# Your Math teacher takes education very seriously, and hates it when a class is missed or canceled for any reason. He even made up the following rule: if a class is missed because of a holiday, the teacher will compensate for it with a makeup class after school.

# You're given an array, daysOfTheWeek, with the weekdays on which your teacher's classes are scheduled, and holidays, representing the dates of the holidays throughout the academic year (from 1st of September in year to 31st of May in year + 1). How many times will you be forced to stay after school for a makeup class because of holiday conflicts in the current academic year?

# For your convenience, here is the list of month lengths (from January to December, respectively):

# Month lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
# Please note that in leap years February has 29 days.

# Example

# For year = 2015, daysOfTheWeek = [2, 3], and
# holidays = ["11-04", "02-22", "02-23", "03-07", "03-08", "05-09"],
# the output should be
# solution(year, daysOfTheWeek, holidays) = 3.

# November 4th of 2015 is a Wednesday, February 23th of 2016 and March 8th of 2016 are Tuesdays, and the other holidays fall on Mondays. Classes are scheduled on Wednesdays and Tuesdays, so there will be only 3 missed classes.


from datetime import datetime, timedelta

def solution(year, days_of_the_week, holidays):
    result = 0
    holidays_end_date = datetime.strptime(f"{year}-09-01", "%Y-%m-%d")
    holidays_start_date = datetime.strptime(f"{year}-05-31", "%Y-%m-%d")

    for holiday in holidays:
        cur_date = datetime.strptime(f"{year}-{holiday}", "%Y-%m-%d")
        if holidays_start_date < cur_date < holidays_end_date:
            continue

        if cur_date < holidays_start_date:
            cur_date = cur_date.replace(year=year + 1)

        day_of_the_week = cur_date.weekday() + 1  # In Python, Monday is 0 and Sunday is 6
        if day_of_the_week in days_of_the_week:
            result += 1

    return result

