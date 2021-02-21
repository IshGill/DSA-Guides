def findReplaceString(s, indexes, sources, targets):
    dupe_s = s[:]
    for i in range(len(indexes)):
        curr = s[indexes[i]]
        if curr == sources[i][0]:
            print(curr)
            dupe_s = dupe_s.replace(sources[i], targets[i])
            print(dupe_s)
    return dupe_s