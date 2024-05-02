# While exploring the ruins of a golden lost city, you discovered an ancient manuscript containing series of strange symbols. Thanks to your profound knowledge of dead languages, you realized that the text was written in one of the dialects of Befunge-93. Looks like the prophecy was true: you are the one who can find the answer to the Ultimate Question of Life! Of course you brought your futuristic laptop with you, so now you just need a function that will run the encrypted message and make you the all-knowing human being.

# Befunge-93 is a stack-based programming language, the programs for which are arranged in a two-dimensional torus grid. The program execution sequence starts at the top left corner and proceeds to the right until the first direction instruction is met (which can appear in the very first cell). The torus adjective means that the program never leaves the grid: when it encounters a border, it simply goes to the next command at the opposite side of the grid.

# You need to write a function that will be able to execute the given Befunge-93 program. Unfortunately your laptop, futuristic that it is, can't handle more than 105 instructions and will probably catch on fire if you try to execute more, so the function should exit after 105 commands. The good news is, the prophesy said that the answer to the Ultimate Question of Life contains no more than 100 symbols, so the function should return the program output once it contains 100 symbols.

# The dialect of Befunge-93 in the manuscript consists of the following commands:

# direction instructions:
# >: start moving right
# <: start moving left
# v: start moving down
# ^: start moving up
# #: bridge; skip next cell
# conditional instructions:
# _: pop a value; move right if value = 0, left otherwise
# |: pop a value; move down if value = 0, up otherwise
# math operators:
# +: addition; pop a, pop b, then push a + b
# -: subtraction; pop a, pop b, then push b - a
# *: multiplication; pop a, pop b, then push a * b
# /: integer division; pop a, pop b, then push b / a
# %: modulo operation; pop a, pop b, then push b % a
# logical operators:
# !: logical NOT; pop a value, if the value = 0, push 1, otherwise push 0
# `: greater than; pop a and b, then push 1 if b > a, otherwise 0
# stack instructions:
# :: duplicate value on top of the stack
# \: swap the top stack value with the second to the top
# $: pop value from the stack and discard it
# output instructions:
# .: pop value and output it as an integer followed by a space
# ,: pop value and output it as ASCII character
# digits 0-9: push the encountered number on the stack
# ": start string mode; push each character's ASCII value all the way up to the next "
#   (whitespace character): empty instruction; does nothing
# @: end program; the program output should be returned then
# If the stack is empty and it is necessary to pop a value, no exception is raised; instead, 0 is produced.

# Example

# For

# program = [
#     "               v",
#     "v  ,,,,,"Hello"<",
#     ">48*,          v",
#     ""!dlroW",,,,,,v>",
#     "25*,@         > "
# ]
# the output should be solution(program) = "Hello World!\n".

# Note, that in the tests tab you will see a \ as an escape symbol before each ".

# Here is how the program is executed:

# the program starts executing at the top left corner, doing nothing according to the   command until it meets the v command, which makes the instructions direct it downward;
# the < makes it go left;
# the " starts the string mode; "Hello" is pushed backwards on the stack;
# six , symbols produce the "Hello" word, emptying the stack;
# since the v symbol is encountered, the third line starts executing;
# 4 and 8 are pushed on the stack; the * operator pops them, multiplies and puts the result (4 * 8 = 32) back on the stack;
# the , operator produces the character with the ASCII value of 32, which is a whitespace character;
# all the empty (' ') instructions are then executed, until the v command is encountered; then, the fourth line starts to execute;
# the > command forces instructions to the right to execute; since there is a border to the right, the leftmost instruction in the fourth line is executed next;
# another string " mode starts, which pushes "World!" backwards on the stack;
# next, the , commands output the "World!" string;
# the v command moves command execution to the next line;
# the > command moves command execution to the very beginning of the fifth line;
# 2 * 5 = 10 is pushed on the stack, and produced as a character \n;
# finally, @ finishes the program execution.

import random


def solution(program):
    # Initialize the stack and the output
    stack = []
    output = ''

    # Convert the program into a list of lists for easier access
    program = [list(row) for row in program]

    # Initialize the direction to right
    dx, dy = 1, 0

    # Initialize the position
    x, y = 0, 0

    # Initialize the string mode to False
    string_mode = False

    # Initialize the instruction count
    instruction_count = 0

    while instruction_count < 10**5 and len(output) < 100:
        # Get the current command
        command = program[y][x]

        # If we're in string mode and the command isn't ", push the ASCII value of the command
        if string_mode and command != '"':
            stack.append(ord(command))
        else:
            # Otherwise, interpret the command
            if command.isdigit():
                stack.append(int(command))
            elif command == '+':
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                stack.append(a + b)
            elif command == '-':
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                stack.append(b - a)
            elif command == '*':
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                stack.append(a * b)
            elif command == '/':
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                stack.append(b // a if a != 0 else 0)
            elif command == '%':
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                stack.append(b % a if a != 0 else 0)
            elif command == '!':
                a = stack.pop() if stack else 0
                stack.append(1 if a == 0 else 0)
            elif command == '`':
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                stack.append(1 if b > a else 0)
            elif command == '>':
                dx, dy = 1, 0
            elif command == '<':
                dx, dy = -1, 0
            elif command == '^':
                dx, dy = 0, -1
            elif command == 'v':
                dx, dy = 0, 1
            elif command == '?':
                dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            elif command == '_':
                a = stack.pop() if stack else 0
                dx, dy = (1, 0) if a == 0 else (-1, 0)
            elif command == '|':
                a = stack.pop() if stack else 0
                dx, dy = (0, 1) if a == 0 else (0, -1)
            elif command == '"':
                string_mode = not string_mode
            elif command == ':':
                stack.append(stack[-1] if stack else 0)
            elif command == '\\':
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                stack.extend([a, b])
            elif command == '$':
                if stack:
                    stack.pop()
            elif command == '.':
                a = stack.pop() if stack else 0
                output += str(a) + ' '
            elif command == ',':
                a = stack.pop() if stack else 0
                output += chr(a)
            elif command == '#':
                x = (x + dx) % len(program[0])
                y = (y + dy) % len(program)
            elif command == '@':
                break

        # Move to the next command
        x = (x + dx) % len(program[0])
        y = (y + dy) % len(program)

        # Increment the instruction count
        instruction_count += 1

    return output

