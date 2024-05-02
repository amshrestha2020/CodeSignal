# In an effort to be more innovative, your boss introduced a strange new tradition: the first day of every month you're allowed to work from home. You like this rule when the day falls on a Monday, because any excuse to skip rush hour traffic is great!

# You and your colleagues have started calling these months regular months. Since you're a fan of working from home, you decide to find out how far away the nearest regular month is, given that the currMonth has just started.

# For your convenience, here is a list of month lengths (from January to December, respectively):

# Month lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
# Please, note that in leap years February has 29 days.

# Example

# For currMonth = "02-2016", the output should be
# solution(currMonth) = "08-2016".

# February of 2016 year is regular, but it doesn't count since it has started already, so the next regular month is August of 2016 - which is the answer.


from datetime import datetime, timedelta

def solution(curr_month):
    month, year = map(int, curr_month.split("-"))

    # Increment the month by 1, and if it exceeds 12, increment the year by 1 and reset the month to 1
    month += 1
    if month > 12:
        month = 1
        year += 1

    # Create a date object for the first day of the next month
    date = datetime(year, month, 1)

    # Keep incrementing the month until the first day of the month is a Monday
    while date.weekday() != 0:
        date += timedelta(days=32)
        date = date.replace(day=1)

    # Return the date in the format mm-yyyy
    return date.strftime("%m-%Y")
