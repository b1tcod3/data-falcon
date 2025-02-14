import requests
from bs4 import BeautifulSoup
import re

url = 'https://oxylabs.io/blog'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

blog_titles = soup.find_all('a', class_=re.compile('oxy-1lpa5pr'))

for title in blog_titles:
    print(title.text)

