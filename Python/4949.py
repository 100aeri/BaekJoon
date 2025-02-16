def isVPS(s):
    brackets = list(filter(lambda x: x in ['(',')','[',']'], list(s)))
    stack = []
    for i in brackets:

        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
        elif i == '[':
            stack.append(i)
        else:
            if len(stack) == 0 or stack[-1] != '[':
                return False
            stack.pop()
    return (len(stack) == 0)



input_strings = []

while True:
    s = input()
    if s == '.':
        break
    input_strings.append(s)

for i in input_strings:
    print("yes") if(isVPS(i)) else print("no")