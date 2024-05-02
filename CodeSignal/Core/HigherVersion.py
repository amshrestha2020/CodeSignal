# Given two version strings composed of several non-negative decimal fields separated by periods ("."), both strings contain equal number of numeric fields. Return true if the first version is higher than the second version and false otherwise.

# The syntax follows the regular semver ordering rules:

# 1.0.5 < 1.1.0 < 1.1.5 < 1.1.10 < 1.2.0 < 1.2.2
# < 1.2.10 < 1.10.2 < 2.0.0 < 10.0.0
# There are no leading zeros in any of the numeric fields, i.e. you do not have to handle inputs like 100.020.003 (it would instead be given as 100.20.3).

# Example

# For ver1 = "1.2.2" and ver2 = "1.2.0", the output should be
# solution(ver1, ver2) = true;
# For ver1 = "1.0.5" and ver2 = "1.1.0", the output should be
# solution(ver1, ver2) = false.

def solution(ver1, ver2):
    ver1_split = ver1.split(".")
    ver2_split = ver2.split(".")
    min_length = min(len(ver1_split), len(ver2_split))
    max_length = max(len(ver1_split), len(ver2_split))
    
    pointer = 0
    while pointer < min_length:
        ver1_num = int(ver1_split[pointer])
        ver2_num = int(ver2_split[pointer])
        if ver1_num > ver2_num:
            return True
        if ver1_num < ver2_num:
            return False
        pointer += 1
    
    is_length_not_equal = len(ver1_split) != len(ver2_split)
    is_ver1_longer = len(ver1_split) > len(ver2_split)
    
    if is_length_not_equal and is_ver1_longer:
        while pointer < max_length:
            if int(ver2_split[pointer]) > 0:
                return True
            pointer += 1
    
    return False
