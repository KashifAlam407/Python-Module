import requests 
from bs4 import BeautifulSoup 

url = 'https://www.bbc.com/news'
response = requests.get(url) 

soup = BeautifulSoup(response.text, 'html.parser') 
headlines = soup.find('body').find_all('h2') 
for x in headlines: 
	print(x.text.strip()) 



##############################################
import requests 
from bs4 import BeautifulSoup 

url = 'https://www.bbc.com/innovation'
response = requests.get(url) 

soup = BeautifulSoup(response.text, 'html5lib') 
headlines = soup.find('body').find_all('h3') 
unwanted = ['BBC World News TV', 'BBC World Service Radio', 
			'News daily newsletter', 'Mobile app', 'Get in touch'] 

for x in list(dict.fromkeys(headlines)): 
	if x.text.strip() not in unwanted: 
		print(x.text.strip()) 

