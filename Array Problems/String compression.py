def stringCompression(s):
    compressed_string = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed_string.append(s[i])
            compressed_string.append(str(count))
            count = 0
    return "".join(compressed_string) if len(compressed_string) < len(s) else s

print(stringCompression("aabcccccaaa"))

