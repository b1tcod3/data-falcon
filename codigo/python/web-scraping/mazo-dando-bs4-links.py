import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://conelmazodando.com.ve"

response = requests.get(url)

links = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    contenedores = soup.select('div.contenedor4 > a')
    
    for contenedor in contenedores: 
        link = contenedor.get('href')
        #agregar a links
        links.append({'enlace':link})
else:
    print("Error en la petición: ", response.status_code)   

# Para guardar los enlaces en un archivo CSV   
df = pd.DataFrame(links)
df.to_csv('enlaces.csv')