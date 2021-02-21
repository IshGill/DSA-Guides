def isRotation(s1, s2):
    count = 0
    for index, letter in enumerate(s1):
        if letter != s2[0]:
            count += 1
        else:
            if s1[:count] in s2 and sorted(s1) == sorted(s2):
                return True
            else:
                return False

print(isRotation("CurryHot","CurryHot"))