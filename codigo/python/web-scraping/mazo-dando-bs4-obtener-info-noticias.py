import requests
from bs4 import BeautifulSoup
import pandas as pd 

root_url = "https://conelmazodando.com.ve"
# get the data from csv file
df = pd.read_csv('enlaces.csv')
noticias = []

# recorrer el dataframe
for index, row in df.iterrows():
    url = root_url+row['enlace']
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titulo = soup.select('article h1')[0].text
        
        parrafos = soup.select('div#newsbody > p')
        fecha = parrafos[0].text.split(' ')[1]
        
        texto = ""
        
        for parrafo in parrafos[1:]:
            texto += " "+parrafo.text
        
        noticia ={
            'titulo': titulo,
            'fecha': fecha,
            'texto': texto
        }
        noticias.append(noticia)
    else:
        print("Error en la petición: ", response.status_code)

# Para guardar las noticias en un archivo CSV
df = pd.DataFrame(noticias)
df.to_csv('noticias-25-enero.csv')



