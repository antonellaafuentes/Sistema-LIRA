import os
import pandas as pd
from src.config import RUTA_CSV_1, RUTA_CSV_2

def cache_if_streamlit(func):
    # Aplica la memoria caché de Streamlit solo cuando la web está corriendo
    try:
        from streamlit.runtime.scriptrunner import get_script_run_context
        import streamlit as st
        if get_script_run_context() is not None:
            return st.cache_data(func)
    except Exception:
        pass
    return func

def _read_alerts_file() -> pd.DataFrame:
    # Lee y limpia las señales de alerta desde el archivo CSV
    if not os.path.exists(RUTA_CSV_1):
        return pd.DataFrame(columns=["Categoría", "Conducta", "Descripción"])
    
    df = pd.read_csv(RUTA_CSV_1, encoding="utf-8-sig")
    df.columns = [str(col).strip() for col in df.columns]
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()
    return df.dropna(how="all")

def _read_resources_file() -> pd.DataFrame:
    # Lee y limpia las instituciones de ayuda desde el archivo CSV
    if not os.path.exists(RUTA_CSV_2):
        return pd.DataFrame(columns=["Servicio", "Contacto", "Horario", "Notas"])
    
    df = pd.read_csv(RUTA_CSV_2, encoding="utf-8-sig")
    df = df.fillna("")
    df.columns = [str(col).strip() for col in df.columns]
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip().replace("nan", "")
    return df.dropna(how="all")

# Funciones públicas de carga (optimizadas para web o consola)
def load_alerts_data() -> pd.DataFrame:
    # Devuelve el catálogo completo de señales de alerta
    return _read_alerts_file()

def load_resources_data() -> pd.DataFrame:
    # Devuelve el catálogo completo de servicios de ayuda
    return _read_resources_file()

def filter_alerts(df: pd.DataFrame, category: str, search_query: str) -> pd.DataFrame:
    # Filtra las señales según la categoría o la palabra escrita por el usuario
    filtered = df.copy()
    
    # Filtro por categoría seleccionada
    if category and category != "Todas las categorías":
        filtered = filtered[filtered["Categoría"] == category]
    
    # Filtro por texto en el buscador
    if search_query and search_query.strip():
        query = search_query.strip().lower()
        filtered = filtered[
            filtered["Conducta"].str.lower().str.contains(query, na=False) |
            filtered["Descripción"].str.lower().str.contains(query, na=False)
        ]
        
    return filtered
