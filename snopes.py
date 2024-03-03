import time
import selenium
from selenium.webdriver.chrome.service import Service

# Ruta al ejecutable 
ruta_chromedriver = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"

# Opciones de Chrome
opciones = selenium.webdriver.ChromeOptions()

# Inicializa el navegador Chrome 
service = Service(ruta_chromedriver)
driver = selenium.webdriver.Chrome(service=service, options=opciones)

# Abre una URL  en el navegador
url = 'https://www.snopes.com/'
driver.get(url)

# Espera 20 segundos antes de cerrar el navegador
time.sleep(20)

# Cierra el navegador cuando hayas terminado
driver.quit()
