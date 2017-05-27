import math
def evalRPN(token):
    stack = []
    for i in range(len(token)):
        #print token[i]
        if token[i].lstrip('-').isdigit():
            stack.append(float(token[i]))
            #print stack
        if token[i] in "+-*/":
            op1 = stack.pop()
            op2 = stack.pop()
            if token[i] == '+':
                stack.append(op1 + op2)
            if token[i] == '-':
                stack.append(op2 - op1)
            if token[i] == '*':
                stack.append(op1 * op2)
            if token[i] == '/':
                stack.append(int(op2 / op1))
        #print stack
    return int(stack[-1])
'''
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
#print evalRPN(["3", "-4", "+"])
#print evalRPN(["2", "1", "+", "3", "*"])
#print evalRPN(["4", "13", "5", "/", "+"] )
print evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print evalRPN(["4","13","5","/","+"])
