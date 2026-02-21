from src.persistencia import cargar_inventario, guardar_inventario
from src.inventario import registrar_pc, buscar_pc_por_serial, modificar_pc, eliminar_pc

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
        guardar_inventario(inventario)
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
    serial_busqueda = input("Ingresa el serial de la PC a modificar: ")
    pc_encontrado = buscar_pc_por_serial(inventario, serial_busqueda)
    if pc_encontrado is not None:
        print("PC encontrada. Ingresa los nuevos datos (deja en blanco para no modificar):")
        nueva_marca = input(f"Marca ({pc_encontrado['marca']}): ") or pc_encontrado["marca"]
        try:
            nueva_ram_input = input(f"RAM ({pc_encontrado['ram']} GB): ")
            nueva_ram = int(nueva_ram_input) if nueva_ram_input else pc_encontrado["ram"]
            nuevo_disco_input = input(f"Disco ({pc_encontrado['disco']} GB): ")
            nuevo_disco = int(nuevo_disco_input) if nuevo_disco_input else pc_encontrado["disco"]
        except ValueError:
            print("Debes ingresar un número entero para la RAM y el disco.")
            return  # Salir de la función si hay un error

        nuevos_datos = {
            "marca": nueva_marca,
            "ram": nueva_ram,
            "disco": nuevo_disco
        }

        exito = modificar_pc(inventario, serial_busqueda, nuevos_datos)
        if exito:
            print("PC modificada con éxito.")
            guardar_inventario(inventario)
        else:
            print("Error al modificar la PC.")
    else:
        print("No se encontró una PC con ese serial para modificar.")
            
def menu_opcion_4():
    serial_busqueda = input("Ingresa el serial de la PC a eliminar: ")
    exito = eliminar_pc(inventario, serial_busqueda, seriales_registrados)
    if exito:
        print("PC eliminada con éxito.")
        guardar_inventario(inventario)
    else:
        print("No se encontró una PC con ese serial para eliminar.")
                
def menu_opcion_5():
    print("Inventario completo:")
    for pc in inventario:
        print("Marca:", pc["marca"], "RAM:", pc["ram"], "Disco:", pc["disco"], "Serial:", pc["serial"])

inventario = cargar_inventario()
seriales_registrados = { pc["serial"] for pc in inventario }