import pandas as pd
import requests
#leer archivo csv

parroquias = pd.read_csv('parroquias.csv',index_col=0)

comunidades = []

for id,row in parroquias.iterrows():
    
    url = f"https://persona.patria.org.ve/public/estados/9/{row['municipio_id']}/{id}"
    
    data = requests.get(url)

    if data.status_code == 200:
        data_comunidades = data.json()    
        for id_comunidad,comunidad in data_comunidades.items():
            comunidades.append({'id':id_comunidad,'comunidad': comunidad,'parroquia':row['parroquia'],'parroquia_id':id,'municipio':row['municipio'],'municipio_id':row['municipio_id']})
    else:
        print("Error al obtener los datos")
    
df = pd.DataFrame(comunidades)
df.to_csv('comunidades.csv', index=False)