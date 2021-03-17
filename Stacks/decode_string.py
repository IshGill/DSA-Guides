#1. Idea is we use a stack, where each element in the stack is a list, the list contains the current string and current repeat value, we know it is the current string because we have not yet hit a closed bracket because once we hit the closed bracket we pop off.
#2. Initialize a stack which contains an empty string and int 1. This is just our final element in the stack which we need to return.
#3. Iterate through the string, we do k * 10 + int(i) because in this would be the best way to get values numerical values greater than 1 digit.
#4. Next we see if we have a open bracket, if we do that means we start a new list and we will build the string in this list until we hit a closing bracket, we also add the k value, remember to reset the k value at this step also for each new list.
#5. Finally, if we hit a closing bracket we assign two variables, one wil hold the string the other will hold the numerical value we will then mutliply that string and add it to our previous stack list element, this is how we continously build our string but adding the previous lists strings in the stack.
#6. If we have simple character then just add it onto the current string portion of the list at the top of the stack.
#7. Return the string portion of the last element in the stack which will hold the decoded list.
def decodeString(self, s):
    stack = [["", 1]]
    k = 0
    for i in s:
        if i.isdigit():
            k = k * 10 + int(i)
        elif i == '[':
            stack.append(["", k])
            k = 0
        elif i == ']':
            char_string, repeat_val = stack.pop()
            stack[-1][0] += char_string * repeat_val
        else:
            stack[-1][0] += i
    return stack[-1][0]