# You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have already watched.

# Example

# For part = "02:20:00" and total = "07:00:00", the output should be
# solution(part, total) = [1, 3].

# You have watched 1 / 3 of the whole video.


def solution(part, total):
    part_in_seconds = convert_time_to_seconds(part)
    total_in_seconds = convert_time_to_seconds(total)
    gcd = get_gcd(part_in_seconds, total_in_seconds)
    return [part_in_seconds // gcd, total_in_seconds // gcd]

def convert_time_to_seconds(time):
    hours, minutes, seconds = map(int, time.split(":"))
    return seconds + minutes * 60 + hours * 3600

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
