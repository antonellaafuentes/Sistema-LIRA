import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from src.config import APP_TITLE
from src.services.data_service import load_alerts_data, load_resources_data, filter_alerts
from src.ui.components import get_category_badge_class, parse_contact_action

# Inicialización de la aplicación FastAPI
app = FastAPI(title=APP_TITLE, docs_url=None, redoc_url=None)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "src", "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "src", "templates")

# Montaje de archivos estáticos (CSS) y templates HTML con Jinja2
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# 1. RUTA: INICIO
@app.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
    df_alerts = load_alerts_data()
    df_resources = load_resources_data()
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "active_page": "home",
            "total_alerts": len(df_alerts),
            "total_resources": len(df_resources)
        }
    )

# 2. RUTA: SEÑALES DE ALERTA
@app.get("/alertas", response_class=HTMLResponse)
async def alerts_view(request: Request, categoria: str = "Todas las categorías", q: str = ""):
    df_alerts = load_alerts_data()
    categories = sorted(list(df_alerts["Categoría"].unique()))
    df_filtered = filter_alerts(df_alerts, categoria, q)
    
    # Enriquecer cada fila con la clase CSS del badge semántico
    alerts_list = []
    for _, row in df_filtered.iterrows():
        item = dict(row)
        item["badge_class"] = get_category_badge_class(item.get("Categoría", ""))
        alerts_list.append(item)
        
    return templates.TemplateResponse(
        request=request,
        name="alerts.html",
        context={
            "active_page": "alerts",
            "alerts": alerts_list,
            "categories": categories,
            "selected_category": categoria,
            "search_query": q
        }
    )

# 3. RUTA: RECURSOS DE AYUDA
@app.get("/recursos", response_class=HTMLResponse)
async def resources_view(request: Request):
    df_resources = load_resources_data()
    resources_list = []
    for _, row in df_resources.iterrows():
        item = dict(row)
        # Parseo inteligente de teléfono o sitio web
        item["action"] = parse_contact_action(item.get("Contacto", ""))
        resources_list.append(item)
        
    return templates.TemplateResponse(
        request=request,
        name="resources.html",
        context={
            "active_page": "resources",
            "resources": resources_list
        }
    )

# 4. RUTA: AUTOEVALUACIÓN (GET)
@app.get("/autoevaluacion", response_class=HTMLResponse)
async def quiz_view(request: Request):
    df_alerts = load_alerts_data()
    grouped = {}
    for cat in sorted(df_alerts["Categoría"].unique()):
        grouped[cat] = df_alerts[df_alerts["Categoría"] == cat].to_dict(orient="records")
        
    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={
            "active_page": "quiz",
            "grouped_alerts": grouped,
            "evaluated": False,
            "total_checked": 0,
            "selected_conductas": []
        }
    )

# 5. RUTA: AUTOEVALUACIÓN (POST - PROCESAR RESPUESTAS)
@app.post("/autoevaluacion", response_class=HTMLResponse)
async def quiz_submit(request: Request):
    form_data = await request.form()
    conductas_marcadas = form_data.getlist("conductas")
    
    df_alerts = load_alerts_data()
    grouped = {}
    for cat in sorted(df_alerts["Categoría"].unique()):
        grouped[cat] = df_alerts[df_alerts["Categoría"] == cat].to_dict(orient="records")
        
    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={
            "active_page": "quiz",
            "grouped_alerts": grouped,
            "evaluated": True,
            "total_checked": len(conductas_marcadas),
            "selected_conductas": conductas_marcadas
        }
    )

# Ejecución directa con uvicorn si se corre `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
