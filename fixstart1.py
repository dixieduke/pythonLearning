# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

def fix_start_a(s):
    newstringa = s[1:].replace(s[0],'*') #returns a**ble
    newstringb = s[0] + newstringa
    
    return newstringb

print(fix_start_a('babble'))


