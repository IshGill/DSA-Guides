def backspaceCompare(s, t):
    def StringBuild(x, stack):
        for i in x:
            if i != "#":
                stack.append(i)
            elif stack:
                stack.pop()
        return "".join(stack)
    return StringBuild(s, []) == StringBuild(t, [])
