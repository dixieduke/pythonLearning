d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
items = d.items()
keys = d.keys()
values = d.values()

print(items)
print(keys)
print(values)

iterator = iter(keys)
print(next(iterator))
print(next(iterator))

items = ['one','two','three']
iterator = iter(items)
x = next(iterator)
print(x)