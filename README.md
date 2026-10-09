# Sistema LIRA

**Sistema LIRA** es una aplicación en consola desarrollada en Python orientada a la orientación, prevención y detección de señales de alerta en relaciones de pareja, así como al acceso rápido a canales y recursos gratuitos de apoyo y ayuda en Chile.

---

## 📋 Contenido del Proyecto

El repositorio actualmente consta de los siguientes archivos:

- **[`Sistema LIRA.py`](file:///c:/Sistema%20trabajo%20ciencias/Proyectoss/Sistema%20LIRA.py)**: Script principal en Python que contiene la lógica de lectura de datos, formateo y el menú interactivo por consola.
- **[`trabajo ciencias 1.csv`](file:///c:/Sistema%20trabajo%20ciencias/Proyectoss/trabajo%20ciencias%201.csv)**: Base de datos que almacena señales de alerta categorizadas (control, manipulación, intimidación, etc.), la conducta observada y su descripción.
- **[`trabajo ciencias 2.csv`](file:///c:/Sistema%20trabajo%20ciencias/Proyectoss/trabajo%20ciencias%202.csv)**: Base de datos con servicios de apoyo psicológico y de emergencia gratuitos, canales de contacto (teléfono/web) y horarios de atención.

---

## 🚀 Funcionalidades Actuales

1. **Consulta de Señales de Alerta**:
   - Carga y despliega información clasificada por categorías de comportamientos de riesgo (por ejemplo: *Control y Aislamiento*, *Manipulación y agresión psicológica*, *Conductas intimidatorias*).
   - Muestra conductas específicas como *Gaslighting*, *Aislamiento social*, *Bombardeo de amor*, etc., junto a su explicación detallada.

2. **Directorio de Recursos de Ayuda Gratuitos**:
   - Muestra canales de asistencia y orientación, tales como:
     - **Hablemos de Todo (INJUV)**
     - **Psicólogos voluntarios de Chile**
     - **Fono Orientación y Ayuda Violencia contra las mujeres (1455)**
   - Proporciona vías de contacto directo y horarios de atención.

3. **Interfaz Interactiva por Consola**:
   - Menú numérico simple e intuitivo para navegar entre las opciones o salir del sistema.

---

## 🛠️ Requisitos e Instalación

- **Python 3.7 o superior** (no requiere librerías externas adicionales; utiliza los módulos estándar `csv` y `os`).

### Ejecución

Para iniciar el sistema, abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python "Sistema LIRA.py"
```

---

## 📌 Estado de Desarrollo y Observaciones

> [!NOTE]
> - Actualmente el menú interactivo se encuentra dentro del flujo de ejecución del script principal.
> - Se recomienda verificar los delimitadores y encabezados en los archivos CSV (por ejemplo, el uso de coma `,` vs punto y coma `;` y la presencia de tildes en encabezados como `Categoría`) para asegurar compatibilidad total en todas las plataformas.

