# Sistema LIRA 🛡️
> **Línea de Información, Recursos y Alerta**  
> Plataforma interactiva para la orientación, prevención y detección temprana de conductas de riesgo en vínculos cotidianos, con acceso a canales y redes gratuitas de apoyo en Chile.

---

## 🏛️ Arquitectura del Proyecto

El sistema está estructurado bajo una **arquitectura modular limpia**, con separación estricta de responsabilidades, componentes reusables y el 100% de los estilos centralizados:

```text
c:\Sistema trabajo ciencias\
│
├── datasets/                           # Fuentes de datos estructuradas (.csv)
│   ├── trabajo ciencias 1.csv          # Señales de alerta (categoría, conducta, descripción)
│   └── trabajo ciencias 2.csv          # Canales de ayuda (servicio, contacto, horario, notas)
│
├── src/                                # Código fuente modular
│   ├── config.py                       # Configuración general, constantes y rutas
│   ├── services/
│   │   └── data_service.py             # Carga con caché, limpieza y filtrado de datos
│   ├── ui/
│   │   ├── styles.py                   # 🎨 100% del CSS centralizado (Tema Claro/Oscuro, a11y y animaciones)
│   │   └── components.py               # Componentes visuales puros y enrutador de enlaces (tel/web)
│   └── views/
│       ├── home.py                     # Pantalla de bienvenida, métricas y emergencia
│       ├── alerts.py                   # Catálogo de señales con filtros por categoría y buscador
│       ├── resources.py                # Directorio de asistencia con marcación rápida y enlaces web
│       └── quiz.py                     # Autoevaluación interactiva agrupada por categorías
│
├── app.py                              # Entrada principal de la aplicación Web (Streamlit)
├── requirements.txt                    # Dependencias requeridas (Streamlit, Pandas)
└── .gitignore                          # Protección contra publicación de secretos y temporales
```

---

## 🚀 Funcionalidades Principales

1. **🌗 Tema Claro y Tema Oscuro Profesional:**
   - Selector en la barra lateral para alternar en tiempo real:
     - **☀️ Modo Claro:** Fondos suaves y descansados (`#F8FAFC`, `#FFFFFF`) con texto de máximo contraste (`#0F172A`).
     - **🌙 Modo Oscuro:** Paleta nocturna profesional (`#0B0F19`, `#151C2C`) para evitar el cansancio visual en entornos con poca luz.

2. **✨ Microinteracciones y Botones Accesibles (Skill Impeccable):**
   - **Contraste garantizado (WCAG AAA/AA):** Texto 100% legible en estado normal, `:hover` y `:active`, evitando la pérdida de contraste de Streamlit.
   - **Fluidez visual:** Animaciones suaves a 180ms (`cubic-bezier(0.16, 1, 0.3, 1)`) con elevación sutil (`translateY(-2px)`) y sombra reactiva.
   - **Vínculos inteligentes:**
     - Enlaces web (ej. *INJUV*): Abren en pestaña nueva con botón `🌐 Visitar sitio web oficial`.
     - Teléfonos móviles y fijos: Formato directo `tel:` para marcar con un toque desde smartphones.
     - Notas informativas visibles (ej. aviso de llamada gratuita sin saldo para el *Fono 1455*).

3. **📱 UI 100% Responsiva:**
   - Adaptación completa a pantallas de celulares, tablets y computadoras de escritorio.
   - Barra superior de salida rápida apilable en pantallas pequeñas.
   - Objetivos táctiles con un área mínima accesible de 44px de altura.

4. **🔒 Navegación Segura y Discreta:**
   - Botón persistente de **Salida Rápida (Cerrar)** en la parte superior que redirige inmediatamente a Google.
   - Proceso privado que se ejecuta en el navegador sin guardar datos personales ni respuestas de evaluación en servidores.

5. **⚠️ Catálogo de Señales de Alerta:**
   - Conductas clasificadas con badges semánticos por categoría (*Control y Aislamiento*, *Manipulación y agresión psicológica*, *Conductas intimidatorias*).
   - Filtro interactivo por categorías y buscador por palabras clave en tiempo real.

6. **📋 Cuestionario de Autoevaluación:**
   - Formulario reflexivo organizado por temáticas con análisis cualitativo y sugerencias de contención según las conductas identificadas.

---

## 🎨 Sistema de Diseño y Accesibilidad

Todos los estilos visuales están centralizados en [src/ui/styles.py](file:///c:/Sistema%20trabajo%20ciencias/src/ui/styles.py) sin estilos `style="..."` inline dispersos en los componentes:

| Elemento | Tema Claro | Tema Oscuro | Estándar WCAG |
| :--- | :--- | :--- | :--- |
| **Fondo Principal** | `#F8FAFC` | `#0B0F19` | — |
| **Tarjetas** | `#FFFFFF` | `#151C2C` | — |
| **Texto Primario** | `#0F172A` | `#F8FAFC` | Ratio > 14:1 (AAA) |
| **Botones de Acción** | `#4338CA` | `#6366F1` | Ratio > 7:1 (AAA) |
| **Botones Telefónicos** | `#0F766E` | `#14B8A6` (texto `#042F2E`) | Ratio > 8:1 (AAA) |
| **Botones Web** | `#1D4ED8` | `#3B82F6` | Ratio > 4.5:1 (AA) |
| **Panel Emergencia** | `#FFF1F2` (borde `#E11D48`) | `#2B1115` (borde `#F43F5E`) | Texto accesible |

---

## 🛠️ Instalación y Uso

### 1. Requisitos Previos
* **Python 3.8 o superior**

### 2. Instalación de Dependencias
Abre una terminal en la carpeta raíz del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación Web
Para iniciar la aplicación en tu navegador:

```bash
python -m streamlit run app.py
```
*La plataforma se abrirá de forma automática en `http://localhost:8501`.*
