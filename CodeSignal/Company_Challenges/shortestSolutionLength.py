# In the "Challenges" section on CodeSignal a user can solve one of the existing challenges or submit their own. Each challenge has its own scoreboard organized by programming language. Solutions in these scoreboards are sorted according to their length. When the length of a solution is calculated, all comments and spaces are ignored. Your task is to implement a simplified version of this length calculator.

# Assume that there are only two types of comments:

# line-comment: starting with '//' and ending at the end of the line;
# block-comment: starting with '/*', and ending with the first occurrence of '*/'. It may span several lines.
# Each non-space character outside comments adds 1 to the total length.

# Note that all characters inside each comment are ignored, so they don't introduce nested comments. See the examples for more details.

# Also note that outside any other comment both '//' and '/*' start a new comment (i.e. in this task you don't have to consider the cases where '//', '/*' or '*/' appear inside a string literal).

# Example

# For

# source = ["int a = 2;",
#           "int b = 47;/*37;*///41;",
#           "int c = 3/*4//5*/;",
#           "return a / b * c/*a /* b / c*/;"]
# the output should be solution(source) = 34.

# In the 1st line there are 7 non-space characters;
# In the 2nd line there are 2 comments - /*37;*/ and //41;. Besides those there are only 8 non-space characters;
# The 3rd line contains 1 comment - /*4//5*/, and 7 non-space characters;
# The last line of code has 1 comment - /*a /* b / c*/, and 12 non-space characters;
# In summary, there are 7 + 8 + 7 + 12 = 34 countable characters.
# For

# source = ["var a = 2;",
#           "/*",
#           "var b = 2;",
#           "if (a === b) {",
#           "  b = a + 1;",
#           "  //b = a * 2 - 1;",
#           "}",
#           "*/",
#           "var b = 3;",
#           "return a * b;"]
# the output should be solution(source) = 24.

# Here the code contains one block-comment that covers lines 2 to 8 (1-based). Other lines don't contain comments and have 7, 7, 10 symbols to count, respectively. So, the answer is 7 + 7 + 10 = 24.

def solution(source):
    in_block_comment = False
    length = 0
    for line in source:
        i = 0
        while i < len(line):
            if not in_block_comment and line[i:i+2] == '//':  # Start of a line comment
                break
            elif not in_block_comment and line[i:i+2] == '/*':  # Start of a block comment
                in_block_comment = True
                i += 1
            elif in_block_comment and line[i:i+2] == '*/':  # End of a block comment
                in_block_comment = False
                i += 1
            elif not in_block_comment and line[i] != ' ':  # Non-space character outside comments
                length += 1
            i += 1
    return length
