def solver(s):
    stack = []
    for i in range(0,len(s)):
        if s[i].isdigit():
            stack.append(int(s[i]))
        else:
            y = stack.pop()
            x = stack.pop()
            if s[i] == '+':
                stack.append(x + y)
            elif s[i] == '-':
                stack.append(x - y)
            elif s[i] == '*':
                stack.append(x * y)
            elif s[i] == '/':
                stack.append(x / y)
    return stack.pop()


s = "231*+9-"
n = solver(s)
print(n)