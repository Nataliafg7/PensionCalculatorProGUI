import sys 
sys.path.append("src")
import unittest
from Pension_Calculator.pension_calculator import *


class TestCalcularPension(unittest.TestCase):

    # Casos Normales
    def test_caso_normal_1(self):
        # Datos de entrada
        edad = 56
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1150
        ahorro_actual = 250000000
        rentabilidad_fondo = 7
        tasa_administracion = 1

        # Resultado esperado
        valor_pensional_esperado = 267500000
        pension_anual_esperada = 16050000
        pension_mensual_esperada = 1337500

        # Llamada a la función para calcular la pensión
        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()
        # Comprobación de los resultados
        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.01)

    def test_caso_normal_2(self):
        edad = 62
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1300
        ahorro_actual = 300000000
        rentabilidad_fondo = 7.5
        tasa_administracion = 1

        valor_pensional_esperado = 300000000
        pension_anual_esperada = 19500000
        pension_mensual_esperada = 1625000

        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()

        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.01)

    def test_caso_normal_3(self):
        edad = 56
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1200
        ahorro_actual = 280000000
        rentabilidad_fondo = 8
        tasa_administracion = 1

        valor_pensional_esperado = 302400000
        pension_anual_esperada = 21168000
        pension_mensual_esperada = 1764000

        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()

        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.01)

    def test_caso_normal_4(self):
        edad = 62
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1400
        ahorro_actual = 320000000
        rentabilidad_fondo = 8.5
        tasa_administracion = 1

        valor_pensional_esperado = 320000000
        pension_anual_esperada = 24000000
        pension_mensual_esperada = 2000000

        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()

        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.01)

    def test_caso_normal_5(self):
        edad = 56
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1250
        ahorro_actual = 270000000
        rentabilidad_fondo = 7.25
        tasa_administracion = 1

        valor_pensional_esperado = 289575000
        pension_anual_esperada = 18098438
        pension_mensual_esperada = 1508203

        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()

        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.5)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.5)

    def test_caso_normal_6(self):
        edad = 62
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1350
        ahorro_actual = 310000000
        rentabilidad_fondo = 7.75
        tasa_administracion = 1

        valor_pensional_esperado = 310000000
        pension_anual_esperada = 20925000
        pension_mensual_esperada = 1743750

        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()

        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.01)

 # Casos excepcionales

    def test_caso_excepcional_1(self):
        edad = 60
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1200
        ahorro_actual = 200000000
        rentabilidad_fondo = 5.5
        tasa_administracion = 1.3
        valor_pensional_esperado = 222605000
        pension_anual_esperada = 9349410
        pension_mensual_esperada = 779117
        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()

    # Comparar cada elemento de las tuplas
        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.5)

    def test_caso_excepcional_2(self):
        edad = 55
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1150
        ahorro_actual = 150000000
        rentabilidad_fondo = 6.75
        tasa_administracion = 1.2
        valor_pensional_esperado = 170933437
        pension_anual_esperada = 9486806
        pension_mensual_esperada = 790567
        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()
        resultado_calculado = tuple(int(round(valor))
                                    for valor in resultado_calculado)
    # Comparar cada elemento de las tuplas
        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.1)

    def test_caso_excepcional_3(self):
        edad = 67
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1400
        ahorro_actual = 280000000
        rentabilidad_fondo = 7.25
        tasa_administracion = 1.4
        valor_pensional_esperado = 197320191
        pension_anual_esperada = 11543231
        pension_mensual_esperada = 961936
        try:
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
            resultado_calculado = calcular.calcular_pension()
            resultado_calculado = tuple(int(round(valor))
                                        for valor in resultado_calculado)
        # Comparar cada elemento de las tuplas
            self.assertAlmostEqual(
                resultado_calculado[0], valor_pensional_esperado, delta=0.01)
            self.assertAlmostEqual(
                resultado_calculado[1], pension_anual_esperada, delta=0.01)
            self.assertAlmostEqual(
                resultado_calculado[2], pension_mensual_esperada, delta=0.01)
        except EdadInsuficiente as e:  # Aquí cambia Calcular.edad_insuficiente por EdadInsuficiente
            print("Advertencia:", e)

    def test_caso_excepcional_4(self):
        edad = 51
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1150
        ahorro_actual = 320000000
        rentabilidad_fondo = 6
        tasa_administracion = 1.2
        valor_pensional_esperado = 453926116
        pension_anual_esperada = 21788454
        pension_mensual_esperada = 1815704
        calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        resultado_calculado = calcular.calcular_pension()
        resultado_calculado = tuple(int(round(valor))
                                    for valor in resultado_calculado)
        # Comparar cada elemento de las tuplas
        self.assertAlmostEqual(
            resultado_calculado[0], valor_pensional_esperado, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[1], pension_anual_esperada, delta=0.01)
        self.assertAlmostEqual(
            resultado_calculado[2], pension_mensual_esperada, delta=0.01)

    def test_caso_excepcional_5(self):
        edad = 65
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1300
        ahorro_actual = 250000000
        rentabilidad_fondo = 7.5
        tasa_administracion = 1.3
        try:
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
            resultado_calculado = calcular.calcular_pension()
            resultado_calculado = tuple(int(round(valor))
                                        for valor in resultado_calculado)
            # Comparar cada elemento de las tuplas
            self.assertAlmostEqual(
                resultado_calculado[0], Calcular.valor_pensional_esperado, delta=0.01)
            self.assertAlmostEqual(
                resultado_calculado[1], Calcular.pension_anual_esperada, delta=0.01)
            self.assertAlmostEqual(
                resultado_calculado[2], Calcular.pension_mensual_esperada, delta=0.01)
        except EdadInsuficiente as e:
            print("Advertencia:", e)

    def test_caso_excepcional_6(self):
        edad = 57
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1200
        ahorro_actual = 180000000
        rentabilidad_fondo = 6.25
        tasa_administracion = 1.4
        valor_pensional_esperado = 180000000
        pension_anual_esperada = 8730000
        pension_mensual_esperada = 727500
        try:
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
            resultado_calculado = calcular.calcular_pension()
            resultado_calculado = tuple(int(round(valor))
                                        for valor in resultado_calculado)
        # Comparar cada elemento de las tuplas
            self.assertAlmostEqual(
                resultado_calculado[0], valor_pensional_esperado, delta=0.01)
            self.assertAlmostEqual(
                resultado_calculado[1], pension_anual_esperada, delta=0.01)
            self.assertAlmostEqual(
                resultado_calculado[2], pension_mensual_esperada, delta=0.1)
        except EdadInsuficiente as e:  
            print("Advertencia:", e)

        
    def test_caso_error_1(self):  # Semanas laboradas negativas
        edad = 55
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = -100
        ahorro_actual = 200000000
        rentabilidad_fondo = 0.06
        tasa_administracion = 0.012
        with self.assertRaises(SemanasNegativas):
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas,
                                ahorro_actual, rentabilidad_fondo, tasa_administracion)
            calcular.calcular_pension()

    def test_caso_error_2(self):  # Saldo negativo
        edad = 40
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1200
        ahorro_actual = -50000000
        rentabilidad_fondo = 0.065
        tasa_administracion = 0.013
        with self.assertRaises(SaldoNegativo):
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas,
                                ahorro_actual, rentabilidad_fondo, tasa_administracion)
            calcular.calcular_pension()

    def test_caso_error_3(self):  # Rentabilidad negativa
        edad = 35
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1200
        ahorro_actual = 300000000
        rentabilidad_fondo = -0.02
        tasa_administracion = 0.011
        with self.assertRaises(RentabilidadNegativa):
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas,
                                ahorro_actual, rentabilidad_fondo, tasa_administracion)
            calcular.calcular_pension()

    def test_caso_error_4(self):  # Administración negativa
        edad = 45
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1300
        ahorro_actual = 250000000
        rentabilidad_fondo = 0.07
        tasa_administracion = -0.015
        with self.assertRaises(AdministracionNegativa):
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas,
                                ahorro_actual, rentabilidad_fondo, tasa_administracion)
            calcular.calcular_pension()


    def test_caso_error_5(self):  # Semanas insuficientes
        edad = 50
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 100
        ahorro_actual = 50000000
        rentabilidad_fondo = 0.06
        tasa_administracion = 0.012
        with self.assertRaises(SemanasInsuficientes):
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas,
                                ahorro_actual, rentabilidad_fondo, tasa_administracion)
            calcular.calcular_pension()

    def test_caso_error_6(self):  # Edad negativa
        edad = -50
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1200
        ahorro_actual = 150000000
        rentabilidad_fondo = 5
        tasa_administracion = 1.1
        with self.assertRaises(EdadNegativa):
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas,
                                ahorro_actual, rentabilidad_fondo, tasa_administracion)
            calcular.calcular_pension()

    def test_caso_error_7(self):  # Rentabilidad superior a cien
        edad = 60
        sexo = "hombre"
        salario_actual = 0
        semanas_laboradas = 1500
        ahorro_actual = 200000000
        rentabilidad_fondo = 110
        tasa_administracion = 1.2
        with self.assertRaises(RentabilidadSuperiorCien):
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas,
                                ahorro_actual, rentabilidad_fondo, tasa_administracion)
            calcular.calcular_pension()

    def test_caso_error_8(self):  # Sexo indefinido
        edad = 56
        sexo = "indefinido"
        salario_actual = 0
        semanas_laboradas = 1150
        ahorro_actual = 250000000
        rentabilidad_fondo = 7
        tasa_administracion = 1
        with self.assertRaises(SexoInvalido):
            calcular = Calcular(edad, sexo, salario_actual, semanas_laboradas,
                                ahorro_actual, rentabilidad_fondo, tasa_administracion)
            calcular.calcular_pension()

if __name__ == '__main__':
    unittest.main()
