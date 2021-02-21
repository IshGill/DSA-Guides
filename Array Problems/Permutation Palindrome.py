#We know for a permutation palindrome that if we have an even number of appearnces of the letters with at most one letter having a odd apperance this is a valid permutation palindrome
def permutationpalindrome(word):
    checker = {}
    for i in word.strip().lower():
        if i.isalpha():
            if i not in checker:
                checker[i] = 1
            else:
                checker[i] += 1
    flag = 0
    for values in checker.values():
        if values % 2 != 0:
            flag += 1
            if flag >= 2:
                return False
    return True if bool(checker) else False


print(permutationpalindrome("Tact Coa"))
print(permutationpalindrome("abcdefg"))
print(permutationpalindrome("1234"))
print(permutationpalindrome("                 "))
print(permutationpalindrome("12321435gdv dbadfbgf dgb dafgfdgt43t4ete508488048/'/;.'.;/.'/;.'/;.';/',;"))