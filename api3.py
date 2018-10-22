import urllib.request

url = 'http://api.open-notify.org/iss-now.json'
file = 'apiinfo.txt'
write = 'w'
append = 'a'

with urllib.request.urlopen(url) as query:
    filehandler = open(file,write)
    filehandler.write(str(query.read()))
    filehandler.close()
