import requests

## Making a POST request
r = requests.post('https://httpbin.org / post', data={'key':'value'})

print(r)

# print(r.json())