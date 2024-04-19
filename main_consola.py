from src.Console.PensionCalculatorConsole import *

# Constantes para las opciones del menú
opcion_calcular = "1"
opcion_salir = "2"


def bienvenida():
    """Imprime un mensaje de bienvenida al usuario."""
    print("¡Bienvenido a tu Pension Calculator Pro!")


def main():
    """Función principal del programa.

    Muestra el menú principal y gestiona las opciones seleccionadas por el usuario.
    """
    bienvenida()
    while True:
        opcion = mostrar_menu()
        if opcion == opcion_calcular:
            ejecutar_calculo_pension()
        elif opcion == opcion_salir:
            print("¡Gracias por usar nuestro servicio!")
            break  # Salir del programa
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
