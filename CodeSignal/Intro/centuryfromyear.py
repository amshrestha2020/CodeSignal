# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.


def solution(year):
    # Calculate the century by dividing the year by 100
    # and rounding up to the nearest whole number
    century = (year - 1) // 100 + 1
    return century

