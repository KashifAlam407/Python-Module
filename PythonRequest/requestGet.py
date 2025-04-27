
import requests

# params = {'kashif': 'Alam'}

response = requests.get("https://google.com" params=params)

##----- request.get() all parameters -----

## 1. url (required):- This is the main url to which your are making the get request. It can be a full URL or a relative path.
## [response = requests.get('https://api.example.com/data')]


## 2. params (optional):- This is used to send query parameters in the URL. These parameters are typically appended to the URL after a '?', and multiple parameters are separated by '&'. This parameters is passed as a dictionary.
## [params = {'search': 'python', 'page': 2}
## response = requests.get('https://api.example.com/search', params=params)
## This will make a request to: https://api.example.com/search?search=python&page=2]

## 3. headers (optional): You can pass HTTP headers as a dictionary. Headers allow you to provide additional information to the server about the request (eg., user-agent, authoriation tokens, etc.).
##----------------------------------------




# #------------ RESPONSE METHOD --------------
# print(response)  ## <Response [200]>

# print(response.content)  ## return the content of the response in bytes

# print(response.headers)  ## return a dictionary of response headers

# print(response.encoding)  ## return the encoding used to decode response.content (ex - ISO-8859-1)

# print(response.elapsed)  ## return a timedelta object with the time elapsed from sending the requests to the arrival of the response (ex - 0:00:02.253725)

# print(response.close()) ## closes the connection to the server

# print(response.cookies)  ## returns a cookieJar objects with the cookies sent back from the server

# print(response.history)  ## returns a list of response objects holding the history of request(url)

# print(response.is_permanent_redirect)  ## returns True if the response is the permanent redirected url, otherwise False

# print(response.is_redirect)  ## returns True if the response was redirected, otherwise False.

# print(response.iter_content())  ## iterates over the response.content

# print(response.json())  ## returns a JSON object of the result (if the result was written in JSON format, if not it raise an error)

print(response.url)  ## returns the URL of the response

# print(response.status_code)  ## return a number that incicates the status (200 is OK, 404 is Not Found)

# print(response.request) ## returns the request object that requested this response

# print(response.reason) ## returns a text corresponding to the status code

# print(response.raise_for_status())  ## returns an HTTPError object if an error has occurred during the process

# print(response.ok) ## returns True if status_code is less than 200 otherwise False

# print(response.links) ## returns the header links

# print(response.text)




##############################################
## --- AUTHENTICATION USING PYTHON REQUEST ---

# import requests

# from requests.auth import HTTPBasicAuth

# ## making a get request
# response = requests.get('https://google.com / user, ', auth=HTTPBasicAuth('user', 'pass'))

# ## print request object
# print(response)






