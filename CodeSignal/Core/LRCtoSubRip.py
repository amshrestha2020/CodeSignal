# During your most recent trip to Codelandia you decided to buy a brand new CodePlayer, a music player that (allegedly) can work with any possible media format. As it turns out, this isn't true: the player can't read lyrics written in the LRC format. It can, however, read the SubRip format, so now you want to translate all the lyrics you have from LRC to SubRip.

# Since you are a pro programmer (no noob would ever get to Codelandia!), you're happy to implement a function that, given lrcLyrics and songLength, returns the lyrics in SubRip format.

# Example

# For

# lrcLyrics = ["[00:12.00] Happy birthday dear coder,",
#              "[00:17.20] Happy birthday to you!"]
# and songLength = "00:00:20", the output should be

# solution(lrcLyrics, songLength) = [
#   "1",
#   "00:00:12,000 --> 00:00:17,200",
#   "Happy birthday dear coder,",
#   "",
#   "2",
#   "00:00:17,200 --> 00:00:20,000",
#   "Happy birthday to you!"
# ]



def solution(lrcLyrics, songLength):
    ret = []   
    for i, l in enumerate(lrcLyrics, 1):
        sep = l.index(']')
        t, tf = l[1:sep].split(".")
        m, s = map(int, t.split(':'))
        h, m = divmod(m, 60)
        ct = "{:02}:{:02}:{:02},{}0".format(h, m, s, tf)
        
        if i > 1:
            ret[-2] += ct
            ret.append("")
        ret.extend([str(i), ct + " --> ", l[sep + 2:]])
    ret[-2] +=songLength + ',000'
    return ret
