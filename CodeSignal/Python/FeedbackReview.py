# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You've launched a revolutionary service not long ago, and were busy improving it for the last couple of months. When you finally decided that the service is perfect, you remembered that you created a feedbacks page long time ago, which you never checked out since then. Now that you have nothing left to do, you would like to have a look at what the community thinks of your service.

# Unfortunately it looks like the feedbacks page is far from perfect: each feedback is displayed as a one-line string, and if it's too long there's no way to see what it is about. Naturally, this horrible bug should be fixed. Implement a function that, given a feedback and the size of the screen, splits the feedback into lines so that:

# each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
# each line is at most size characters long;
# no line has trailing or leading spaces;
# each line should have the maximum possible length, assuming that all lines before it were also the longest possible.
# Example

# For feedback = "This is an example feedback" and size = 8,
# the output should be

# solution(feedback, size) = ["This is", 
#                             "an", 
#                             "example", 
#                             "feedback"

import textwrap

def solution(feedback, size):
    return textwrap.wrap(feedback,size)