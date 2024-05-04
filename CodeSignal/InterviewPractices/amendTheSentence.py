# You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

# Put a single space between the words.
# Convert the uppercase letters to lowercase.
# Example

# For s = "CodesignalIsAwesome", the output should be
# solution(s) = "codesignal is awesome";
# For s = "Hello", the output should be
# solution(s) = "hello".


def solution(s):
    amended_sentence = ""
    
    # Iterate through the characters of the string
    for i, char in enumerate(s):
        # If the current character is uppercase and not the first character
        if char.isupper() and i > 0:
            # Insert a space before the uppercase letter
            amended_sentence += " "
        # Convert the character to lowercase and append it to the amended sentence
        amended_sentence += char.lower()
    
    return amended_sentence

# Test cases
print(solution("CodesignalIsAwesome"))  # Output: "codesignal is awesome"
print(solution("Hello"))  # Output: "hello"
