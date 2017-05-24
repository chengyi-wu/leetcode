'''
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-20-dynamic-programming-ii-text-justification-blackjack/

Subproblems: Where the 2nd line begins. (word[i:])

'''
import math
import sys
def badness(words, i, j, maxWidth):
    w = 0
    for z in range(i, j):
        w += len(words[z])
    if w > maxWidth:
        return sys.maxint
    return (maxWidth - w) * (maxWidth - w) * (maxWidth - w)

def fullJustify(words, maxWidth):
    if len(words) == 1:
        min_badness = badness(words, 0, 1, maxWidth)
        return (min_badness, [words[0]])
    for i in range(1, len(words)):
        #The badness for this line
        b = badness(words, 0, i, maxWidth)
        if b == sys.maxint:
            break
        else:
            n, lines = fullJustify(words[i:], maxWidth)
            if i == 1:
                min_badness = b + n
                line_break = i
            else:
                if b + n < min_badness:
                    min_badness = b + n
                    line_break = i

    lines = [' '.join(words[:line_break])] + lines
    return (min_badness, lines)

def test_fullJustify(words, maxWidth):
    for line in fullJustify(words, maxWidth)[1]:
        print line

test_fullJustify(["This", "is", "an", "example", "of", "text", "justification.", "This", "is", "my", "test."], 16)
