import pandas as pd
import requests
#leer archivo csv

municipios = pd.read_csv('municipios.csv',index_col=0)

parroquias = []

for id,row in municipios.iterrows():
    
    url = f"https://persona.patria.org.ve/public/estados/9/{id}"
    
    data = requests.get(url)

    if data.status_code == 200:
        data_parroquias = data.json()    
        for id_parroquia,parroquia in data_parroquias.items():
            parroquias.append({'id':id_parroquia,'parroquia': parroquia,'municipio':row['nombre'],'municipio_id':id})
    else:
        print("Error al obtener los datos")
    
df = pd.DataFrame(parroquias)
df.to_csv('parroquias.csv', index=False)