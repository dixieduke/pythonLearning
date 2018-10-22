filename = 'file.txt'

with open(filename) as f:
    content = f.readlines()

print(content)

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)

with open(filename) as fp:
    for i, line in enumerate(fp):
        print(i)
        print(fp.readline())
