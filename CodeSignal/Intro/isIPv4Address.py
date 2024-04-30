# An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

# Given a string, find out if it satisfies the IPv4 address naming rules.

# Example

# For inputString = "172.16.254.1", the output should be
# solution(inputString) = true;

# For inputString = "172.316.254.1", the output should be
# solution(inputString) = false.

# 316 is not in range [0, 255].

# For inputString = ".254.255.0", the output should be
# solution(inputString) = false.

# There is no first number.

def solution(inputString):
    parts = inputString.split('.')
    
    # Check if there are exactly four parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if each part is a valid integer
        if not part.isdigit():
            return False

        # Check if each number is in the range [0, 255]
        if not (0 <= int(part) <= 255):
            return False

    # Check if the original string starts and ends with a digit
    if not inputString.split('.')[0].isdigit() or not inputString.split('.')[-1].isdigit():
        return False
    
    # Check if the original string and each part have the same representation
    if inputString != '.'.join(str(int(part)) for part in parts):
        return False
    return True

