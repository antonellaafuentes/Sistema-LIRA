import csv
import os

carpeta_actual = os.path.dirname(os.path.abspath(__file__))

ruta_csv_1 = os.path.join(carpeta_actual, "trabajo ciencias 1.csv")

trabajo_ciencias_1 = []

def mostrar_1(trabajo):
    print(f"Categoria: {trabajo['Categoria']}")
    print(f"Conducta: {trabajo['Conducta']}")
    print(f"Descripcion: {trabajo['Descripcion']}")

def cargar_1():
    trabajo_ciencias_1.clear()
    if os.path.exists(ruta_csv_1):
        with open(ruta_csv_1, "r", encoding="utf-8-sig", newline="") as f:
            lector = csv.DictReader(f, delimiter=";")

            for fila in lector:
                if not fila or not any(fila.values()):
                    continue
                fila["Categoria"] = int(str(fila.get("Categoria", "")).strip())
                fila["Conducta"] = str(fila.get("Conducta", "")).strip()
                fila["Descripcion"] = str(fila.get("Descripcion", "")).strip()
                trabajo_ciencias_1.append(fila)


def listar_1():
    if not trabajo_ciencias_1:
        print("No hay datos en el archivo")
        return
    for trabajo in trabajo_ciencias_1:
        mostrar_1(trabajo)


ruta_csv_2 = os.path.join(carpeta_actual, "trabajo ciencias 2.csv")

trabajo_ciencias_2 = []

def mostrar_2(trabajo):
    print(f"Servicio: {trabajo['Servicio']}")
    print(f"Contacto: {trabajo['Contacto']}")
    print(f"Horario: {trabajo['Horario']}")

def cargar_2():
    trabajo_ciencias_2.clear()
    if os.path.exists(ruta_csv_2):
        with open(ruta_csv_2, "r", encoding="utf-8-sig", newline="") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                if not fila or not any(fila.values()):
                    continue
                fila["Servicio"] = str(fila.get("Servicio", "")).strip()
                fila["Contacto"] = str(fila.get("Contacto", "")).strip()
                fila["Horario"] = str(fila.get("Horario", "")).strip()
                trabajo_ciencias_2.append(fila)

def listar_2():
    if not trabajo_ciencias_2:
        print("No hay datos en el archivo")
        return
    for trabajo in trabajo_ciencias_2:
        mostrar_2(trabajo)


    cargar_1()
    cargar_2()

    while True:
        print("---- Sistema LIRA ----")
        print("1. Señales de alerta")
        print("2. Recursos de ayuda gratuitos")
        print("3. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            listar_1()
        elif opcion == "2":
            listar_2()
        elif opcion == "3":
            print("Ten un buen dia, gracias por usar LIRA")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")