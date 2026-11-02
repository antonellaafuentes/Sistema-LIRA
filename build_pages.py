import os
import json
import shutil
from jinja2 import Environment, FileSystemLoader
from src.services.data_service import load_alerts_data, load_resources_data
from src.ui.components import get_category_badge_class, parse_contact_action

def build_static_site():
    OUTPUT_DIR = "dist"
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 1. Copiar assets estaticos (CSS, JS)
    shutil.copytree("src/static", os.path.join(OUTPUT_DIR, "static"))
    
    # Archivo .nojekyll para GitHub Pages
    with open(os.path.join(OUTPUT_DIR, ".nojekyll"), "w") as f:
        f.write("")
        
    env = Environment(loader=FileSystemLoader("src/templates"))
    
    # Cargar datos
    df_alerts = load_alerts_data()
    df_resources = load_resources_data()
    
    alerts_list = []
    for _, row in df_alerts.iterrows():
        item = dict(row)
        item["badge_class"] = get_category_badge_class(item.get("Categoría", ""))
        alerts_list.append(item)
        
    categories = sorted(list(df_alerts["Categoría"].unique()))
    
    resources_list = []
    for _, row in df_resources.iterrows():
        item = dict(row)
        item["action"] = parse_contact_action(item.get("Contacto", ""))
        resources_list.append(item)
        
    grouped_alerts = {}
    for cat in categories:
        grouped_alerts[cat] = [a for a in alerts_list if a.get("Categoría") == cat]
        
    # Helper para ajustar rutas a relativas en GitHub Pages (ej: ./static/...)
    def fix_paths(html: str) -> str:
        # Reemplazar rutas de assets
        html = html.replace('href="/static/', 'href="./static/')
        html = html.replace('src="/static/', 'src="./static/')
        # Reemplazar navegacion interna
        html = html.replace('href="/"', 'href="./index.html"')
        html = html.replace('href="/alertas"', 'href="./alertas.html"')
        html = html.replace('href="/recursos"', 'href="./recursos.html"')
        html = html.replace('href="/autoevaluacion"', 'href="./autoevaluacion.html"')
        return html

    # 1. index.html (Home)
    t_home = env.get_template("home.html")
    html_home = t_home.render(
        active_page="home",
        total_alerts=len(df_alerts),
        total_resources=len(df_resources)
    )
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(fix_paths(html_home))

    # 2. alertas.html
    # Para GitHub Pages, agregamos filtrado instantáneo en cliente (JS) para selector y buscador
    t_alerts = env.get_template("alerts.html")
    html_alerts = t_alerts.render(
        active_page="alerts",
        alerts=alerts_list,
        categories=categories,
        selected_category="Todas las categorías",
        search_query=""
    )
    # Reemplazar el form submit por JS interactivo sin recarga de servidor
    html_alerts = html_alerts.replace('onchange="this.form.submit()"', 'id="filter-category" onchange="filterCards()"')
    html_alerts = html_alerts.replace('<form method="get" action="/alertas" class="filter-bar">', '<div class="filter-bar">')
    html_alerts = html_alerts.replace('</form>', '</div>')
    html_alerts = html_alerts.replace('name="q"', 'id="filter-query" oninput="filterCards()"')
    html_alerts = html_alerts.replace('<button type="submit" class="btn-cta btn-primary" style="margin-top: 0; padding: 0.6rem 1rem;">\n    Buscar\n  </button>', '<button type="button" class="btn-cta btn-primary" style="margin-top: 0; padding: 0.6rem 1rem;" onclick="filterCards()">Buscar</button>')
    
    # Inyectar script de filtrado en cliente
    filter_script = """
    <script>
      function filterCards() {
        const cat = document.getElementById('filter-category').value;
        const q = document.getElementById('filter-query').value.toLowerCase().trim();
        const cards = document.querySelectorAll('.card-pro');
        let count = 0;
        cards.forEach(card => {
          const badge = card.querySelector('.badge-category');
          if (!badge) return; // empty state card
          const cardCat = badge.textContent.trim();
          const title = (card.querySelector('.card-title') || {}).textContent || '';
          const desc = (card.querySelector('.card-description') || {}).textContent || '';
          const text = (title + ' ' + desc).toLowerCase();
          
          const matchCat = (cat === 'Todas las categorías' || cardCat === cat);
          const matchQuery = (!q || text.includes(q));
          
          if (matchCat && matchQuery) {
            card.style.display = 'block';
            count++;
          } else {
            card.style.display = 'none';
          }
        });
        const countEl = document.getElementById('signals-count');
        if (countEl) countEl.textContent = count;
      }
    </script>
    """
    html_alerts = html_alerts.replace('Mostrando <strong>{{ alerts|length }}</strong>', 'Mostrando <strong id="signals-count">' + str(len(alerts_list)) + '</strong>')
    html_alerts = html_alerts.replace('</body>', filter_script + '</body>')
    with open(os.path.join(OUTPUT_DIR, "alertas.html"), "w", encoding="utf-8") as f:
        f.write(fix_paths(html_alerts))

    # 3. recursos.html
    t_resources = env.get_template("resources.html")
    html_resources = t_resources.render(
        active_page="resources",
        resources=resources_list
    )
    with open(os.path.join(OUTPUT_DIR, "recursos.html"), "w", encoding="utf-8") as f:
        f.write(fix_paths(html_resources))

    # 4. autoevaluacion.html (Con evaluación 100% interactiva en navegador)
    t_quiz = env.get_template("quiz.html")
    html_quiz = t_quiz.render(
        active_page="quiz",
        grouped_alerts=grouped_alerts,
        selected_conductas=[],
        evaluated=False,
        total_checked=0
    )
    # Reemplazar el submit de backend por cálculo interactivo en cliente
    html_quiz = html_quiz.replace('<form method="post" action="/autoevaluacion">', '<form id="quiz-form" onsubmit="event.preventDefault(); evaluateQuiz();">')
    
    quiz_script = """
    <div id="quiz-result-container"></div>
    <script>
      function evaluateQuiz() {
        const checked = Array.from(document.querySelectorAll('input[name="conductas"]:checked')).map(cb => cb.value);
        const total = checked.length;
        const container = document.getElementById('quiz-result-container');
        
        let html = '';
        if (total === 0) {
          html = `
            <div class="quiz-result success">
              <strong>✅ No has seleccionado señales de alerta de la lista.</strong><br>
              Las relaciones basadas en el respeto, el diálogo y la libertad recíproca son el pilar de un vínculo sano.
            </div>`;
        } else if (total <= 2) {
          const items = checked.map(c => `<li>${c}</li>`).join('');
          html = `
            <div class="quiz-result warning">
              <strong>⚠️ Has identificado ${total} conducta(s) de riesgo:</strong>
              <ul style="margin: 0.5rem 0 0.5rem 1.2rem;">${items}</ul>
              Te sugerimos reflexionar sobre estos límites y conversarlo en un entorno seguro. Reconocer conductas a tiempo es clave para evitar dinámicas mayores.
            </div>`;
        } else {
          const items = checked.map(c => `<li>${c}</li>`).join('');
          html = `
            <div class="quiz-result danger">
              <strong>🚨 Has identificado ${total} conductas de alerta significativas:</strong>
              <ul style="margin: 0.5rem 0 0.5rem 1.2rem;">${items}</ul>
              Estas dinámicas atentan contra tu integridad y bienestar. Te recomendamos acudir a la sección de <strong><a href="./recursos.html" style="color: inherit; text-decoration: underline;">Recursos de Ayuda</a></strong> para comunicarte gratuitamente con profesionales que pueden orientarte.
            </div>`;
        }
        container.innerHTML = html;
        container.scrollIntoView({ behavior: 'smooth' });
      }
    </script>
    """
    html_quiz = html_quiz.replace('</form>', '</form>' + quiz_script)
    with open(os.path.join(OUTPUT_DIR, "autoevaluacion.html"), "w", encoding="utf-8") as f:
        f.write(fix_paths(html_quiz))

    print(f"Sitio estatico generado exitosamente en /{OUTPUT_DIR}")

if __name__ == "__main__":
    build_static_site()
