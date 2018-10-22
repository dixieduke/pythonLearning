#sort lists
#numbers
x = [3,6,21,1,5,98,4,23,1,6]
print(x)
x.sort()
print(x)

#strings
words = ['be','car','always','door','eat']
words.sort()
print(words)
#words.sort(reverse=True)
words = words[::-1]
print(words)

a = [(1,9),(7,2),(9,0)]
print(a)
print(a[1])
sorted(a,key=lambda a: a[1])
print(a)

