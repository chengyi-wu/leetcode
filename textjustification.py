'''
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-20-dynamic-programming-ii-text-justification-blackjack/

Subproblems: Where the 2nd line begins. (word[i:])
'''
import math
import sys
def badness(line, maxWidth):
    w = 0
    for word in line:
        w += len(word)
    if w > maxWidth:
        return float("inf")
    v = (maxWidth - w) * (maxWidth - w) * (maxWidth - w)
    print line, v
    return v

def fullJustify(words, maxWidth):
    #print words
    if len(words) == 0:
        return (0, [])
    line = words[:1]
    min_badness, rest_lines = fullJustify(words[1:], maxWidth)
    min_badness += badness(line, maxWidth)
    lines = [line] + rest_lines
    for i in range(2, len(words) + 1):
        line = words[:i]
        rest_badness, rest_lines = fullJustify(words[i:], maxWidth)
        if badness(line, maxWidth) + rest_badness < min_badness:
            min_badness = badness(line, maxWidth) + rest_badness
            lines = [line] + rest_lines
    return (min_badness, lines)


def test_fullJustify(words, maxWidth):
    print fullJustify(words, maxWidth)

test_fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
