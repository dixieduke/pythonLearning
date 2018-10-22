ratings = [3,4,5,6]
print(ratings)

#the following doesn't add to the list, it replaces existing lists
ratings = ['a','b','c','d']
print(ratings)
print(ratings[2])

list = ['Spartanburg','Greenville','Columbia','Union']

print(list)
print(list[0])

list2 = [1,2,3,4,5]

print(sum(list2))
print(min(list2))
print(max(list2))
print(list2[0])
print(list2[-1])

#sort lists
x = [3,6,1,21,98,6]
print(x)
x.sort()
print(x)

#the below items do the same thing; the 2nd line is shorter
x.sort(reverse=True)
#x = x[::-1]
print(x)