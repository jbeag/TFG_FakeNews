import time
import selenium
from selenium.webdriver.chrome.service import Service

# Ruta al ejecutable de ChromeDriver
ruta_chromedriver = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"

# Opciones de Chrome
opciones = selenium.webdriver.ChromeOptions()

# Inicializa el navegador Chrome con las opciones
service = Service(ruta_chromedriver)
driver = selenium.webdriver.Chrome(service=service, options=opciones)

# Abre una URL específica en el navegador
url = 'https://www.tineye.com/'
driver.get(url)

# Espera 10 segundos antes de cerrar el navegador
time.sleep(20)

# Cierra el navegador cuando hayas terminado
driver.quit()
