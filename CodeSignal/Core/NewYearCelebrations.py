# You're a pretty busy billionaire, and you often fly your personal Private Jet to remote places. Usually travel doesn't bother you, but this time you are unlucky: it's New Year's Eve, and since you have to fly halfway around the world, you'll probably have to celebrate New Year's Day in mid-air!

# Your course lies west of your current location and crosses several time zones. The pilot told you the exact schedule: it is known that you will take off at takeOffTime, and in minutes[i] after takeoff you will cross the ith border between time zones. After crossing each border you will have to set your wrist watch one hour earlier (every second matters to you, so you can't let your watch show incorrect time). It is guaranteed that you won't cross the IDL (i.e. after crossing each time zone border your current time will be set one hour back).

# You've been thinking about this situation and realized that it might be a good opportunity to celebrate New Year's Day more than once, i.e. each time your wrist watch shows 00:00. Assuming that you set your watch immediately after the border is crossed, how many times will you be able to celebrate this New Year's Day with a nice bottle of champagne? Note that the answer should include celebrations both in mid-air and on the ground (it doesn't matter if the plane landed in the last time zone before the midnight or not, you'll not let the last opportunity to celebrate New Year slip through your fingers).

# Example

# For takeOffTime = "23:35" and minutes = [60, 90, 140],
# the output should be
# solution(takeOffTime, minutes) = 3.

# Here is the list of events by the time zones:

# initial time zone:
# at 23:35 your flight starts;
# at 00:00 you celebrate New Year for the first time;
# at 00:35 (60 minutes after the take off) you cross the first border;
# time zone -1:
# at 23:35 you cross the border (00:35 by your initial time zone);
# at 00:00 you celebrate New Year for the second time (01:00 by your initial time zone);
# at 00:05 (90 minutes after the take off) you cross the second border;
# time zone -2:
# at 23:05 you cross the border;
# at 23:55 (140 minutes after the take off) you cross another border;
# time zone -3:
# at 22:55 you cross the border;
# at 00:00 you celebrate New Year for the third time.
# Thus, the output should be 3. That's a lot of champagne!


def solution(take_off_time, minutes):
    result = 0
    over_day = False
    hour, minute = map(int, take_off_time.split(":"))

    if hour == 0:
        hour = 24

    for i in range(len(minutes)):
        prev = minutes[i - 1] if i > 0 else 0
        minute += minutes[i] - prev

        if minute >= 60:
            hour += minute // 60
            minute = minute % 60

        if hour >= 24:
            over_day = True
        if over_day:
            result += 1

        hour -= 1
        if hour > 24 or (hour == 24 and minute != 0):
            return result
        if hour < 24 or (hour == 24 and minute == 0):
            over_day = False

    if not over_day:
        result += 1
    return result

