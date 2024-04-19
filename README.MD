# PensionCalculatorPro

## Por:
Juliana Casas Ramírez
Natalia Florez Guzmán

## ¿Qué es?

La calculadora de pensiones es una herramienta digital que ayuda a las personas a estimar el monto de sus pensiones futuras. Utilizando información como la edad actual, el género, el salario actual, las semanas laboradas, el ahorro acumulado, la rentabilidad del fondo de pensiones y la tasa de administración del mismo, esta herramienta proporciona una proyección del ingreso que recibirán durante su jubilación.

## Propósito
El propósito de la calculadora de pensiones es permitir a los usuarios planificar su futuro financiero durante la jubilación. Al proporcionar una estimación del ingreso futuro, los individuos pueden tomar decisiones informadas sobre ahorros y contribuciones al fondo de pensiones, así como ajustar su planificación financiera para asegurar un retiro cómodo y sin preocupaciones.

## ¿Cómo lo haces funcionar?

### Prerrequisitos para Abrir la Calculadora Pensional

Antes de comenzar, asegúrate de tener lo siguiente:

1. **Computadora:** Necesitarás una computadora (Windows, macOS o Linux) para abrir la Calculadora Pensional.

2. **Conexión a Internet:** Asegúrate de tener una conexión a Internet estable para descargar la carpeta "PensionCalculatorProGUI-main".

3. **Programa de Extracción de Archivos:** Deberás tener instalado un programa que te permita extraer archivos comprimidos, como WinRAR, 7-Zip o el descompresor integrado en tu sistema operativo.

4. **Espacio en Disco:** Asegúrate de tener suficiente espacio en disco para almacenar y ejecutar la Calculadora Pensional.

5. **Permisos de Ejecución:** Es posible que necesites tener permisos de ejecución para ejecutar el archivo ejecutable "Ejecutable_Calculadora". Si estás utilizando un sistema operativo que requiere permisos de administrador, asegúrate de tenerlos.

Con estos prerrequisitos, estarás listo/a para abrir y utilizar la Calculadora Pensional en tu computadora. Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en contactarnos. ¡Disfruta utilizando la Calculadora Pensional!

### Ejecución:
### Paso a Paso para Abrir la Calculadora Pensional

Aquí tienes los pasos detallados para abrir y utilizar la Calculadora Pensional:

1. **Descarga de Archivos:**
   - Descarga el archivo comprimido "CalculadoraPensional" desde el enlace proporcionado o desde donde te hayan entregado el archivo.

2. **Extracción de Archivos:**
   - Abre el archivo comprimido "PensionCalculatorProGUI-main.zip" utilizando un programa de extracción de archivos, como WinRAR o 7-Zip.
   - Extrae todos los archivos de la carpeta en una ubicación de tu elección en tu computadora.

3. **Ubicación del Ejecutable:**
   - Después de extraer los archivos, encontrarás una carpeta llamada "PensionCalculatorProGUI-main".
   - Abre esta carpeta y localiza el archivo ejecutable llamado "Ejecutable_Calculadora". Este es el archivo que necesitas ejecutar para abrir la Calculadora Pensional.

   **Abrir para ejecutar consola** 
   Para ejecutar el archivo main_consola.py desde la terminal, siga estos pasos:

1. Abre la terminal.
2. Utiliza el comando cd ruta_de_la_carpeta/PensionCalculatorProGUI-main

Asegúrate de reemplazar ruta_de_la_carpeta con la ruta real de la carpeta "PensionCalculatorProGUI-main" en tu sistema.

3. Una vez en el directorio correcto, puedes ejecutar el archivo main_consola.py utilizando Python. Coloca el siguiente comando en tu terminal:
python main_consola.py

4. **Ejecución del Ejecutable:**
   - Haz doble clic en el archivo "Ejecutable_Calculadora" para ejecutarlo.
   - Dependiendo de tu sistema operativo, es posible que necesites confirmar que deseas ejecutar el archivo.
   -Una vez que aparezca ventana de "Ejecutable_Calculadora", en la parte superior derecha de la ventana encontrarás 3 íconos, selecciona el de la mitad, el cuál es un cuadrado sobre otro cuadrado, llamado "Restore Down".

5. **Interfaz de la Calculadora:**
   - Una vez que se haya ejecutado el archivo, debería abrirse la interfaz de la Calculadora Pensional.
   - Puedes utilizar la interfaz para ingresar los datos necesarios y calcular la pensión.

6. **Uso de la Aplicación:**
   - Completa los campos requeridos con la información relevante, como la edad actual, el salario, las semanas laboradas, etc.
   - Haz clic en el botón "Calcular" para obtener los resultados de la pensión.
   - La aplicación mostrará los resultados en una nueva ventana o pantalla.

7. **Finalización de la Aplicación:**
   - Una vez que hayas utilizado la Calculadora Pensional y obtenido los resultados deseados, puedes cerrar la aplicación haciendo clic en el botón de cierre o saliendo del programa como lo harías con cualquier otra aplicación.

 ¡Espero que encuentres útil la aplicación!
## ¿Cómo está hecho?
CalculadoraPensional/
│
├── Ejecutable_Calculadora        # Archivo ejecutable para abrir la aplicación
│
├── src/                           # Carpeta que contiene el código fuente de la aplicación
│   ├── Console/                   # Carpeta que contiene el código para la versión de consola (no utilizado en la aplicación)
│   │   └── PensionCalculatorConsole.py
│   ├── Gui/                       # Carpeta que contiene el código para la interfaz gráfica de usuario
│   │   └── pension_interface.py
│   └── Pension_Calculator/        # Carpeta que contiene la lógica de cálculo de la pensión
│       └── pension_calculator.py
│
├── tests/                         # Carpeta que contiene pruebas (no utilizado en la aplicación)
│   └── PensionCalculatorTests
│
└── main.py                        # Archivo principal de Python que inicia la aplicación
Claro, aquí tienes la estructura de la aplicación "CalculadoraPensional" en formato de texto:

- **Ejecutable_Calculadora:** Archivo ejecutable para abrir la aplicación.
- **src/:** Carpeta que contiene el código fuente de la aplicación.
  - **Console/:** Carpeta que contiene el código para la versión de consola (no utilizado en la aplicación).
    - **PensionCalculatorConsole.py:** Archivo de código para la versión de consola.
  - **Gui/:** Carpeta que contiene el código para la interfaz gráfica de usuario.
    - **pension_interface.py:** Archivo de código para la interfaz gráfica de usuario.
  - **Pension_Calculator/:** Carpeta que contiene la lógica de cálculo de la pensión.
    - **pension_calculator.py:** Archivo de código para la lógica de cálculo de la pensión.
- **tests/:** Carpeta que contiene pruebas (no utilizado en la aplicación).
  - **PensionCalculatorTests:** Archivo de pruebas.
- **main.py:** Archivo principal de Python que inicia la aplicación.

## ¿Cómo se hizo el ejecutable? 
1. Instalamos PyInstaller usando el comando: pip install pyinstaller, una vez instalado
2. Abrimos la terminal en main.py e ingresamos el siguiente comando: pyinstaller --onefile --windowed main.py
3. Esto creó un archivo el cual llamamos Ejecutable_calculadora.exe


Bibliotecas Utilizadas:
El proyecto hace uso de las siguientes bibliotecas estándar de Python:

unittest: Utilizada para escribir y ejecutar pruebas unitarias.

Dependencias de Otros Proyectos:
El proyecto no tiene dependencias externas a otros proyectos. Todas las funcionalidades están implementadas dentro del propio proyecto sin requerir bibliotecas externas.

