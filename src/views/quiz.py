import streamlit as st
import pandas as pd

def render_quiz_view(df_alerts: pd.DataFrame):
    # Pantalla de autoevaluación: formulario confidencial para reflexionar sobre dinámicas de pareja
    st.markdown('<div class="hero-title">Cuestionario de Autoevaluación</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Selecciona con tranquilidad si has presenciado o experimentado alguna de estas conductas en una relación.</div>',
        unsafe_allow_html=True
    )
    
    # Mensaje de privacidad con estilo centralizado en styles.py
    st.markdown("""
    <div class="info-box-privacy">
        🔒 <strong>Privacidad absoluta:</strong> Esta autoevaluación es orientativa y temporal. Tus respuestas se procesan únicamente en tu navegador y se borran al cerrar la pestaña.
    </div>
    """, unsafe_allow_html=True)
    
    if df_alerts.empty:
        st.info("No hay datos disponibles para la autoevaluación.")
        return
        
    categorias = sorted(list(df_alerts["Categoría"].unique()))
    
    with st.form("form_autoevaluacion", clear_on_submit=False):
        marcadas = []
        
        for cat in categorias:
            st.markdown(f"#### 📌 {cat}")
            df_cat = df_alerts[df_alerts["Categoría"] == cat]
            
            for idx, fila in df_cat.iterrows():
                seleccion = st.checkbox(
                    f"**{fila['Conducta']}**: {fila['Descripción']}",
                    key=f"item_{idx}"
                )
                if seleccion:
                    marcadas.append(f"{fila['Conducta']} ({fila['Categoría']})")
            
            st.write("")
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_btn1, col_btn2 = st.columns([1, 3])
        with col_btn1:
            submit = st.form_submit_button("Analizar respuestas", use_container_width=True)
            
    if submit:
        st.markdown("---")
        total = len(marcadas)
        if total == 0:
            st.success(
                "✅ **No has seleccionado señales de alerta de la lista.**\n\n"
                "Las relaciones basadas en el respeto, el diálogo y la libertad recíproca son el pilar de un vínculo sano."
            )
        elif total <= 2:
            st.warning(
                f"⚠️ **Has identificado {total} conducta(s) de riesgo:**\n\n" +
                "\n".join([f"- {c}" for c in marcadas]) +
                "\n\nTe sugerimos reflexionar sobre estos límites y conversarlo en un entorno seguro. Reconocer conductas a tiempo es clave para evitar dinámicas mayores."
            )
        else:
            st.error(
                f"🚨 **Has identificado {total} conductas de alerta significativas:**\n\n" +
                "\n".join([f"- {c}" for c in marcadas]) +
                "\n\nEstas dinámicas atentan contra tu integridad y bienestar. Te recomendamos acudir a la pestaña de **Recursos de Ayuda** para comunicarte gratuitamente con profesionales que pueden orientarte."
            )
