# Whenever you decide to celebrate your birthday you always do this your favorite café, which is quite popular and as such usually very crowded. This year you got lucky: when you and your friend enter the café you're surprised to see that it's almost empty. The waiter lets slip that there are always very few people on this day of the week.

# You enjoyed having the café all to yourself, and are now curious about the next time you'll be this lucky. Given the current birthdayDate, determine the number of years until it will fall on the same day of the week.

# For your convenience, here is the list of months lengths (from January to December, respectively):

# Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
# Please, note that in leap years February has 29 days. If your birthday is on the 29th of February, you celebrate it once in four years. Otherwise you birthday is celebrated each year.

# Example

# For birthdayDate = "02-01-2016", the output should be
# solution(birthdayDate) = 5.

# February 1 in 2016 is a Monday. The next year in which this same date will be Monday too is 2021. 2021 - 2016 = 5, which is the answer.


from datetime import datetime

def solution(birthday_date):
    # Parse the birthday date
    birthday = datetime.strptime(birthday_date, '%m-%d-%Y')
    
    # Get the day of the week for the birthday
    birthday_weekday = birthday.weekday()
    
    # Find the next year where the same date falls on the same day of the week
    current_year = birthday.year
    next_year = current_year
    while True:
        next_year += 1
        try:
            next_birthday = datetime(next_year, birthday.month, birthday.day)
            if next_birthday.weekday() == birthday_weekday:
                break
        except ValueError:
            # This handles the case when the birthday is on Feb 29 and the next year is not a leap year
            continue
    
    # Calculate the number of years until the same day of the week
    num_years = next_year - current_year
    
    return num_years

# Test cases
print(solution("02-01-2016"))  # Output: 5
