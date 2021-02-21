def isValid(self, s):
    stack = []
    validBrackets = ["[]", "{}", "()"]
    openBracket = ["(", "[", "{"]
    for i in s:
        if i in openBracket:
            stack.append(i)
        elif len(stack) > 0:
            bracket = stack.pop()
            if bracket + i in validBrackets:
                pass
            else:
                return False
        else:
            return False
    return True if len(s) > 1 and len(stack) == 0 else False