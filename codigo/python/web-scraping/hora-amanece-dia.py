import requests
from bs4 import BeautifulSoup
import pandas as pd 

# determinar la hora y el amanecer de un dia

lat = 11.40
lng = -69.67
fecha = "2025-02-25"

url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={fecha}"

respuesta_sunset = requests.get(url)

if respuesta_sunset.status_code == 200:
    data = respuesta_sunset.json()
    sunset = data['results']['sunset']
    print(sunset)


response = requests.get(url)

