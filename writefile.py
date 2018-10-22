f = open('test.txt','w')

f.write('Hello world, \n')
f.write('This is written to file \n')

f.close()

f = open('test.txt','a')

f.write("Don't delete existing data \n")
f.write('Add this to existing file.')

f.close()