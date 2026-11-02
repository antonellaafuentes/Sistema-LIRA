import streamlit as st
import pandas as pd
import os

# Configuración inicial de página
st.set_page_config(
    page_title="Sistema LIRA | Espacio Seguro y Orientación",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inyección de estilos con principios de diseño Impeccable
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');


    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #F5F5DC;
    }

    /* Ocultar elementos sobrantes del footer predeterminado */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Encabezados y jerarquía */
    .hero-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: #F5F5DC;
        letter-spacing: -0.025em;
        line-height: 1.25;
        margin-bottom: 0.35rem;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #F5F5DC;
        line-height: 1.55;
        margin-bottom: 1.75rem;
    }

    /* Tarjetas de contenido refinadas */
    .card-pro {
        background: #F5F5DC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.25rem 1.4rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .card-pro:hover {
        border-color: #CBD5E1;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    }

    /* Badges de categorías */
    .badge-category {
        display: inline-block;
        padding: 0.25rem 0.65rem;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        background-color: #EAD2A8;
        color: #EAD2A8;
        margin-bottom: 0.5rem;
    }

    /* Caja de emergencia empática y sobria */
    .emergency-banner {
        background: linear-gradient(135deg, #F5F5DC 0%, #F5F5DC 100%);
        border: 1px solid #FECACA;
        border-left: 5px solid #EF4444;
        border-radius: 12px;
        padding: 1.25rem 1.4rem;
        margin-bottom: 1.5rem;
    }
    .emergency-banner h4 {
        margin: 0 0 0.4rem 0;
        color: #EAD2A8;
        font-weight: 700;
    }
    .emergency-banner p {
        margin: 0;
        color: #7F1D1D;
        font-size: 0.95rem;
        line-height: 1.45;
    }

    /* Tarjetas de recursos de contacto */
    .resource-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #F5F5DC;
        margin-bottom: 0.35rem;
    }
    .contact-badge {
        display: inline-block;
        font-size: 1.1rem;
        font-weight: 700;
        color: #F5F5DC;
        background: #F5F5DC;
        border: 1px solid #CCFBF1;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        margin: 0.3rem 0;
    }
    .schedule-info {
        font-size: 0.88rem;
        color: #F5F5DC;
        margin-top: 0.25rem;
    }

    /* Métricas destacadas */
    div[data-testid="stMetric"] {
        background-color: #F5F5DC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    }
    </style>
""", unsafe_allow_html=True)

# Rutas de los CSV
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV_1 = os.path.join(DIRECTORIO_ACTUAL, "trabajo ciencias 1.csv")
RUTA_CSV_2 = os.path.join(DIRECTORIO_ACTUAL, "trabajo ciencias 2.csv")

@st.cache_data
def cargar_datos_alertas():
    if not os.path.exists(RUTA_CSV_1):
        return pd.DataFrame(columns=["Categoría", "Conducta", "Descripción"])
    df = pd.read_csv(RUTA_CSV_1, encoding="utf-8-sig")
    df.columns = [col.strip() for col in df.columns]
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()
    return df.dropna(how="all")

@st.cache_data
def cargar_datos_recursos():
    if not os.path.exists(RUTA_CSV_2):
        return pd.DataFrame(columns=["Servicio", "Contacto", "Horario"])
    df = pd.read_csv(RUTA_CSV_2, encoding="utf-8-sig")
    df.columns = [col.strip() for col in df.columns]
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()
    return df.dropna(how="all")

df_alertas = cargar_datos_alertas()
df_recursos = cargar_datos_recursos()

# Barra lateral de navegación
with st.sidebar:
    st.markdown("### 🛡️ **Sistema LIRA**")
    st.caption("Línea de Información, Recursos y Alerta")
    st.markdown("---")
    
    opcion = st.radio(
        "Secciones:",
        ["🏠 Inicio", "⚠️ Señales de Alerta", "📞 Recursos de Ayuda", "📋 Autoevaluación Rápida"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.85rem; color: #F5F5DC; line-height: 1.45;">
        🔒 <strong>Privacidad:</strong> Este sitio es confidencial, no almacena tus datos ni guarda respuestas de evaluación.
    </div>
    """, unsafe_allow_html=True)

# ==================== VISTA: INICIO ====================
if opcion == "🏠 Inicio":
    st.markdown('<div class="hero-title">Espacio de Orientación y Prevención</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">El Sistema LIRA te ayuda a identificar conductas de riesgo en vínculos cotidianos y te conecta con recursos de asistencia profesional gratuitos.</div>', unsafe_allow_html=True)
    
    col_izq, col_der = st.columns([1.8, 1.2], gap="large")
    
    with col_izq:
        st.markdown("""
        #### ¿Cómo funciona esta plataforma?
        
        - 🔎 **Consulta las señales:** Revisa conductas tipificadas según el grado de control, manipulación o agresión psicológica.
        - 📝 **Autoevaluación:** Realiza un ejercicio confidencial de reflexión para analizar dinámicas en tu entorno o en el de amistades.
        - 🤝 **Encuentra ayuda:** Accede a números de teléfono, centros de atención y horarios disponibles en todo momento.
        """)
        
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Señales tipificadas", len(df_alertas))
        with c2:
            st.metric("Redes de ayuda gratuitas", len(df_recursos))
            
    with col_der:
        st.markdown("""
        <div class="emergency-banner">
            <h4>🚨 ¿En peligro inmediato?</h4>
            <p>Si estás viviendo una situación de riesgo inminente, llama al <strong>911</strong> o a la línea nacional especializada (<strong>144</strong> en Argentina) de inmediato.</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.container():
            st.markdown("""
            <div class="card-pro" style="border-left: 4px solid #4338CA;">
                <h5 style="margin: 0 0 0.35rem 0; color: #1E293B;">💬 Tu seguridad es lo primero</h5>
                <p style="margin: 0; font-size: 0.9rem; color: #F5F5DC  ; line-height: 1.4;">
                    Reconocer señales no es exagerar. Buscar información a tiempo permite construir vínculos basados en la libertad y el respeto.
                </p>
            </div>
            """, unsafe_allow_html=True)

# ==================== VISTA: SEÑALES DE ALERTA ====================
elif opcion == "⚠️ Señales de Alerta":
    st.markdown('<div class="hero-title">Identificación de Señales de Alerta</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Conoce cómo se manifiestan patrones de aislamiento, control o agresiones sutiles en las relaciones.</div>', unsafe_allow_html=True)
    
    if df_alertas.empty:
        st.info("No hay señales cargadas actualmente.")
    else:
        categorias = ["Todas las categorías"] + sorted(list(df_alertas["Categoría"].unique()))
        
        col_filtro, col_search = st.columns([1, 2], gap="medium")
        with col_filtro:
            cat_seleccionada = st.selectbox("Filtrar por categoría", categorias)
        with col_search:
            busqueda = st.text_input("Buscar conducta o concepto", placeholder="Ej: celular, celos, aislamiento, dinero...")
        
        # Filtrado
        df_mostrar = df_alertas.copy()
        if cat_seleccionada != "Todas las categorías":
            df_mostrar = df_mostrar[df_mostrar["Categoría"] == cat_seleccionada]
        if busqueda.strip():
            df_mostrar = df_mostrar[
                df_mostrar["Conducta"].str.contains(busqueda, case=False, na=False) |
                df_mostrar["Descripción"].str.contains(busqueda, case=False, na=False)
            ]
            
        st.caption(f"Mostrando **{len(df_mostrar)}** señal(es) encontrada(s)")
        st.markdown("<br>", unsafe_allow_html=True)
        
        for _, fila in df_mostrar.iterrows():
            with st.container():
                st.markdown(f"""
                <div class="card-pro">
                    <span class="badge-category">{fila['Categoría']}</span>
                    <h3 style="margin: 0.2rem 0 0.6rem 0; font-size: 1.15rem; font-weight: 600; color: #0F172A;">
                        {fila['Conducta']}
                    </h3>
                    <p style="margin: 0; font-size: 0.95rem; color: #F5F5DC; line-height: 1.55;">
                        {fila['Descripción']}
                    </p>
                </div>
                """, unsafe_allow_html=True)

# ==================== VISTA: RECURSOS DE AYUDA ====================
elif opcion == "📞 Recursos de Ayuda":
    st.markdown('<div class="hero-title">Recursos y Líneas Gratuitas de Asistencia</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Canales oficiales de contención, asesoría legal y apoyo psicológico confidencial.</div>', unsafe_allow_html=True)
    
    if df_recursos.empty:
        st.info("No hay recursos registrados por el momento.")
    else:
        col1, col2 = st.columns(2, gap="medium")
        for i, (_, fila) in enumerate(df_recursos.iterrows()):
            col_actual = col1 if i % 2 == 0 else col2
            with col_actual:
                st.markdown(f"""
                <div class="card-pro" style="min-height: 165px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div class="resource-title">🏛️ {fila['Servicio']}</div>
                        <div class="schedule-info">🕒 <strong>Horario de atención:</strong> {fila['Horario']}</div>
                    </div>
                    <div>
                        <span class="contact-badge">📞 {fila['Contacto']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# ==================== VISTA: AUTOEVALUACIÓN RÁPIDA ====================
elif opcion == "📋 Autoevaluación Rápida":
    st.markdown('<div class="hero-title">Cuestionario de Autoevaluación</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Selecciona con honestidad si reconoces alguna de estas situaciones en tu relación actual o reciente.</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #F5F5DC; border-radius: 8px; padding: 0.85rem 1.1rem; margin-bottom: 1.25rem; font-size: 0.9rem; color: #475569;">
        ℹ️ <strong>Recordatorio confidencial:</strong> Este cuestionario se procesa solo en tu navegador durante esta sesión y no queda registrado en ningún servidor.
    </div>
    """, unsafe_allow_html=True)
    
    if not df_alertas.empty:
        with st.form("form_autoevaluacion", clear_on_submit=False):
            marcadas = []
            for idx, fila in df_alertas.iterrows():
                seleccion = st.checkbox(
                    f"**{fila['Conducta']}**: {fila['Descripción']}",
                    key=f"item_{idx}"
                )
                if seleccion:
                    marcadas.append(fila['Conducta'])
            
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("Analizar mis respuestas", use_container_width=True)
            
        if submit:
            st.markdown("---")
            total = len(marcadas)
            if total == 0:
                st.success("✅ **No has seleccionado señales de alerta de la lista.**\n\nLas relaciones saludables se fundamentan en la confianza mutua, la comunicación honesta y la libertad individual.")
            elif total <= 2:
                st.warning(f"⚠️ **Has marcado {total} conducta(s) de alerta:**\n\n" + 
                           "\n".join([f"- {c}" for c in marcadas]) + 
                           "\n\nTe sugerimos prestar atención y establecer límites claros. No dudes en consultar con amistades o profesionales de confianza.")
            else:
                st.error(f"🚨 **Has marcado {total} conductas de alerta significativas:**\n\n" + 
                         "\n".join([f"- {c}" for c in marcadas]) + 
                         "\n\nEstas dinámicas pueden poner en riesgo tu bienestar emocional o físico. Te recomendamos comunicarte a los **Recursos de Ayuda** de forma gratuita y confidencial.")
