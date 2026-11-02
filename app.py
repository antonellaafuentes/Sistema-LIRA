import os
import sys
import streamlit as st

# Agregamos la carpeta raíz para que Python encuentre los módulos de src
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from src.config import APP_TITLE, PAGE_ICON
from src.services.data_service import load_alerts_data, load_resources_data
from src.ui.styles import inject_styles
from src.ui.components import render_safe_exit_bar
from src.views.home import render_home_view
from src.views.alerts import render_alerts_view
from src.views.resources import render_resources_view
from src.views.quiz import render_quiz_view

# 1. Configuración básica de la pestaña del navegador
st.set_page_config(
    page_title=f"{APP_TITLE} | Espacio Seguro y Orientación",
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Selector de tema en la barra lateral (Claro u Oscuro)
with st.sidebar:
    st.markdown(f"### {PAGE_ICON} **{APP_TITLE}**")
    st.caption("Línea de Información, Recursos y Alerta")
    
    # Alternador visual de tema
    tema_seleccionado = st.radio(
        "Tema visual:",
        ["☀️ Claro", "🌙 Oscuro"],
        index=0,
        horizontal=True
    )
    tema = "dark" if "Oscuro" in tema_seleccionado else "light"
    st.markdown("---")

# 3. Aplicamos los estilos CSS centralizados según el tema elegido
inject_styles(theme=tema)

# 4. Cargamos los datos desde los archivos CSV (con memoria caché)
df_alerts = load_alerts_data()
df_resources = load_resources_data()

# 5. Mostramos la barra superior con el botón de salida rápida
render_safe_exit_bar()

# 6. Menú de navegación en la barra lateral
with st.sidebar:
    opcion = st.radio(
        "Navegación:",
        ["🏠 Inicio", "⚠️ Señales de Alerta", "📞 Recursos de Ayuda", "📋 Autoevaluación Rápida"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
    <div class="sidebar-privacy-note">
        🔒 <strong>Privacidad:</strong> Este sitio es confidencial, no almacena tus datos ni guarda respuestas de evaluación.
    </div>
    """, unsafe_allow_html=True)

# 7. Mostramos la pantalla elegida por el usuario
if opcion == "🏠 Inicio":
    render_home_view(df_alerts, df_resources)
elif opcion == "⚠️ Señales de Alerta":
    render_alerts_view(df_alerts)
elif opcion == "📞 Recursos de Ayuda":
    render_resources_view(df_resources)
elif opcion == "📋 Autoevaluación Rápida":
    render_quiz_view(df_alerts)
