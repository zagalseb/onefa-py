import pandas as pd

BASE = "https://raw.githubusercontent.com/zagalseb/onefa-data/main"


def load_onefa_teams() -> pd.DataFrame:
    """Equipos de la ONEFA: una fila por equipo.

    Columnas: id, nombre, nombre_corto, abreviatura, institucion, ciudad,
    estado, conferencia, logo_url, logo_oscuro_url, color_primario,
    color_primario_texto, color_secundario, color_secundario_texto,
    estadio, estadio_lat, estadio_lng.
    """
    return pd.read_parquet(f"{BASE}/teams/onefa_teams.parquet")
