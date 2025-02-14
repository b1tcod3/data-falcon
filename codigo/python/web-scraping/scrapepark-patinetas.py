import requests
from bs4 import BeautifulSoup

# determinar la hora y el amanecer de un dia

url = "https://scrapepark.org/spanish/"

pedido_obtenido = requests.get(url)

html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, 'html.parser')

divs = soup.find_all('div', class_='detail-box')

products = []
precios = []

for div in divs:
    if (div.h6 is not None) and ('Patineta' in div.h5.text):
        
        product = div.h5.get_text(strip=True)
        precio = div.h6.get_text(strip=True).replace('$', '')
        
        # filtras los productos por un precio
        products.append(product)
        precios.append(precio)

print(products)
print(precios)