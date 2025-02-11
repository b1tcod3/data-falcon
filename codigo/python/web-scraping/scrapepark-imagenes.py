import requests
from bs4 import BeautifulSoup

# determinar la hora y el amanecer de un dia

url = "https://scrapepark.org/spanish/"

pedido_obtenido = requests.get(url)

html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, 'html.parser')

src_todos = soup.find_all(src=True)

for i, src in enumerate(src_todos):
    if src['src'].endswith('png'):
        print(src['src'])
        r = requests.get(f"https://scrapepark.org/{src['src']}")
        with open(f'image_{i}.png', 'wb') as f:
            f.write(r.content)