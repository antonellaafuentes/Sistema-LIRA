import streamlit as st
import pandas as pd
from src.ui.components import render_resource_card

def render_resources_view(df_resources: pd.DataFrame):
    # Pantalla del directorio de ayuda gratuita con botones interactivos y notas
    st.markdown('<div class="hero-title">Recursos y Líneas Gratuitas de Asistencia</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Canales oficiales de contención, asesoría legal y apoyo psicológico confidencial. Puedes pulsar directamente para llamar o ingresar al sitio oficial.</div>',
        unsafe_allow_html=True
    )
    
    if df_resources.empty:
        st.info("No hay recursos registrados por el momento.")
        return
        
    # Mostramos los recursos organizados en dos columnas
    col1, col2 = st.columns(2, gap="medium")
    for i, (_, fila) in enumerate(df_resources.iterrows()):
        col_actual = col1 if i % 2 == 0 else col2
        with col_actual:
            render_resource_card(
                servicio=fila.get("Servicio", ""),
                contacto=fila.get("Contacto", ""),
                horario=fila.get("Horario", ""),
                notas=fila.get("Notas", "")
            )
