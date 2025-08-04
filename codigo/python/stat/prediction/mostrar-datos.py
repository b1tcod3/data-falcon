import os
import pandas as pd
from soccerdata import SoccerData

API_TOKEN ="94a3896e70fed7579ad6f97b7ae7dcf3f3fac7b4"

sd = SoccerData(token=API_TOKEN)

print("Ligas disponibles:")
print(sd.get_leagues())