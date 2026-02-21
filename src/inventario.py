
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


def modificar_pc(inventario, serial_busqueda, nuevos_datos):
    for pc in inventario:
        if pc["serial"] == serial_busqueda:
            pc.update(nuevos_datos)
            return True

    return False

def eliminar_pc(inventario, serial_busqueda, seriales_registrados):
    for i, pc in enumerate(inventario):
        if pc["serial"] == serial_busqueda:
            del inventario[i]
            seriales_registrados.discard(serial_busqueda)
            return True

    return False