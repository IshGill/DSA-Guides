def URLify(word):
    return "".join([i.replace(" ", "%20") for i in word.strip()])

print(URLify("My John Smith     "))