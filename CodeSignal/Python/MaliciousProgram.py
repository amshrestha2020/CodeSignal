# You decided to create a malicious program to play a joke on your friend. He's now struggling with a report for his work, and you want to scare him by spoiling some dates in it (of course you will change them back after you have your moment of joy). However, you don't want him to discover the errors until he starts double-checking the report, so all spoiled dates should be valid.

# Now your goal is to write a program that modifies the curDate according to the rules that specify the changes that should be made. However, if the changes result in an incorrect date, the program should leave the date as is.

# Given the changes and the curDate, return the spoiled date or don't change it if the result appears to be invalid.

# Example

# For curDate = "01 Jul 2016 16:53:24" and
# changes = [2, 3, -1, 0, 5, 4], the output should be
# solution(curDate, changes) = "03 Oct 2015 16:58:28";

# For curDate = "15 Mar 1998 12:09:59" and
# changes = [-2, 0, 9, 1, 3, 1], the output should be
# solution(curDate, changes) = "15 Mar 1998 12:09:59".

# After changing the date will look like "13 Mar 2007 13:12:60", which is incorrect, because the number of seconds cannot be equal to 60.



from datetime import datetime, timedelta

def solution(curDate, changes):
    # Parse the current date
    curDate = datetime.strptime(curDate, "%d %b %Y %H:%M:%S")

    # Calculate the new date
    try:
        newYear = curDate.year + changes[2]
        newMonth = curDate.month + changes[1]
        newDay = curDate.day + changes[0]
        newHour = curDate.hour + changes[3]
        newMinute = curDate.minute + changes[4]
        newSecond = curDate.second + changes[5]

        # Check if the new date components are valid
        if not(1 <= newMonth <= 12 and 0 <= newHour < 24 and 0 <= newMinute < 60 and 0 <= newSecond < 60):
            raise ValueError

        newDate = datetime(newYear, newMonth, newDay, newHour, newMinute, newSecond)
    except ValueError:
        # If the new date is not valid, return the original date
        return curDate.strftime("%d %b %Y %H:%M:%S")

    return newDate.strftime("%d %b %Y %H:%M:%S")
