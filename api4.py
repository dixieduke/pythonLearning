import requests

url = 'http://api.open-notify.org/iss-now.json'
file = 'apiinfo.txt'
write = 'w'
append = 'a'

response = requests.get(url)
print(response.status_code)
print(response._content)

