import urllib.request

url = 'http://api.open-notify.org/iss-now.json'

with urllib.request.urlopen(url) as f:
    print(f.read())


'''
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
print(response.status_code)
'''