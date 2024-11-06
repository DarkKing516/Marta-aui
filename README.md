# Proyecto de Automatización con Selenium

Este proyecto utiliza Selenium WebDriver para automatizar el proceso de registro de usuarios en una página web. Está diseñado para realizar registros automáticos de múltiples usuarios a través de un formulario en línea.

## Tecnologías Utilizadas

- **Selenium**: Herramienta para automatizar navegadores web.
- **Python**: Lenguaje de programación utilizado para escribir los scripts de automatización.
- **Microsoft Edge WebDriver**: Controlador para automatizar el navegador Edge.

## Instalación

Para ejecutar este proyecto, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   git clone <url_del_repositorio>
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd <nombre_del_directorio>
   ```

3. Instala las dependencias de Python. Asegúrate de tener `pip` instalado:

   ```bash
   pip install selenium
   ```

4. Descarga el **Microsoft Edge WebDriver** que coincida con la versión de tu navegador [aquí](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). Colócalo en la carpeta que prefieras y asegúrate de que el script apunte a la ubicación correcta en el código:

   ```python
   edge_service = Service(executable_path="C:/ruta/al/msedgedriver.exe")
   ```

## Cómo Ejecutar

1. Abre el archivo Python con tu editor de código favorito.

2. Asegúrate de que los datos de registro en el script son correctos (nombre, teléfono, correo, etc.).

3. Ejecuta el script con el siguiente comando:

   ```bash
   python nombre_del_script.py
   ```

4. El script abrirá el navegador Microsoft Edge, rellenará el formulario de registro y enviará los datos automáticamente para cada usuario definido en el script. Después de cada registro, tomará una captura de pantalla y volverá a la página de registro para el siguiente usuario.

## Archivos del Proyecto

- **registro_individual.py**: Realiza un único registro de usuario y guarda una captura de pantalla.
- **registro_multiples.py**: Realiza múltiples registros de usuarios, uno por uno, con datos predefinidos, y guarda una captura de pantalla para cada registro.

## Capturas de Pantalla

Al finalizar el registro de cada usuario, el script toma una captura de pantalla que se guarda en la carpeta del proyecto con el nombre del usuario, como se muestra a continuación:

- **registro_juanperez.png**
- **registro_alejandro123.png**
