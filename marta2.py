from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta a tu WebDriver
edge_service = Service(executable_path="C:/Users/UwU/Documents/selenium/msedgedriver.exe")
driver = webdriver.Edge(service=edge_service)

# Abre la página de registro
driver.get('https://erikas-homemade.onrender.com/configuracion/registrarse/')

# Lista de datos para los registros
datos = [{"nombre": "Patricia", "telefono": "6667788990", "documento": "890123456", "correo": "patricia@example.com", "usuario": "patricia234", "contraseña": "Pass4567"},
    {"nombre": "Alejandro", "telefono": "5556677889", "documento": "789012345", "correo": "alejandro@example.com", "usuario": "alejandro123", "contraseña": "Pass3456"},
    {"nombre": "Andrés", "telefono": "7778899001", "documento": "901234567", "correo": "andres@example.com", "usuario": "andres345", "contraseña": "Pass5678"},
    {"nombre": "Juliana", "telefono": "8889900112", "documento": "012345678", "correo": "juliana@example.com", "usuario": "juliana456", "contraseña": "Pass6789"},
    {"nombre": "Roberto", "telefono": "9990011223", "documento": "123456789", "correo": "roberto@example.com", "usuario": "roberto567", "contraseña": "Pass7890"},
    {"nombre": "Valeria", "telefono": "0001122334", "documento": "234567890", "correo": "valeria@example.com", "usuario": "valeria678", "contraseña": "Pass8901"},
    {"nombre": "Santiago", "telefono": "1112233445", "documento": "345678901", "correo": "santiago@example.com", "usuario": "santiago789", "contraseña": "Pass9012"},
    {"nombre": "Juan", "telefono": "1234567890", "documento": "123456789", "correo": "juan@example.com", "usuario": "juan123", "contraseña": "Password1"},
    {"nombre": "Catalina", "telefono": "2223344556", "documento": "456789012", "correo": "catalina@example.com", "usuario": "catalina890", "contraseña": "Pass0123"},
    {"nombre": "Felipe", "telefono": "3334455667", "documento": "567890123", "correo": "felipe@example.com", "usuario": "felipe901", "contraseña": "Pass1234"},
    {"nombre": "Natalia", "telefono": "4445566778", "documento": "678901234", "correo": "natalia@example.com", "usuario": "natalia012", "contraseña": "Pass2345"},
    {"nombre": "Ana", "telefono": "0987654321", "documento": "987654321", "correo": "ana@example.com", "usuario": "ana456", "contraseña": "Password2"},
    {"nombre": "anuel aa", "telefono": "0987234321", "documento": "91254321", "correo": "ana1213@example.com", "usuario": "an12456", "contraseña": "P1assword2"},
]

for datos_registro in datos:
    # Rellena los campos del formulario
    driver.find_element(By.NAME, "nombre").send_keys(datos_registro["nombre"])
    driver.find_element(By.NAME, "telefono").send_keys(datos_registro["telefono"])
    driver.find_element(By.NAME, "documento").send_keys(datos_registro["documento"])
    driver.find_element(By.NAME, "correo").send_keys(datos_registro["correo"])
    driver.find_element(By.NAME, "usuario").send_keys(datos_registro["usuario"])
    driver.find_element(By.NAME, "contraseña").send_keys(datos_registro["contraseña"])
    
    # Envía el formulario
    driver.find_element(By.ID, "button").click()
    
    # Espera un poco para permitir que el formulario se procese
    time.sleep(5)
    
    # Toma una captura de pantalla después de cada envío
    driver.save_screenshot(f"registro_{datos_registro['usuario']}.png")

    # Volver a la página de registro para el siguiente registro
    driver.get('https://erikas-homemade.onrender.com/configuracion/registrarse/')

# Cierra el navegador
driver.quit()
