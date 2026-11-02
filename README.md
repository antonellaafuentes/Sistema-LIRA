# Sistema LIRA 🛡️
> **Línea de Información, Recursos y Alerta**  
> Plataforma web interactiva desarrollada en **FastAPI + HTML5/CSS3** para la orientación, prevención y detección temprana de conductas de riesgo en vínculos cotidianos, con acceso a canales y redes gratuitas de apoyo en Chile.

---

## 🏛️ Arquitectura del Proyecto (FastAPI Web App)

El sistema está construido bajo una **arquitectura web estándar y moderna (MVC)**, con control total del DOM, cero recargas innecesarias y estilos 100% predecibles:

```text
c:\Sistema trabajo ciencias\
│
├── datasets/                           # Fuentes de datos estructuradas (.csv)
│   ├── trabajo ciencias 1.csv          # Señales de alerta (categoría, conducta, descripción)
│   └── trabajo ciencias 2.csv          # Canales de ayuda (servicio, contacto, horario, notas)
│
├── src/                                # Código fuente modular
│   ├── config.py                       # Configuración general y constantes
│   ├── services/
│   │   └── data_service.py             # Carga, sanitización y filtrado de datos (Pandas)
│   ├── ui/
│   │   └── components.py               # Lógica de componentes (vínculos tel:/web, badges)
│   ├── static/
│   │   └── styles.css                  # 🎨 Hoja de estilos centralizada (Tema Claro/Oscuro y responsividad)
│   └── templates/                      # Plantillas HTML con Jinja2
│       ├── base.html                   # Layout maestro (Sidebar, Navbar, Escape Seguro)
│       ├── home.html                   # Vista Inicio y métricas
│       ├── alerts.html                 # Vista Señales de Alerta con filtros
│       ├── resources.html              # Vista Directorio de Ayuda con botones de llamada directa
│       └── quiz.html                   # Vista Autoevaluación interactiva
│
├── main.py                             # Servidor web principal (FastAPI + Uvicorn)
├── requirements.txt                    # Dependencias del proyecto
└── .gitignore                          # Protección contra subida de secretos y temporales
```

---

## 🚀 Funcionalidades Principales

1. **⚡ Rendimiento y Control Total (FastAPI):**
   - Sin barras de carga ni widgets automáticos de Streamlit.
   - Navegación instantánea y HTML limpio y ligero.

2. **🌗 Tema Claro y Tema Oscuro con 1 Clic:**
   - Alternador en la barra lateral con memoria en `localStorage`:
     - **☀️ Modo Claro:** Fondo suave (`#F8FAFC`, `#FFFFFF`) con texto de alto contraste (`#0F172A`).
     - **🌙 Modo Oscuro:** Paleta nocturna (`#0B0F19`, `#151C2C`) con contraste verificado para lectura descansada.

3. **✨ Microinteracciones y Botones Accesibles:**
   - **Vínculos inteligentes:**
     - Enlaces web (ej. *INJUV*): Abren en pestaña nueva (`target="_blank"`).
     - Teléfonos móviles y fijos: Formato directo `tel:` para marcar con un toque desde smartphones.
     - Avisos y notas (ej. llamada gratuita sin saldo para el *Fono 1455*).
   - Animaciones fluidas a 180ms con elevación sutil en `:hover` y feedback táctil en `:active`.

4. **🔒 Navegación Segura y Discreta:**
   - Botón superior de **Salida Rápida (Cerrar)** que redirige inmediatamente a Google sin dejar rastros en pantalla.

5. **⚠️ Catálogo de Señales de Alerta:**
   - Filtro interactivo por categorías y buscador por palabras clave en tiempo real.

6. **📋 Cuestionario de Autoevaluación:**
   - Formulario organizado por temáticas con análisis cualitativo y recomendaciones inmediatas.

---

## 🛠️ Instalación y Ejecución

### 1. Requisitos Previos
* **Python 3.8 o superior**

### 2. Instalación de Dependencias
Abre una terminal en la carpeta del proyecto e instala las librerías:

```bash
pip install -r requirements.txt
```

### 3. Iniciar el Servidor Web (FastAPI + Uvicorn)
Para iniciar la aplicación:

```bash
python main.py
```
*O también mediante el CLI de Uvicorn:*
```bash
uvicorn main:app --reload
```

Abre tu navegador en:
👉 **[http://localhost:8000](http://localhost:8000)**
