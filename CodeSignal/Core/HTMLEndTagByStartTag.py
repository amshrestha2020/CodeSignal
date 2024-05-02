# You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.

# Given the starting HTML tag, find the appropriate end tag which your editor should propose.

# If you are not familiar with HTML, consult with this note.

# Example

# For startTag = "<button type='button' disabled>", the output should be
# solution(startTag) = "</button>";
# For startTag = "<i>", the output should be
# solution(startTag) = "</i>".


def solution(startTag):
    startTag = re.search("<[^\s/>]+", startTag).group() 
    return startTag[0] + "/" + startTag[1:] + ">" 

