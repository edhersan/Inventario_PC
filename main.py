from src.menu import menu_opcion_1, menu_opcion_2, menu_opcion_3, menu_opcion_4, menu_opcion_5


def mostrar_menu():
    print("===== MENÚ INVENTARIO =====")
    print("1. Registrar PC")
    print("2. Buscar PC por serial")
    print("3. Modificar PC por serial")
    print("4. Eliminar PC por serial")
    print("5. Mostrar inventario")
    print("6. Salir")

def main(): 
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
            menu_opcion_4()

        elif opcion == "5":
            menu_opcion_5()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")
        

if __name__ == "__main__":
    main()