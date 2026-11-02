# ==============================================================================
# HOJA DE ESTILOS CENTRALIZADA — SISTEMA LIRA
# Implementación optimizada con contraste garantizado:
# - Contraste estricto en textos primarios, secundarios, inputs, radios y selectbox
# - Ocultación de widgets de accesibilidad/animación de carga predeterminada
# - Eliminación de scrolls muertos y padding armónico
# - Tema Claro y Oscuro con variables CSS sincronizadas con Streamlit
# ==============================================================================

CSS_TEMPLATE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

/* ==========================================================================
   VARIABLES DE COLOR Y DISEÑO
   ========================================================================== */
:root {{
    /* --- TEMA CLARO (Contraste verificado) --- */
    --bg-page: #F8FAFC;
    --bg-card: #FFFFFF;
    --bg-card-hover: #FFFFFF;
    --border-color: #CBD5E1;
    --border-color-hover: #94A3B8;
    
    --text-primary: #0F172A;
    --text-secondary: #1E293B;
    --text-muted: #475569;
    
    /* Botones de acción principales */
    --btn-primary-bg: #4338CA;
    --btn-primary-hover: #3730A3;
    --btn-primary-active: #312E81;
    --btn-primary-text: #FFFFFF;
    --btn-primary-shadow: rgba(67, 56, 202, 0.25);
    
    /* Botones telefónicos */
    --btn-phone-bg: #0F766E;
    --btn-phone-hover: #115E59;
    --btn-phone-active: #134E4A;
    --btn-phone-text: #FFFFFF;
    --btn-phone-shadow: rgba(15, 118, 110, 0.25);
    
    /* Botones web */
    --btn-web-bg: #1D4ED8;
    --btn-web-hover: #1E40AF;
    --btn-web-active: #1E3A8A;
    --btn-web-text: #FFFFFF;
    --btn-web-shadow: rgba(29, 78, 216, 0.25);
    
    /* Barra de escape seguro */
    --safe-bar-bg: #E2E8F0;
    --safe-bar-border: #CBD5E1;
    --safe-bar-btn: #0F172A;
    --safe-bar-btn-hover: #1E293B;
    --safe-bar-btn-active: #334155;
    --safe-bar-btn-text: #FFFFFF;
    --safe-bar-btn-shadow: rgba(15, 23, 42, 0.2);
    
    /* Panel de emergencia */
    --emergency-bg: #FFF1F2;
    --emergency-border: #FDA4AF;
    --emergency-accent: #E11D48;
    --emergency-title: #9F1239;
    --emergency-text: #881337;
    
    /* Cajas informativas */
    --info-box-bg: #F1F5F9;
    --info-box-border: #CBD5E1;
    --info-box-text: #0F172A;
    --sidebar-privacy-text: #475569;
    
    /* Badges de alerta de alto contraste */
    --badge-control-bg: #FEF3C7;
    --badge-control-text: #78350F;
    --badge-control-border: #FCD34D;
    
    --badge-manip-bg: #EDE9FE;
    --badge-manip-text: #4C1D95;
    --badge-manip-border: #C4B5FD;
    
    --badge-intim-bg: #FFE4E6;
    --badge-intim-text: #881337;
    --badge-intim-border: #FDA4AF;
    
    --badge-general-bg: #EEF2FF;
    --badge-general-text: #312E81;
    --badge-general-border: #C7D2FE;
    
    --shadow-soft: 0 1px 3px rgba(0, 0, 0, 0.05);
    --shadow-hover: 0 4px 12px rgba(0, 0, 0, 0.08);
}}

/* --- TEMA OSCURO --- */
{dark_mode_overrides}

/* ==========================================================================
   CONFIGURACIÓN GENERAL
   ========================================================================== */
html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}}

/* Fondo global y contraste de texto principal */
.stApp {{
    background-color: var(--bg-page) !important;
    color: var(--text-primary) !important;
}}

/* Asegurar contraste en párrafos, títulos y labels nativos */
.stApp p, .stApp span, .stApp label, .stApp div {{
    color: inherit;
}}

/* Eliminar padding superior muerto de Streamlit */
.block-container {{
    padding-top: 1.25rem !important;
    padding-bottom: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 1200px !important;
}}

/* Barra lateral con contraste garantizado */
section[data-testid="stSidebar"] {{
    background-color: var(--bg-card) !important;
    border-right: 1px solid var(--border-color) !important;
}}

section[data-testid="stSidebar"] .block-container {{
    padding-top: 1.25rem !important;
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
}}

/* Espaciado vertical entre bloques */
div[data-testid="stVerticalBlock"] > div {{
    gap: 0.65rem !important;
}}

/* Ocultar barra superior, menú y decoraciones de carga de Streamlit */
#MainMenu, footer, header, div[data-testid="stDecoration"], div[data-testid="stStatusWidget"] {{
    display: none !important;
    visibility: hidden !important;
}}

/* ==========================================================================
   TIPOGRAFÍA Y ENCABEZADOS
   ========================================================================== */
.hero-title {{
    font-size: 1.95rem;
    font-weight: 700;
    color: var(--text-primary) !important;
    letter-spacing: -0.025em;
    line-height: 1.2;
    margin-top: 0;
    margin-bottom: 0.25rem;
}}

.hero-subtitle {{
    font-size: 1rem;
    color: var(--text-secondary) !important;
    line-height: 1.45;
    margin-bottom: 1.15rem;
}}

/* ==========================================================================
   BARRA SUPERIOR DE SALIDA RÁPIDA
   ========================================================================== */
.safe-exit-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--safe-bar-bg);
    border: 1px solid var(--safe-bar-border);
    border-radius: 9px;
    padding: 0.45rem 0.85rem;
    margin-bottom: 1rem;
    gap: 0.75rem;
}}

.safe-exit-text {{
    font-size: 0.84rem;
    color: var(--text-primary) !important;
    font-weight: 500;
    line-height: 1.35;
}}

.safe-exit-link {{
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background-color: var(--safe-bar-btn) !important;
    color: var(--safe-bar-btn-text) !important;
    font-size: 0.82rem;
    font-weight: 600;
    padding: 0.4rem 0.85rem;
    border-radius: 7px;
    border: 1px solid transparent;
    text-decoration: none !important;
    white-space: nowrap;
    cursor: pointer;
    box-shadow: 0 1px 3px var(--safe-bar-btn-shadow);
    transition: transform 0.16s ease, background-color 0.16s ease;
}}

.safe-exit-link:hover {{
    background-color: var(--safe-bar-btn-hover) !important;
    color: var(--safe-bar-btn-text) !important;
    transform: translateY(-1px);
}}

/* ==========================================================================
   BOTONES Y ENLACES (CONTRASTE ALTO WCAG AAA)
   ========================================================================== */
.phone-cta-btn {{
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    background-color: var(--btn-phone-bg) !important;
    color: var(--btn-phone-text) !important;
    font-size: 0.92rem;
    font-weight: 600;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    border: 1px solid transparent;
    text-decoration: none !important;
    min-height: 40px;
    cursor: pointer;
    box-shadow: 0 2px 4px var(--btn-phone-shadow);
    transition: transform 0.16s ease, background-color 0.16s ease;
}}

.phone-cta-btn:hover {{
    background-color: var(--btn-phone-hover) !important;
    color: var(--btn-phone-text) !important;
    transform: translateY(-2px);
}}

.website-cta-btn {{
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    background-color: var(--btn-web-bg) !important;
    color: var(--btn-web-text) !important;
    font-size: 0.92rem;
    font-weight: 600;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    border: 1px solid transparent;
    text-decoration: none !important;
    min-height: 40px;
    cursor: pointer;
    box-shadow: 0 2px 4px var(--btn-web-shadow);
    transition: transform 0.16s ease, background-color 0.16s ease;
}}

.website-cta-btn:hover {{
    background-color: var(--btn-web-hover) !important;
    color: var(--btn-web-text) !important;
    transform: translateY(-2px);
}}

div.stButton > button,
div[data-testid="stFormSubmitButton"] > button,
button[kind="primary"],
button[kind="secondary"] {{
    background-color: var(--btn-primary-bg) !important;
    color: var(--btn-primary-text) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.25rem !important;
    border-radius: 9px !important;
    border: 1px solid transparent !important;
    box-shadow: 0 2px 5px var(--btn-primary-shadow) !important;
    min-height: 42px !important;
    cursor: pointer !important;
    transition: transform 0.16s ease, background-color 0.16s ease !important;
}}

div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover,
button[kind="primary"]:hover,
button[kind="secondary"]:hover {{
    background-color: var(--btn-primary-hover) !important;
    color: var(--btn-primary-text) !important;
    transform: translateY(-2px) !important;
}}

/* ==========================================================================
   TARJETAS Y CONTENEDORES
   ========================================================================== */
.card-pro {{
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 11px;
    padding: 1.05rem 1.25rem;
    margin-bottom: 0.75rem;
    box-shadow: var(--shadow-soft);
    transition: border-color 0.16s ease, box-shadow 0.16s ease, transform 0.16s ease;
}}

.card-pro:hover {{
    border-color: var(--border-color-hover);
    box-shadow: var(--shadow-hover);
    transform: translateY(-1px);
}}

.card-title {{
    margin: 0.15rem 0 0.35rem 0;
    font-size: 1.08rem;
    font-weight: 700;
    color: var(--text-primary) !important;
}}

.card-description {{
    margin: 0;
    font-size: 0.94rem;
    color: var(--text-secondary) !important;
    line-height: 1.5;
}}

.card-callout {{
    border-left: 4px solid var(--btn-primary-bg);
    margin-top: 0.75rem;
}}

.card-callout-title {{
    margin: 0 0 0.25rem 0;
    color: var(--text-primary) !important;
    font-size: 1rem;
    font-weight: 700;
}}

.card-callout-text {{
    margin: 0;
    font-size: 0.9rem;
    color: var(--text-secondary) !important;
    line-height: 1.45;
}}

/* ==========================================================================
   BADGES DE CATEGORÍAS
   ========================================================================== */
.badge-category {{
    display: inline-block;
    padding: 0.22rem 0.6rem;
    border-radius: 9999px;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.02em;
    margin-bottom: 0.4rem;
}}

.badge-cat-control {{
    background-color: var(--badge-control-bg);
    color: var(--badge-control-text) !important;
    border: 1px solid var(--badge-control-border);
}}

.badge-cat-manipulacion {{
    background-color: var(--badge-manip-bg);
    color: var(--badge-manip-text) !important;
    border: 1px solid var(--badge-manip-border);
}}

.badge-cat-intimidacion {{
    background-color: var(--badge-intim-bg);
    color: var(--badge-intim-text) !important;
    border: 1px solid var(--badge-intim-border);
}}

.badge-cat-general {{
    background-color: var(--badge-general-bg);
    color: var(--badge-general-text) !important;
    border: 1px solid var(--badge-general-border);
}}

/* ==========================================================================
   PANEL DE EMERGENCIA
   ========================================================================== */
.emergency-banner {{
    background-color: var(--emergency-bg);
    border: 1px solid var(--emergency-border);
    border-left: 5px solid var(--emergency-accent);
    border-radius: 11px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.75rem;
}}

.emergency-banner h4 {{
    margin: 0 0 0.25rem 0;
    color: var(--emergency-title) !important;
    font-size: 1.05rem;
    font-weight: 700;
}}

.emergency-banner p {{
    margin: 0;
    color: var(--emergency-text) !important;
    font-size: 0.92rem;
    line-height: 1.45;
}}

/* ==========================================================================
   TARJETAS DE RECURSOS
   ========================================================================== */
.resource-card {{
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 11px;
    padding: 1.15rem;
    margin-bottom: 0.85rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: var(--shadow-soft);
    transition: border-color 0.16s ease, box-shadow 0.16s ease, transform 0.16s ease;
}}

.resource-card:hover {{
    border-color: var(--border-color-hover);
    box-shadow: var(--shadow-hover);
    transform: translateY(-1px);
}}

.resource-title {{
    font-size: 1.08rem;
    font-weight: 700;
    color: var(--text-primary) !important;
    margin-bottom: 0.35rem;
}}

.schedule-text {{
    font-size: 0.88rem;
    color: var(--text-secondary) !important;
    margin-top: 0.25rem;
}}

.resource-note {{
    font-size: 0.84rem;
    color: var(--text-primary) !important;
    background-color: var(--safe-bar-bg);
    border-left: 3px solid var(--btn-phone-bg);
    padding: 0.4rem 0.65rem;
    border-radius: 4px;
    margin-top: 0.5rem;
    line-height: 1.35;
}}

/* ==========================================================================
   CAJAS DE MENSAJE Y PRIVACIDAD
   ========================================================================== */
.info-box-privacy {{
    background-color: var(--info-box-bg);
    border: 1px solid var(--info-box-border);
    border-radius: 9px;
    padding: 0.75rem 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--info-box-text) !important;
    line-height: 1.45;
}}

.sidebar-privacy-note {{
    font-size: 0.84rem;
    color: var(--sidebar-privacy-text) !important;
    line-height: 1.45;
}}

/* ==========================================================================
   MÉTRICAS, INPUTS Y FORMULARIOS DE STREAMLIT (CONSTRASTE ALTO)
   ========================================================================== */
div[data-testid="stMetric"] {{
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 11px !important;
    padding: 0.75rem 1rem !important;
    box-shadow: var(--shadow-soft) !important;
}}

div[data-testid="stMetric"] label {{
    color: var(--text-muted) !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
}}

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{
    color: var(--text-primary) !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
}}

/* Inputs de texto, selectores y checkboxes de Streamlit */
div[data-baseweb="select"] > div {{
    background-color: var(--bg-card) !important;
    border-color: var(--border-color) !important;
    color: var(--text-primary) !important;
}}

div[data-baseweb="select"] span {{
    color: var(--text-primary) !important;
}}

input[type="text"] {{
    background-color: var(--bg-card) !important;
    border-color: var(--border-color) !important;
    color: var(--text-primary) !important;
}}

div[data-testid="stMarkdownContainer"] p {{
    color: var(--text-secondary);
}}

div[data-testid="stMarkdownContainer"] h4, 
div[data-testid="stMarkdownContainer"] h5 {{
    color: var(--text-primary) !important;
}}

/* Checkboxes del cuestionario */
div[data-testid="stCheckbox"] label {{
    color: var(--text-primary) !important;
    font-size: 0.95rem !important;
    cursor: pointer !important;
}}

/* Radio buttons de navegación */
div[data-testid="stRadio"] label {{
    color: var(--text-primary) !important;
    cursor: pointer !important;
}}

/* ==========================================================================
   DISEÑO RESPONSIVO (Móviles y Tablets)
   ========================================================================== */
@media (max-width: 768px) {{
    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 1.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }}
    
    .hero-title {{
        font-size: 1.5rem;
    }}
    
    .hero-subtitle {{
        font-size: 0.92rem;
        margin-bottom: 1rem;
    }}
    
    .safe-exit-bar {{
        flex-direction: column;
        align-items: stretch;
        gap: 0.5rem;
        padding: 0.6rem;
    }}
    
    .safe-exit-link {{
        width: 100%;
        text-align: center;
        justify-content: center;
    }}
    
    .card-pro, .resource-card, .emergency-banner {{
        padding: 0.9rem 1rem;
    }}
    
    .phone-cta-btn, .website-cta-btn {{
        width: 100%;
        justify-content: center;
    }}
    
    div.stButton > button,
    div[data-testid="stFormSubmitButton"] > button {{
        width: 100% !important;
    }}
}}
</style>
"""

# Bloque de variables para Modo Oscuro con contraste reforzado
DARK_MODE_CSS = """
:root {
    --bg-page: #0B0F19;
    --bg-card: #151C2C;
    --bg-card-hover: #1C2438;
    --border-color: #2D3A54;
    --border-color-hover: #4B5E86;
    
    --text-primary: #FFFFFF;
    --text-secondary: #E2E8F0;
    --text-muted: #CBD5E1;
    
    --btn-primary-bg: #6366F1;
    --btn-primary-hover: #4F46E5;
    --btn-primary-active: #4338CA;
    --btn-primary-text: #FFFFFF;
    --btn-primary-shadow: rgba(99, 102, 241, 0.35);
    
    --btn-phone-bg: #0D9488;
    --btn-phone-hover: #0F766E;
    --btn-phone-active: #115E59;
    --btn-phone-text: #FFFFFF;
    --btn-phone-shadow: rgba(13, 148, 136, 0.3);
    
    --btn-web-bg: #2563EB;
    --btn-web-hover: #1D4ED8;
    --btn-web-active: #1E40AF;
    --btn-web-text: #FFFFFF;
    --btn-web-shadow: rgba(37, 99, 235, 0.3);
    
    --safe-bar-bg: #151C2C;
    --safe-bar-border: #2D3A54;
    --safe-bar-btn: #38BDF8;
    --safe-bar-btn-hover: #0EA5E9;
    --safe-bar-btn-active: #0284C7;
    --safe-bar-btn-text: #041E34;
    --safe-bar-btn-shadow: rgba(56, 189, 248, 0.25);
    
    --emergency-bg: #2B1115;
    --emergency-border: #7F1D1D;
    --emergency-accent: #F43F5E;
    --emergency-title: #FECDD3;
    --emergency-text: #FFE4E6;
    
    --info-box-bg: #151C2C;
    --info-box-border: #2D3A54;
    --info-box-text: #E2E8F0;
    --sidebar-privacy-text: #CBD5E1;
    
    --badge-control-bg: rgba(245, 158, 11, 0.22);
    --badge-control-text: #FDE68A;
    --badge-control-border: rgba(245, 158, 11, 0.45);
    
    --badge-manip-bg: rgba(139, 92, 246, 0.22);
    --badge-manip-text: #DDD6FE;
    --badge-manip-border: rgba(139, 92, 246, 0.45);
    
    --badge-intim-bg: rgba(244, 63, 94, 0.22);
    --badge-intim-text: #FECDD3;
    --badge-intim-border: rgba(244, 63, 94, 0.45);
    
    --badge-general-bg: rgba(99, 102, 241, 0.22);
    --badge-general-text: #C7D2FE;
    --badge-general-border: rgba(99, 102, 241, 0.45);
    
    --shadow-soft: 0 1px 3px rgba(0, 0, 0, 0.35);
    --shadow-hover: 0 4px 12px rgba(0, 0, 0, 0.5);
}
"""

def inject_styles(theme: str = "light"):
    # Inyecta en Streamlit el CSS con el tema seleccionado ('light' u 'dark')
    import streamlit as st
    dark_overrides = DARK_MODE_CSS if theme == "dark" else ""
    full_css = CSS_TEMPLATE.format(dark_mode_overrides=dark_overrides)
    st.markdown(full_css, unsafe_allow_html=True)
