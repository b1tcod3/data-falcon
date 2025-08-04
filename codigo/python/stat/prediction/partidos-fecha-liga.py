import os
import pandas as pd
from soccerdata import FiveThirtyEight

sd = FiveThirtyEight()

def listar_partidos_por_fecha_liga(fecha: str, liga: str = None) -> pd.DataFrame:
    """
    lista de partidos por fecha y liga
    """
    df = sd.read_forecasts()
    
    df_filtrado = df[df['date'].startswith(fecha)]
    
    if liga:
        df_filtrado = df_filtrado[df_filtrado['league'] == liga]
    
    return df_filtrado[['date','league', 'team1', 'team2']]


if __name__ == "__main__":
    
    fecha = "2025-07-08"
    liga = None # "Premier League"
    
    df = listar_partidos_por_fecha_liga(fecha, liga)
    print(df)