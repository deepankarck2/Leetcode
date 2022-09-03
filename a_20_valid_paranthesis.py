from unittest import removeResult


def isValid(s):
    open = ['(', '[', '{']
    close = [')', ']', '}']
    stack = [] 

    for char in s:
        if(char in open):
            stack.append(char)

        if(char in close):
            index = close.index(char)
            if(stack):
                top = stack.pop()
                if(top != open[index]):
                    return False
            else:
                return False

    return not stack

print(isValid("{{{}}}()"))