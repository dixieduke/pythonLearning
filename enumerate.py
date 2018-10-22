#some sequential list
family = ['Rebecca','Alisson','Missy','Dad']

#create enumeratable and convert to list
x = list(enumerate(family))
print(x)

eObj = enumerate(family)

y = next(eObj)
print(y)
y = next(eObj)
print(y)

for obj in eObj:
    print(obj)