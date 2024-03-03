import time
import selenium
from selenium.webdriver.chrome.service import Service

# Ruta ChromeDriver
ruta_chromedriver = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"

# Opciones de Chrome
opciones = selenium.webdriver.ChromeOptions()

# Inicializa el navegador 
service = Service(ruta_chromedriver)
driver = selenium.webdriver.Chrome(service=service, options=opciones)

# Abre URL 
url = 'https://hoaxy.osome.iu.edu//'
driver.get(url)

# Espera 20 segundos
time.sleep(20)

# Cierra el navegador
driver.quit()
