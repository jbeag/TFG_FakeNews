import time
import selenium
from selenium.webdriver.chrome.service import Service

# Ruta ChromeDriver
ruta_chromedriver = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"

# Opciones de Chrome
opciones = selenium.webdriver.ChromeOptions()

# Carga de la extensión 
ruta_extension = r"C:\Users\User\Downloads\Fake-news-debunker-by-InVID-WeVerify.crx"
opciones.add_extension(ruta_extension)

# Inicializar el navegador Chrome 
driver = selenium.webdriver.Chrome(service=service, options=opciones)

# Maximizar la ventana del navegador 
driver.maximize_window()

# Abrir extensión 
driver.get('chrome-extension://mhccpoafgdgbhnjfhkcmgknndkeenfhe/popup.html#/app/tools/all')

# Espera 20 segundos
time.sleep(20)

# Cerrar el navegador 
driver.quit()
