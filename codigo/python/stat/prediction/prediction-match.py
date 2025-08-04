import os
import pandas as pd
from soccerdata import SoccerData

API_TOKEN ="94a3896e70fed7579ad6f97b7ae7dcf3f3fac7b4"

sd = SoccerData(token=API_TOKEN)

def obtener_datos_partido(league: str, match_id: int) -> pd.DataFrame:
    """
    informacion de un partido
    """
    
    # datos del partido
    partido = sd.get_match(league:league, match_id:match_id)
    
    odds = sd.get_odds(league:league, match_id:match_id)
    
    #equipos
    equipo_home = partido.home_team
    equipo_away = partido.away_team
    
    # forma reciente de los equipos (ultimos 5 partidos)

    forma_home = sd.get_team_form(league:league, team=equipo_home,last=5)
    forma_away = sd.get_team_form(league:league, team=equipo_away,last=5)
    
    # enfrentamientos directo h2h
    h2h = sd.get_h2h(league=league,team1=equipo_home,team2=equipo_away,last=5)
    
    data = {
        "fecha": [partido.date],
        "liga": [league],
        "equipo_home": [equipo_home],
        "equipo_away": [equipo_away],
        "forma_home": [forma_home],
        "forma_away": [forma_away],
        "h2h": [h2h],
        "odds": [odds]
    }
    
    df = pd.DataFrame(data)
    
    return df

def analizar_partido(df: pd.DataFrame) -> str:
    """
    ANALIZAR PARTIDO
    """
    
    row = df.iloc[0]
    odds = row.odds
    
    forma_home_mean = sum([r[2] for r in row.forma_home])/ len(row.forma_home)
    forma_away_mean = sum([r[2] for r in row.forma_away])/ len(row.forma_away)
    
    suggestion = "No hay sugerencia clara"
    
    # cuota de victoria local
    home_win_odds = odds.get('home_win', {}).get('average')
    if forma_home_mean > forma_away_mean and home_win_odds < 2.0:
        suggestion = "Local"
    
    # cuota de empate
    draw_odds = odds.get('draw', {}).get('average')
    if forma_home_mean == forma_away_mean and draw_odds < 2.0:
        suggestion = "Empate"
    
    # cuota de victoria visitante
    away_win_odds = odds.get('away_win', {}).get('average')
    if forma_away_mean > forma_home_mean and away_win_odds < 2.0:
        suggestion = "Visitante"
    
    return suggestion

if __name__ == "__main__":
    
    league = "Premier League"
    match_id = 1
    
    df = obtener_datos_partido(league, match_id)
    print("Datos del partido:")
    print(df.to_dict(orient='records'))
    
    suggestion = analizar_partido(df)
    print("Sugerencia:", suggestion)
    