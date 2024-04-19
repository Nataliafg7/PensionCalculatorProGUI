#
import sys 
sys.path.append("src")
from src.Pension_Calculator.pension_calculator import *

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

# Importa la clase Calcular desde el archivo pension_calculator.py

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Imagen como título
        image = Image(source='logo.jpg', size_hint_y=None, height=200)  # Reemplaza 'logo.jpg' con el nombre de tu imagen
        layout.add_widget(image)
        
        # Lista de nombres de los resultados y sus valores
        result_data = [
            ("Valor del ahorro pensional esperado:", ""),
            ("Pensión anual:", ""),
            ("Pensión mensual:", "")
        ]
        
        # Creamos y agregamos las etiquetas para los resultados a la tabla
        self.result_labels = []
        for name, value in result_data:
            name_label = Label(text=name, font_size=30, color="black",bold=True)
            value_label = Label(text=value, font_size=30, color="black")
            self.result_labels.append(value_label)
            layout.add_widget(name_label)
            layout.add_widget(value_label)
            
        button_layout = BoxLayout(spacing=10)
        layout.add_widget(button_layout)
        # Botón Volver
        volver_button = Button(text='Volver', font_size=25, size_hint=(0.4, None), size=(150, 60))
        volver_button.bind(on_press=self.volver_formulario)
        button_layout.add_widget(volver_button)
        volver_button.background_color = (0, 0, 0, 1)  # Establece el color del botón a negro

        # Botón Salir
        salir_button = Button(text='Salir', font_size=25, size_hint=(0.4, None), size=(150, 60))
        salir_button.bind(on_press=self.salir)
        button_layout.add_widget(salir_button)
        salir_button.background_color = (0, 0, 0, 1)  # Establece el color del botón a negro

        self.add_widget(layout)
       
       
    def mostrar_resultado(self, valor_ahorro_pensional, pension_anual, pension_mensual):
        for label in self.result_labels:
            label.text = ""
        
        self.result_labels[0].text += f" {valor_ahorro_pensional:.3f}"
        self.result_labels[1].text += f" {pension_anual:.3f}"
        self.result_labels[2].text += f" {pension_mensual:.3f}"
    
    def volver_formulario(self, instance):
        self.manager.current = 'formulario'
    def salir(self, instance):
        App.get_running_app().stop()



class PensionCalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PrincipalScreen(name='principal'))
        sm.add_widget(FormScreen(name='formulario'))
        sm.add_widget(ResultScreen(name='resultado'))
        return sm
        
Window.clearcolor = (0.69, 0.77, 0.87, 1)  # Lightsteelblue color

from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


class PrincipalScreen(Screen):
    def __init__(self, **kwargs):
        super(PrincipalScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1)  # Cambiamos a 1 columna
        with self.canvas:
            Color(0.69, 0.77, 0.87, 1)  # Lightsteelblue color
            Rectangle(pos=self.pos, size=self.size)
        self.add_widget(layout)

        # Imagen como título
        image = Image(source='logo.jpg')  # Asegúrate de tener la imagen 'title_image.png' en el mismo directorio
        layout.add_widget(image)


        # Mensaje de bienvenida
        welcome_label = Label(text="[size=40]¡Bienvenido a la calculadora de pensiones![/size] \n                           ¡Esperamos que esta herramienta sea útil para ti!", font_size=20, color="black", markup=True)
        layout.add_widget(welcome_label)
        
        # Botón Ir al formulario
        form_button = Button(text='Ir al formulario', font_size=30)
        form_button.bind(on_press=self.ir_al_formulario)
        form_button.size_hint = (0.3, 0.2)  # Cambia el tamaño del botón
        layout.add_widget(form_button)
        form_button.background_color = (0, 0, 0, 1)
        # Botón Salir
        salir_button = Button(text='Salir', font_size=30)
        salir_button.bind(on_press=self.salir)
        salir_button.size_hint = (0.3, 0.2)  # Cambia el tamaño del botón
        layout.add_widget(salir_button)
        salir_button.background_color = (0, 0, 0, 1)  # Establece el color del botón a negro

    def ir_al_formulario(self, instance):
        self.manager.current = 'formulario'

    def salir(self, instance):
        App.get_running_app().stop()


class FormScreen(Screen):
    def __init__(self, **kwargs):
        super(FormScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[50, 20], spacing=10)
        with self.canvas:
            Color(0.69, 0.77, 0.87, 1)  # Lightsteelblue color
            Rectangle(pos=self.pos, size=self.size)
        self.add_widget(layout)
        
        # Imagen como título
        image = Image(source='logo.jpg')  # Reemplaza 'titulo_formulario.png' con el nombre de tu imagen
        layout.add_widget(image)
        
        # GridLayout para etiquetas y cajas de entrada
        form_layout = GridLayout(cols=2, spacing=[10, 10])
        layout.add_widget(form_layout)
        
        # Labels y TextInputs para recoger los datos
        labels = ["Edad actual:", "Sexo (mujer/hombre):", "Salario actual:", "Semanas laboradas:",
                  "Ahorro actual:", "Rentabilidad del fondo (%):", "Tasa de administración del fondo (%)"]

        # Lista para almacenar las instancias de TextInput
        self.inputs = []

        for label in labels:
            form_layout.add_widget(Label(text=label, color="black", font_size=25, size_hint=(0.4, None), height=30))
            input_field = TextInput(multiline=False, font_size=25, size_hint=(0.4, None), height=30, size=(40, 40))
            form_layout.add_widget(input_field)
            self.inputs.append(input_field)

        # BoxLayout para botones
        button_layout = BoxLayout(spacing=10)
        layout.add_widget(button_layout)
        
        # Botón para calcular
        calcular_button = Button(text='Calcular', font_size=25, size_hint=(0.4, None), size=(150, 60))
        calcular_button.bind(on_press=self.calcular_pension)
        button_layout.add_widget(calcular_button)
        calcular_button.background_color = (0, 0, 0, 1)  # Establece el color del botón a negro

        # Botón para volver a la ventana principal
        volver_button = Button(text='Volver', font_size=25, size_hint=(0.4, None), size=(150, 60))
        volver_button.bind(on_press=self.volver_principal)
        button_layout.add_widget(volver_button)
        volver_button.background_color = (0, 0, 0, 1)  # Establece el color del botón a negro
    
    def calcular_pension(self, instance):
        # Obtener los datos ingresados
        try:
            edad_actual = int(self.inputs[0].text)
            sexo = self.inputs[1].text.lower()
            salario_actual = float(self.inputs[2].text)
            semanas_laboradas = int(self.inputs[3].text)
            ahorro_actual = float(self.inputs[4].text)
            rentabilidad_fondo = float(self.inputs[5].text)
            tasa_administracion = float(self.inputs[6].text)

            # Calcular la pensión
            pension_calculator = Calcular(edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual,
                                          rentabilidad_fondo, tasa_administracion)
            valor_ahorro_pensional, pension_anual, pension_mensual = pension_calculator.calcular_pension()

                       # Mostrar los resultados en la pestaña de resultados
            result_screen = self.manager.get_screen('resultado')
            result_screen.mostrar_resultado(valor_ahorro_pensional, pension_anual, pension_mensual)
            self.manager.current = 'resultado'

        except Exception as e:
            # Mostrar error en caso de excepción
            popup = Popup(title='Error', content=Label(text=str(e)), size_hint=(None, None), size=(900, 300))
            popup.open()

    def mostrar_resultado(self, ahorro_pensional_esperado, pension_anual, pension_mensual):
        content = GridLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text="Resultado del cálculo de la pensión:", font_size=25))
        content.add_widget(Label(text="Valor del ahorro pensional esperado: {:.3f}".format(ahorro_pensional_esperado), font_size=25))
        content.add_widget(Label(text="Valor de la pensión anual: {:.3f}".format(pension_anual), font_size=25))
        content.add_widget(Label(text="Valor de la pensión mensual: {:.3f}".format(pension_mensual), font_size=25))
        
        popup = Popup(title="Resultado", content=content, size_hint=(None, None), size=(900, 300))
        popup.open()
    
    def limpiar_campos(self):
        # Itera sobre los campos de entrada y establece su texto en vacío
        for input_field in self.inputs:
            input_field.text = ""

    def volver_principal(self, instance):
        # Limpiar los campos antes de cambiar a la ventana principal
        self.limpiar_campos()
        self.manager.current = 'principal'

if __name__ == '__main__':
    PensionCalculatorApp().run()
