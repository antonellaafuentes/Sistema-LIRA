import os

# Carpeta principal del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carpeta donde se guardan los archivos CSV con los datos
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")

# Rutas a los dos archivos de datos
RUTA_CSV_1 = os.path.join(DATASETS_DIR, "trabajo ciencias 1.csv")
RUTA_CSV_2 = os.path.join(DATASETS_DIR, "trabajo ciencias 2.csv")

# Textos e información general de la aplicación
APP_TITLE = "Sistema LIRA"
APP_SUBTITLE = "Línea de Información, Recursos y Alerta"
PAGE_ICON = "🛡️"

# Números de emergencia oficiales para ayuda rápida
EMERGENCY_PHONE_1 = "911"
EMERGENCY_PHONE_2 = "144"

# Página web a la que redirige el botón de salida rápida para cerrar la app con discreción
SAFE_EXIT_URL = "https://www.google.com"
