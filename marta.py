from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta a tu WebDriver
edge_service = Service(executable_path="C:/Users/UwU/Documents/selenium/msedgedriver.exe")
driver = webdriver.Edge(service=edge_service)

# Abre la página de registro
driver.get('https://erikas-homemade.onrender.com/configuracion/registrarse/')

# Rellenar los campos del formulario
driver.find_element(By.NAME, "nombre").send_keys("Juan Pérez")
driver.find_element(By.NAME, "telefono").send_keys("3111234567")
driver.find_element(By.NAME, "documento").send_keys("123456789")
driver.find_element(By.NAME, "correo").send_keys("juanperez@example.com")
driver.find_element(By.NAME, "usuario").send_keys("juanperez")
driver.find_element(By.NAME, "contraseña").send_keys("ContraseñaSegura123")

# Enviar el formulario
driver.find_element(By.ID, "button").click()

# Esperar a que aparezca un mensaje de éxito o redirección (espera un máximo de 10 segundos)
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "mensaje_de_exito_selector"))
    )
    print("Prueba exitosa: Registro completado")
except:
    print("Prueba fallida: No se pudo completar el registro")

driver.save_screenshot("registro_prueba.png")
# Cerrar el navegador
driver.quit()
