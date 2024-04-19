from src.Pension_Calculator.pension_calculator import *
def ejecutar_calculo_pension():
    try:
        datos = solicitar_datos_por_consola()
        calcular = Calcular(*datos)
        resultado = calcular.calcular_pension()
        mostrar_resultado(*resultado)
    except (Calcular.edad_negativa, Calcular.saldo_negativo, Calcular.rentabilidad_negativa, Calcular.administracion_negativa, Calcular.semanas_negativas, Calcular.semanas_insuficientes, Calcular.edad_insuficiente, Calcular.sexo_invalido) as e:
        print("Error:", e)


def solicitar_datos_por_consola():
    while True:
        try:
            edad_actual = solicitar_entero_positivo("Ingrese su edad actual: ")
            sexo = solicitar_sexo()
            salario_actual = solicitar_float_positivo(
                "Ingrese su salario actual: ")
            semanas_laboradas = solicitar_entero_positivo(
                "Ingrese el número de semanas laboradas: ")
            ahorro_actual = solicitar_float_positivo(
                "Ingrese su ahorro actual: ")
            rentabilidad_fondo = solicitar_float_positivo(
                "Ingrese la rentabilidad del fondo (%): ")
            tasa_administracion = solicitar_float_positivo(
                "Ingrese la tasa de administración del fondo (%): ")
            return edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion
        except ValueError as ve:
            print("Error:", ve)
            print("Por favor, ingrese datos válidos.\n")


def mostrar_menu():
    print("\nMenu:")
    print("1. Calcular pensión")
    print("2. Salir")
    return input("Ingrese el número de la opción que desea realizar: ")


def mostrar_resultado(ahorro_pensional_esperado, pension_anual, pension_mensual):
    print("Resultado del cálculo de la pensión:")
    print("Valor del ahorro pensional esperado:",
          "{:,.3f}".format(ahorro_pensional_esperado))
    print("Valor de la pensión anual:", "{:,.3f}".format(pension_anual))
    print("Valor de la pensión mensual:", "{:,.3f}".format(pension_mensual))


def solicitar_entero_positivo(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Error: Debe ingresar un número entero positivo.")


def solicitar_float_positivo(mensaje):
    while True:
        valor = input(mensaje)
        try:
            valor_float = float(valor)
            if valor_float >= 0:
                return valor_float
            else:
                print("Error: Debe ingresar un número positivo.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")


def solicitar_sexo():
    while True:
        sexo = input("Ingrese su sexo (mujer/hombre): ").lower()
        if sexo in ["mujer", "hombre"]:
            return sexo
        print("Error: El sexo debe ser 'mujer' o 'hombre'.")


if __name__ == '__main__':
    print("¡Bienvenido a tu pension calculator pro!")
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            ejecutar_calculo_pension()
        elif opcion == "2":
            print("¡Gracias por usar nuestro servicio!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
