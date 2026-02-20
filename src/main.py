import json


def cargar_inventario(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as f:
            inventario = json.load(f)
            return inventario
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: El archivo de inventario está corrupto. Se iniciará un nuevo inventario.")
        return []

def guardar_inventario(nombre_archivo, inventario):
    with open(nombre_archivo, "w") as f:
        json.dump(inventario, f, indent=4)

def buscar_pc_por_serial(inventario, serial_busqueda):
    for pc in inventario:
        if pc["serial"] == serial_busqueda:
            return pc

    return None
    

def registrar_pc(inventario, nuevo_pc, seriales_registrados):
    serial = nuevo_pc["serial"]

    if serial in seriales_registrados:
        return False

    inventario.append(nuevo_pc)
    seriales_registrados.add(serial)
    return True

def menu_opcion_1():
    marca = input("Marca de la PC: ")
    try:
        ram = int(input("RAM (en GB): "))
        disco = int(input("Disco (en GB): "))
    except ValueError:
        print("Debes ingresar un número entero para la RAM y el disco.")
        return  # Salir de la función si hay un error

    serial = input("Serial: ")
    

    nuevo_pc = {
        "marca": marca,
        "ram": ram,
        "disco": disco,
        "serial": serial
        }

    exito = registrar_pc(inventario, nuevo_pc, seriales_registrados)
    if exito:
        print("PC registrada con éxito.")
        guardar_inventario("../data/inventario.json", inventario)
    else:
        print("Error: El serial ya está registrado.")
            
def menu_opcion_2():
    serial_busqueda = input("Ingresa el serial a buscar: ")
    pc_encontrado = buscar_pc_por_serial(inventario, serial_busqueda)
    if pc_encontrado is not None:
        print("PC encontrada:")
        print("Marca:", pc_encontrado["marca"])
        print("RAM:", pc_encontrado["ram"])
        print("Disco:", pc_encontrado["disco"])
        print("Serial:", pc_encontrado["serial"])
    else:
        print("No se encontró una PC con ese serial.")
            
            
def menu_opcion_3():
    print("Inventario completo:")
    for pc in inventario:
        print("Marca:", pc["marca"], "RAM:", pc["ram"], "Disco:", pc["disco"], "Serial:", pc["serial"])
        
inventario = cargar_inventario("../data/inventario.json")
seriales_registrados = { pc["serial"] for pc in inventario }

def mostrar_menu():
    print("===== MENÚ INVENTARIO =====")
    print("1. Registrar PC")
    print("2. Buscar PC por serial")
    print("3. Mostrar inventario")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        menu_opcion_1()

    elif opcion == "2":
        menu_opcion_2()

    elif opcion == "3":
        menu_opcion_3()       

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")