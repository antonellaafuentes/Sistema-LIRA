import streamlit as st
import pandas as pd
from src.services.data_service import filter_alerts
from src.ui.components import render_alert_card

def render_alerts_view(df_alerts: pd.DataFrame):
    # Pantalla del catálogo de señales de alerta con filtros interactivos
    st.markdown('<div class="hero-title">Identificación de Señales de Alerta</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Conoce cómo se manifiestan patrones de aislamiento, control o agresiones sutiles en las relaciones.</div>',
        unsafe_allow_html=True
    )
    
    if df_alerts.empty:
        st.info("No hay señales cargadas actualmente.")
        return
        
    # Obtenemos las categorías disponibles para el filtro
    categorias = ["Todas las categorías"] + sorted(list(df_alerts["Categoría"].unique()))
    
    # Barra de controles con selector de categoría y buscador de texto
    col_filtro, col_search = st.columns([1, 2], gap="medium")
    with col_filtro:
        cat_seleccionada = st.selectbox("Filtrar por categoría", categorias)
    with col_search:
        busqueda = st.text_input("Buscar conducta o concepto", placeholder="Ej: celular, celos, dinero, culpa...")
    
    # Aplicamos el filtro con el servicio de datos
    df_filtrado = filter_alerts(df_alerts, cat_seleccionada, busqueda)
    
    st.caption(f"Mostrando **{len(df_filtrado)}** de **{len(df_alerts)}** señal(es)")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mostramos cada tarjeta de alerta resultante
    for _, fila in df_filtrado.iterrows():
        render_alert_card(
            conducta=fila["Conducta"],
            categoria=fila["Categoría"],
            descripcion=fila["Descripción"]
        )
