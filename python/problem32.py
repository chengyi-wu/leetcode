'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

https://leetcode.com/submissions/detail/146684864/
'''

def longestValidParentheses(s):
    stack = [-1] # invalid index
    maxlen = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        if c == ')':
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                maxlen = max(maxlen, i - stack[-1])
    return maxlen

def test(s):
    print(s, longestValidParentheses(s))

test("(()")
test("(()()")   