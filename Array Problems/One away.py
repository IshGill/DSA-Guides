def OneAway(word1, word2):
    if len(word1) == len(word2):
        return OneEditReplace(word1, word2)
    elif len(word1) + 1 == len(word2):
        return OneEditInsert(word1, word2)
    elif len(word1) - 1 == len(word2):
        return OneEditInsert(word2, word1)
    return False

def OneEditReplace(word1, word2):
    founddifference = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if founddifference:
                return False
        founddifference = True
    return True

def OneEditInsert(word1, word2):
    index1 = 0
    index2 = 0
    while index2 < len(word2) and index1 < len(word1):
        if word1[index1] != word2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

print(OneAway("pale", "ple"))
print(OneAway("pale", "bake"))