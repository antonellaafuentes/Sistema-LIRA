import re
import streamlit as st
from src.config import SAFE_EXIT_URL

def render_safe_exit_bar():
    # Barra superior de navegación segura con botón discreto de escape
    st.markdown(f"""
    <div class="safe-exit-bar">
        <span class="safe-exit-text">
            🔒 Navegación confidencial • Tus datos no se guardan en ningún servidor
        </span>
        <a href="{SAFE_EXIT_URL}" class="safe-exit-link" target="_self" title="Cierra esta ventana y abre Google de inmediato">
            ✕ Salida Rápida (Cerrar)
        </a>
    </div>
    """, unsafe_allow_html=True)

def get_category_badge_class(category: str) -> str:
    # Devuelve la clase de color según la categoría de la alerta
    cat_lower = category.lower()
    if "control" in cat_lower or "aislamiento" in cat_lower:
        return "badge-cat-control"
    elif "manipulaci" in cat_lower or "agresi" in cat_lower:
        return "badge-cat-manipulacion"
    elif "intimidaci" in cat_lower or "explosivo" in cat_lower:
        return "badge-cat-intimidacion"
    return "badge-cat-general"

def render_alert_card(conducta: str, categoria: str, descripcion: str):
    # Dibuja la tarjeta de una conducta sin ningún estilo inline
    badge_class = get_category_badge_class(categoria)
    st.markdown(f"""
    <div class="card-pro">
        <span class="badge-category {badge_class}">{categoria}</span>
        <h3 class="card-title">{conducta}</h3>
        <p class="card-description">{descripcion}</p>
    </div>
    """, unsafe_allow_html=True)

def parse_contact_action(contacto: str):
    # Analiza el tipo de contacto (página web o número telefónico) y crea el enlace correcto
    contacto_clean = str(contacto).strip()
    
    # 1. Si es un enlace de página web
    if contacto_clean.startswith("http://") or contacto_clean.startswith("https://") or "www." in contacto_clean:
        url = contacto_clean if contacto_clean.startswith("http") else f"https://{contacto_clean}"
        return {
            "url": url,
            "label": "🌐 Visitar sitio web oficial",
            "btn_class": "website-cta-btn",
            "target": "_blank",
            "rel": 'rel="noopener noreferrer"'
        }
    
    # 2. Si es un número telefónico (móvil, fijo o de emergencia)
    if contacto_clean.startswith("+"):
        # Mantiene el signo + para llamadas internacionales
        digits = "+" + re.sub(r"\D", "", contacto_clean)
    else:
        digits = re.sub(r"\D", "", contacto_clean)
        
    tel_url = f"tel:{digits}" if digits else "#"
    return {
        "url": tel_url,
        "label": f"📞 Llamar: {contacto_clean}",
        "btn_class": "phone-cta-btn",
        "target": "_self",
        "rel": ""
    }

def render_resource_card(servicio: str, contacto: str, horario: str, notas: str = ""):
    # Dibuja la tarjeta del servicio con botón funcional (tel: o web) y nota si existe
    action = parse_contact_action(contacto)
    
    nota_html = ""
    if notas and str(notas).strip() and str(notas).strip() != "nan":
        nota_html = f'<div class="resource-note">ℹ️ {notas.strip()}</div>'
    
    st.markdown(f"""
    <div class="resource-card">
        <div>
            <div class="resource-title">🏛️ {servicio}</div>
            <div class="schedule-text">🕒 <strong>Atención:</strong> {horario}</div>
            {nota_html}
        </div>
        <div>
            <a href="{action['url']}" class="{action['btn_class']}" target="{action['target']}" {action['rel']}>
                {action['label']}
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
