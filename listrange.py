#x = list(range(100))
#print(x)
#
#x = list(range(1,101))
#print(x)

for i in range(1,11):
    print(i)

x = list(range(20))
print(min(x))
print(max(x))

y = []
z = []
for number in x:
    if number%2 == 0: #the modulus is the remainder of division b/t two munbers. 5 / 2 has remainder of 1, so 5%2 = 1
        y.append(number)
    else:
        z.append(number)       
print(y)
print(z)
