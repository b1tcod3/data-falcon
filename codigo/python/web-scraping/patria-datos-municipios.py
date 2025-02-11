import requests
import pandas as pd
# determinar la hora y el amanecer de un dia

url = "https://persona.patria.org.ve/public/estados/9"

data = requests.get(url)

municipios = []

if data.status_code == 200:
    data_municipios = data.json()    
    for id,municipio in data_municipios.items():
        municipios.append({'id':id,'nombre': municipio})
else:
    print("Error al obtener los datos")

df = pd.DataFrame(municipios)
df.to_csv('municipios.csv', index=False)