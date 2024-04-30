# Check if the given string is a correct time representation of the 24-hour clock.

# Example

# For time = "13:58", the output should be
# solution(time) = true;
# For time = "25:51", the output should be
# solution(time) = false;
# For time = "02:76", the output should be
# solution(time) = false.


def solution(time):
    try:
        hours, minutes = map(int, time.split(':'))
        return 0 <= hours < 24 and 0 <= minutes < 60
    except ValueError:
        return False


