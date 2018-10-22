import urllib.request

url = 'http://api.open-notify.org/iss-now.json'
file = 'apiinfo.txt'
write = 'w'

with urllib.request.urlopen(url) as query:
    filehandler = open(file,write)
    filehandler.write(str(query.read()))
    filehandler.close()

'''
    g = open('apiinfo.txt','w')
    g.write(str(f.read()))
    g.close()
'''


'''
The below reads info from api site, and prints to console:
with urllib.request.urlopen(url) as f:
    print(f.read())
'''

'''
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
print(response.status_code)
'''