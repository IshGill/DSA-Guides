# 1. So we are given from 0 to 4 possible digits and we need to find all possible letter combinations for these digits.
# * ie: "23" = 2 = [a, b, c] and b = [d, e ,f] hence 23 = [ad, ae, af, bd, be, bf, cd, ce, cf]
# 2. Do some error checking in case of empty strings.
# 3. Build the hash map which has keys as the numbers and values as their respective letters
# 4. We then make our recursive function where we will do the meat of the work.
# 5. We use backtracking. We make all possible combinations with the 0th index digit key. When we hit an index equal to digits, we have made a valid combination, hence we return pop off the current element and restart the backtracking process.
# 6. Time complexity is O(x^n) * O(n), with X^n being X digits passes and n possibilities per digit. The O(n) because we need to visit O(n) elements.
# 7. Space complexity is O(n) as we build our call stack.
def letterCombinations(self, digits):
    if digits == "":
        return []

    # Mapping where each key is the digit number and values are the letters assigned to it.
    hash_map = {1: [], 2: ["a", "b", "c"], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    # Recursive function to generate the combination strings.
    def backTrack(path, index):
        if index == len(digits):
            combinations.append("".join(path))
            return
        else:
            curr_key_letters = hash_map[int(digits[index])]
            for letter in curr_key_letters:
                path.append(letter)
                backTrack(path, index + 1)
                path.pop()

    combinations, path = [], []
    backTrack(path, 0)
    return combinations