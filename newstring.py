def bothEnds(s):
    newString = s[:2] + s[-2:]
    return newString

print(bothEnds('spring'))