# ==============================================================================
# HOJA DE ESTILOS CENTRALIZADA — SISTEMA LIRA
# Implementación optimizada Impeccable:
# - Ajuste de espaciados y eliminación de scrollbars muertos
# - Padding compacto y armónico en contenedores y sidebar
# - UI 100% responsiva con microinteracciones táctiles
# ==============================================================================

CSS_TEMPLATE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

/* ==========================================================================
   VARIABLES DE COLOR Y DISEÑO
   ========================================================================== */
:root {{
    /* --- TEMA CLARO (Por defecto) --- */
    --bg-page: #F8FAFC;
    --bg-card: #FFFFFF;
    --bg-card-hover: #FFFFFF;
    --border-color: #E2E8F0;
    --border-color-hover: #CBD5E1;
    
    --text-primary: #0F172A;
    --text-secondary: #334155;
    --text-muted: #64748B;
    
    /* Botones de acción principales (Índigo) */
    --btn-primary-bg: #4338CA;
    --btn-primary-hover: #3730A3;
    --btn-primary-active: #312E81;
    --btn-primary-text: #FFFFFF;
    --btn-primary-shadow: rgba(67, 56, 202, 0.2);
    
    /* Botones telefónicos (Verde Esmeralda) */
    --btn-phone-bg: #0F766E;
    --btn-phone-hover: #115E59;
    --btn-phone-active: #134E4A;
    --btn-phone-text: #FFFFFF;
    --btn-phone-shadow: rgba(15, 118, 110, 0.2);
    
    /* Botones de sitio web (Azul Océano) */
    --btn-web-bg: #1D4ED8;
    --btn-web-hover: #1E40AF;
    --btn-web-active: #1E3A8A;
    --btn-web-text: #FFFFFF;
    --btn-web-shadow: rgba(29, 78, 216, 0.2);
    
    /* Botón de escape seguro superior */
    --safe-bar-bg: #F1F5F9;
    --safe-bar-border: #E2E8F0;
    --safe-bar-btn: #0F172A;
    --safe-bar-btn-hover: #1E293B;
    --safe-bar-btn-active: #334155;
    --safe-bar-btn-text: #FFFFFF;
    --safe-bar-btn-shadow: rgba(15, 23, 42, 0.15);
    
    /* Panel de emergencia */
    --emergency-bg: #FFF1F2;
    --emergency-border: #FECDD3;
    --emergency-accent: #E11D48;
    --emergency-title: #9F1239;
    --emergency-text: #881337;
    
    /* Cajas informativas */
    --info-box-bg: #F8FAFC;
    --info-box-border: #E2E8F0;
    --info-box-text: #334155;
    --sidebar-privacy-text: #64748B;
    
    /* Badges de alerta */
    --badge-control-bg: #FEF3C7;
    --badge-control-text: #92400E;
    --badge-control-border: #FDE68A;
    
    --badge-manip-bg: #EDE9FE;
    --badge-manip-text: #5B21B6;
    --badge-manip-border: #DDD6FE;
    
    --badge-intim-bg: #FFE4E6;
    --badge-intim-text: #9F1239;
    --badge-intim-border: #FECDD3;
    
    --badge-general-bg: #EEF2FF;
    --badge-general-text: #4338CA;
    --badge-general-border: #E0E7FF;
    
    --shadow-soft: 0 1px 3px rgba(0, 0, 0, 0.04);
    --shadow-hover: 0 4px 12px rgba(0, 0, 0, 0.07);
}}

/* --- TEMA OSCURO --- */
{dark_mode_overrides}

/* ==========================================================================
   CONFIGURACIÓN GENERAL Y ELIMINACIÓN DE SCROLLS MUERTOS
   ========================================================================== */
html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}}

/* Fondo global y control de desbordamiento */
.stApp {{
    background-color: var(--bg-page) !important;
    color: var(--text-primary) !important;
}}

/* Eliminar padding superior muerto de Streamlit (antes 6rem) */
.block-container {{
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 1200px !important;
}}

/* Reducir espaciado muerto en la barra lateral */
section[data-testid="stSidebar"] {{
    background-color: var(--bg-card) !important;
    border-right: 1px solid var(--border-color) !important;
}}

section[data-testid="stSidebar"] .block-container {{
    padding-top: 1.5rem !important;
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
}}

/* Reducir espacio entre widgets verticales de Streamlit (antes 1rem por defecto) */
div[data-testid="stVerticalBlock"] > div {{
    gap: 0.65rem !important;
}}

/* Ocultar elementos predeterminados que generan scroll muerto */
#MainMenu {{display: none !important;}}
footer {{display: none !important;}}
header {{display: none !important;}}

/* ==========================================================================
   TIPOGRAFÍA Y ENCABEZADOS
   ========================================================================== */
.hero-title {{
    font-size: 1.95rem;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: -0.025em;
    line-height: 1.2;
    margin-top: 0;
    margin-bottom: 0.25rem;
}}

.hero-subtitle {{
    font-size: 1rem;
    color: var(--text-secondary);
    line-height: 1.45;
    margin-bottom: 1.15rem;
}}

/* ==========================================================================
   BARRA SUPERIOR DE SALIDA RÁPIDA (COMPACTA)
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
    font-size: 0.82rem;
    color: var(--text-muted);
    line-height: 1.35;
}}

.safe-exit-link {{
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background-color: var(--safe-bar-btn) !important;
    color: var(--safe-bar-btn-text) !important;
    font-size: 0.8rem;
    font-weight: 600;
    padding: 0.38rem 0.85rem;
    border-radius: 7px;
    border: 1px solid transparent;
    text-decoration: none !important;
    white-space: nowrap;
    cursor: pointer;
    box-shadow: 0 1px 3px var(--safe-bar-btn-shadow);
    transition: transform 0.16s ease, background-color 0.16s ease, box-shadow 0.16s ease;
}}

.safe-exit-link:hover {{
    background-color: var(--safe-bar-btn-hover) !important;
    color: var(--safe-bar-btn-text) !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 10px var(--safe-bar-btn-shadow);
}}

.safe-exit-link:active {{
    background-color: var(--safe-bar-btn-active) !important;
    transform: translateY(0);
}}

/* ==========================================================================
   BOTONES Y ENLACES
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
    transition: transform 0.16s ease, background-color 0.16s ease, box-shadow 0.16s ease;
}}

.phone-cta-btn:hover {{
    background-color: var(--btn-phone-hover) !important;
    color: var(--btn-phone-text) !important;
    transform: translateY(-2px);
    box-shadow: 0 5px 12px var(--btn-phone-shadow);
}}

.phone-cta-btn:active {{
    background-color: var(--btn-phone-active) !important;
    transform: translateY(0);
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
    transition: transform 0.16s ease, background-color 0.16s ease, box-shadow 0.16s ease;
}}

.website-cta-btn:hover {{
    background-color: var(--btn-web-hover) !important;
    color: var(--btn-web-text) !important;
    transform: translateY(-2px);
    box-shadow: 0 5px 12px var(--btn-web-shadow);
}}

.website-cta-btn:active {{
    background-color: var(--btn-web-active) !important;
    transform: translateY(0);
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
    transition: transform 0.16s ease, background-color 0.16s ease, box-shadow 0.16s ease !important;
}}

div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover,
button[kind="primary"]:hover,
button[kind="secondary"]:hover {{
    background-color: var(--btn-primary-hover) !important;
    color: var(--btn-primary-text) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 14px var(--btn-primary-shadow) !important;
}}

div.stButton > button:active,
div[data-testid="stFormSubmitButton"] > button:active,
button[kind="primary"]:active,
button[kind="secondary"]:active {{
    background-color: var(--btn-primary-active) !important;
    transform: translateY(0) !important;
}}

/* ==========================================================================
   TARJETAS Y CONTENEDORES
   ========================================================================== */
.card-pro {{
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 11px;
    padding: 1rem 1.2rem;
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
    font-weight: 600;
    color: var(--text-primary);
}}

.card-description {{
    margin: 0;
    font-size: 0.92rem;
    color: var(--text-secondary);
    line-height: 1.5;
}}

.card-callout {{
    border-left: 4px solid var(--btn-primary-bg);
    margin-top: 0.75rem;
}}

.card-callout-title {{
    margin: 0 0 0.25rem 0;
    color: var(--text-primary);
    font-size: 1rem;
    font-weight: 600;
}}

.card-callout-text {{
    margin: 0;
    font-size: 0.88rem;
    color: var(--text-secondary);
    line-height: 1.4;
}}

/* ==========================================================================
   ETIQUETAS SEMÁNTICAS (BADGES DE CATEGORÍAS)
   ========================================================================== */
.badge-category {{
    display: inline-block;
    padding: 0.2rem 0.55rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    margin-bottom: 0.35rem;
}}

.badge-cat-control {{
    background-color: var(--badge-control-bg);
    color: var(--badge-control-text);
    border: 1px solid var(--badge-control-border);
}}

.badge-cat-manipulacion {{
    background-color: var(--badge-manip-bg);
    color: var(--badge-manip-text);
    border: 1px solid var(--badge-manip-border);
}}

.badge-cat-intimidacion {{
    background-color: var(--badge-intim-bg);
    color: var(--badge-intim-text);
    border: 1px solid var(--badge-intim-border);
}}

.badge-cat-general {{
    background-color: var(--badge-general-bg);
    color: var(--badge-general-text);
    border: 1px solid var(--badge-general-border);
}}

/* ==========================================================================
   PANEL DE EMERGENCIA INMEDIATA
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
    color: var(--emergency-title);
    font-size: 1.05rem;
    font-weight: 700;
}}

.emergency-banner p {{
    margin: 0;
    color: var(--emergency-text);
    font-size: 0.9rem;
    line-height: 1.4;
}}

/* ==========================================================================
   TARJETAS DE RECURSOS DE AYUDA (ALTURA DINÁMICA SIN SCROLL MUERTO)
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
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.35rem;
}}

.schedule-text {{
    font-size: 0.86rem;
    color: var(--text-muted);
    margin-top: 0.25rem;
}}

.resource-note {{
    font-size: 0.82rem;
    color: var(--text-secondary);
    background-color: var(--safe-bar-bg);
    border-left: 3px solid var(--btn-phone-bg);
    padding: 0.35rem 0.6rem;
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
    font-size: 0.88rem;
    color: var(--info-box-text);
    line-height: 1.4;
}}

.sidebar-privacy-note {{
    font-size: 0.82rem;
    color: var(--sidebar-privacy-text);
    line-height: 1.4;
}}

/* ==========================================================================
   MÉTRICAS Y INPUTS COMPACTOS
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
    font-size: 0.84rem !important;
}}

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{
    color: var(--text-primary) !important;
    font-size: 1.6rem !important;
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

# Bloque de variables para Modo Oscuro
DARK_MODE_CSS = """
:root {
    --bg-page: #0B0F19;
    --bg-card: #151C2C;
    --bg-card-hover: #1C2438;
    --border-color: #242F48;
    --border-color-hover: #374668;
    
    --text-primary: #F8FAFC;
    --text-secondary: #CBD5E1;
    --text-muted: #94A3B8;
    
    --btn-primary-bg: #6366F1;
    --btn-primary-hover: #4F46E5;
    --btn-primary-active: #4338CA;
    --btn-primary-text: #FFFFFF;
    --btn-primary-shadow: rgba(99, 102, 241, 0.3);
    
    --btn-phone-bg: #14B8A6;
    --btn-phone-hover: #0D9488;
    --btn-phone-active: #0F766E;
    --btn-phone-text: #042F2E;
    --btn-phone-shadow: rgba(20, 184, 166, 0.25);
    
    --btn-web-bg: #3B82F6;
    --btn-web-hover: #2563EB;
    --btn-web-active: #1D4ED8;
    --btn-web-text: #FFFFFF;
    --btn-web-shadow: rgba(59, 130, 246, 0.25);
    
    --safe-bar-bg: #151C2C;
    --safe-bar-border: #242F48;
    --safe-bar-btn: #38BDF8;
    --safe-bar-btn-hover: #0EA5E9;
    --safe-bar-btn-active: #0284C7;
    --safe-bar-btn-text: #082F49;
    --safe-bar-btn-shadow: rgba(56, 189, 248, 0.25);
    
    --emergency-bg: #2B1115;
    --emergency-border: #6B1D27;
    --emergency-accent: #F43F5E;
    --emergency-title: #FDA4AF;
    --emergency-text: #FECDD3;
    
    --info-box-bg: #151C2C;
    --info-box-border: #242F48;
    --info-box-text: #CBD5E1;
    --sidebar-privacy-text: #94A3B8;
    
    --badge-control-bg: rgba(245, 158, 11, 0.16);
    --badge-control-text: #FBBF24;
    --badge-control-border: rgba(245, 158, 11, 0.35);
    
    --badge-manip-bg: rgba(139, 92, 246, 0.16);
    --badge-manip-text: #C4B5FD;
    --badge-manip-border: rgba(139, 92, 246, 0.35);
    
    --badge-intim-bg: rgba(244, 63, 94, 0.16);
    --badge-intim-text: #FDA4AF;
    --badge-intim-border: rgba(244, 63, 94, 0.35);
    
    --badge-general-bg: rgba(99, 102, 241, 0.16);
    --badge-general-text: #A5B4FC;
    --badge-general-border: rgba(99, 102, 241, 0.35);
    
    --shadow-soft: 0 1px 3px rgba(0, 0, 0, 0.3);
    --shadow-hover: 0 4px 12px rgba(0, 0, 0, 0.45);
}
"""

def inject_styles(theme: str = "light"):
    # Inyecta en Streamlit el CSS con el tema seleccionado ('light' u 'dark')
    import streamlit as st
    dark_overrides = DARK_MODE_CSS if theme == "dark" else ""
    full_css = CSS_TEMPLATE.format(dark_mode_overrides=dark_overrides)
    st.markdown(full_css, unsafe_allow_html=True)
