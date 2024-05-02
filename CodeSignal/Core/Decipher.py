# Consider the following ciphering algorithm:

# For each character replace it with its code.
# Concatenate all of the obtained numbers.
# Given a ciphered string, return the initial one if it is known that it consists only of lowercase letters.

# Note: here the character's code means its decimal ASCII code, the numerical representation of a character used by most modern programming languages.

# Example

# For cipher = "10197115121", the output should be
# solution(cipher) = "easy".

# Explanation: charCode('e') = 101, charCode('a') = 97, charCode('s') = 115 and charCode('y') = 121.

def solution(cipher):
    sum_val = 0
    res = []
    char_code_z = ord("z")

    for num in cipher:
        potential_char_code = sum_val * 10 + int(num)

        if potential_char_code <= char_code_z:
            sum_val = potential_char_code
        else:
            res.append(chr(sum_val))
            sum_val = int(num)

    res.append(chr(sum_val))
    return "".join(res)
