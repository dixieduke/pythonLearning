'''
x = list(range(100))
print(x)

x = list(range(1,101))
print(x)

for i in range(1,11):
    print(i)
'''

x = list(range(1,1001))
y = []
z = []

for i in x:
    if i %2 == 0:
        y.append(i)
    else:
        z.append(i)

print(y)
print(z)



