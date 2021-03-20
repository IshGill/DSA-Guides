# 1. We use backtracking. Choice, constraints, goal.
# 2. Choice = will we place a open ( or close ) bracket?
# 3. Constraints:
# * Can only place open if open < n, ie if n = 3 then we have at max ((( ))) of each bracket. Therefore if open = 4 we would have (((( thus invalid.
# * Close < open in order to place close. If close == open then we could place )( which is invalid. If close > open then ))( hence invalid.
# * Max size of the string is 2 * n, why? Because if n = 3 we can have 3 open brackets (((, and 3 closing bracket ))) at max hence 6 in total.
# 4. Goal = find all possible valid combinations, if we stick to our constraints then we WILL get all valid options.
# 5. Rest is simple, we basically just backtrack, nearly exact same story as letter combinations of a phone number, just rememeber we must pop off the recently added element from the stack for backtracking!
# 6. Also, of course iteration starts at 0, 0 for open and closed as we haven't placed any brackets yet.

def generateParenthesis(self, n):
    result, stack = [], []

    def backTrack(open_count, close_count):
        if len(stack) == (2 * n):
            result.append("".join(stack))
            return
        if open_count < n:
            stack.append("(")
            backTrack(open_count + 1, close_count)
            stack.pop()
        if close_count < open_count:
            stack.append(")")
            backTrack(open_count, close_count + 1)
            stack.pop()

    backTrack(0, 0)
    return result