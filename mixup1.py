# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  newstringa = a[:2] + b[2:100]
  newstringb = b[:2] + a[2:100]
  newstringc = newstringb + " " + newstringa
  return newstringc

print(mix_up('dog', 'dinner'))
