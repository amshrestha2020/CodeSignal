# You've intercepted an encrypted message, and you are really curious about its contents. You were able to find out that the message initially contained only lowercase English letters, and was encrypted with the following cipher:

# Let all letters from 'a' to 'z' correspond to the numbers from 0 to 25, respectively.
# The number corresponding to the ith letter of the encrypted message is then equal to the sum of numbers corresponding to the first i letters of the initial unencrypted message modulo 26.
# Now that you know how the message was encrypted, implement the algorithm to decipher it.

# Example

# For message = "taiaiaertkixquxjnfxxdh", the output should be
# solution(message) = "thisisencryptedmessage".

# The initial message "thisisencryptedmessage" was encrypted as follows:

# letter 0: t -> 19 -> t;
# letter 1: th -> (19 + 7) % 26 -> 0 -> a;
# letter 2: thi -> (19 + 7 + 8) % 26 -> 8 -> i;
# etc.

def solution(message):
    sum_val = 0
    res = []
    char_code_a = ord('a')

    for char in message:
        cur_char_code = ord(char) - char_code_a

        decrypted_char_code = cur_char_code - sum_val
        if sum_val > cur_char_code:
            decrypted_char_code += 26

        res.append(chr(decrypted_char_code + char_code_a))
        sum_val = cur_char_code

    return ''.join(res)
