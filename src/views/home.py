import streamlit as st
import pandas as pd
from src.config import EMERGENCY_PHONE_1, EMERGENCY_PHONE_2

def render_home_view(df_alerts: pd.DataFrame, df_resources: pd.DataFrame):
    # Pantalla principal con introducción, métricas y panel de emergencia
    st.markdown('<div class="hero-title">Espacio de Orientación y Prevención</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">El Sistema LIRA te ayuda a identificar conductas de riesgo en vínculos cotidianos y te conecta con recursos de asistencia profesional gratuitos.</div>',
        unsafe_allow_html=True
    )
    
    col_izq, col_der = st.columns([1.8, 1.2], gap="medium")
    
    with col_izq:
        st.markdown("""
        #### ¿Cómo funciona esta plataforma?
        
        - 🔎 **Consulta de señales:** Revisa conductas tipificadas según el grado de control, manipulación o agresión psicológica.
        - 📝 **Autoevaluación confidencial:** Realiza un ejercicio de reflexión para identificar dinámicas en tu entorno.
        - 🤝 **Directorio de apoyo:** Accede a números de teléfono, centros de atención y horarios disponibles en todo momento.
        """)
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Señales tipificadas", len(df_alerts))
        with c2:
            st.metric("Redes de ayuda gratuitas", len(df_resources))
            
    with col_der:
        st.markdown(f"""
        <div class="emergency-banner">
            <h4>🚨 ¿En peligro inmediato?</h4>
            <p>Si estás viviendo una situación de riesgo inminente, llama al <strong>{EMERGENCY_PHONE_1}</strong> o a la línea nacional especializada (<strong>{EMERGENCY_PHONE_2}</strong>) de inmediato.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-pro card-callout">
            <h5 class="card-callout-title">💬 Tu seguridad es lo primero</h5>
            <p class="card-callout-text">
                Reconocer señales no es exagerar. Buscar información a tiempo permite construir vínculos basados en la libertad y el respeto mutuo.
            </p>
        </div>
        """, unsafe_allow_html=True)
