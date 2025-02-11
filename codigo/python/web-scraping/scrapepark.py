import requests
from bs4 import BeautifulSoup

# determinar la hora y el amanecer de un dia

url = "https://scrapepark.org/spanish/"

pedido_obtenido = requests.get(url)

html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, 'html.parser')

divs = soup.find_all('div', class_="heading-container heading-center")

print(divs)