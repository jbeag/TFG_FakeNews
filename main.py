import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests

# Funciones para las llamadas a las APIs (reemplaza con las funciones adecuadas)
def google_fact_check(ruta_imagen):
    import requests

    # API Key
    api_key = "AIzaSyAdMZyEh6qs06AebTuwMrtjAiui7yrapFM"

    # Remplazar por el hecho a verificar
    claim = "chemtrails"

    url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?key={api_key}&query={claim}"
    print(url)

    # Mandar request
    response = requests.get(url)

    # Chequear codigo de respuesta
    if response.status_code == 200:
        # Respuesta JSON
        fact_check_results = response.json()

        # Imprimir Resultado
        print(fact_check_results)
    else:
        print(f"Error fetching fact check results: {response.status_code}")
        print(response.json())

def buscar_imagen_google(ruta_imagen):
    from google_images_downloader import GoogleImagesDownloader

    downloader = GoogleImagesDownloader(browser="chrome", show=False, debug=False,
                                        quiet=False, disable_safeui=False)  # Valores

    downloader.download("melon cat", destination=r"C:\Users\User\Downloads\Busqueda")  # Destino de Descarga

    downloader.close()  # Cerrar el Driver

def verificar_autenticidad_imagen(ruta_imagen):
    import time
    import selenium
    from selenium.webdriver.chrome.service import Service

    # Ruta al ejecutable
    ruta_chromedriver = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"

    # Opciones de Chrome
    opciones = selenium.webdriver.ChromeOptions()

    # Carga de la extensión
    ruta_extension = r"C:\Users\User\Downloads\Fake-news-debunker-by-InVID-WeVerify.crx"
    opciones.add_extension(ruta_extension)

    # Inicializar el navegador Chrome
    service = Service(ruta_chromedriver)
    driver = selenium.webdriver.Chrome(service=service, options=opciones)

    # Maximizar la ventana del navegador
    driver.maximize_window()

    # Abrir una URL a la extensión cargada
    driver.get('chrome-extension://mhccpoafgdgbhnjfhkcmgknndkeenfhe/popup.html#/app/tools/all')

    # Espera 20 segundos antes de cerrar el navegador
    time.sleep(20)

    # Cerrar el navegador cuando hayas terminado
    driver.quit()

def verificar_autenticidad_video(url_video):
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
    service = Service(ruta_chromedriver)
    driver = selenium.webdriver.Chrome(service=service, options=opciones)

    # Maximizar la ventana del navegador
    driver.maximize_window()

    # Abrir extensión
    driver.get('chrome-extension://mhccpoafgdgbhnjfhkcmgknndkeenfhe/popup.html#/app/tools/all')

    # Espera 20 segundos
    time.sleep(20)

    # Cerrar el navegador
    driver.quit()

def obtener_verificacion_claims(texto):
    import requests
    import json

    api_key = "cae0ccf67bf64a578070e1b787bcf1e3"
    input_claim = "The sky is blue."

    # Ruta del Endpoint del webservice
    api_endpoint = f"https://idir.uta.edu/claimbuster/api/v2/score/text/{input_claim}"
    request_headers = {"x-api-key": api_key}

    # Lanzamos el get con la libreria de request
    api_response = requests.get(url=api_endpoint, headers=request_headers)

    # Imprimos la respuesta del json
    print(api_response.json())

def buscar_noticias(texto_noticia):
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

def snopes(texto_noticia):
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

def fotoforensic(ruta_imagen):
    import time
    import selenium
    from selenium.webdriver.chrome.service import Service

    # Ruta al ejecutable
    ruta_chromedriver = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"

    # Opciones de Chrome
    opciones = selenium.webdriver.ChromeOptions()

    # Inicializa el navegador
    service = Service(ruta_chromedriver)
    driver = selenium.webdriver.Chrome(service=service, options=opciones)

    # Abre una URL  en el navegador
    url = 'https://fotoforensics.com/'
    driver.get(url)

    # Espera 20 segundos
    time.sleep(20)

    # Cierra el navegador cuando hayas terminado
    driver.quit()

def forensically(ruta_imagen):
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
    url = 'https://29a.ch/photo-forensics/#forensic-magnifier'
    driver.get(url)

    # Espera 20 segundos
    time.sleep(20)

    # Cierra el navegador cuando hayas terminado
    driver.quit()

# Funciones para la interfaz gráfica
def buscar_imagen_google_gui():
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        resultado = buscar_imagen_google(ruta_imagen)
        if resultado:
            popup_resultado(resultado)

def verificar_autenticidad_imagen_gui():
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        resultado = verificar_autenticidad_imagen(ruta_imagen)
        if resultado:
            popup_resultado(resultado)

def verificar_autenticidad_video_gui():
    url_video = entry_video.get()
    resultado = verificar_autenticidad_video(url_video)
    if resultado:
        popup_resultado(resultado)

def obtener_verificacion_claims_gui():
    texto = entry_claim.get()
    resultado = obtener_verificacion_claims(texto)
    if resultado:
        popup_resultado(resultado)

def buscar_noticias_gui():
    texto_noticia = entry_noticia.get()
    resultado = buscar_noticias(texto_noticia)
    if resultado:
        popup_resultado(resultado)

def snopes_gui():
    texto_noticia = entry_noticia.get()
    resultado = snopes(texto_noticia)
    if resultado:
        popup_resultado(resultado)

def fotoforensic_gui():
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        resultado = fotoforensic(ruta_imagen)
        if resultado:
            popup_resultado(resultado)

def forensically_gui():
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        resultado = forensically(ruta_imagen)
        if resultado:
            popup_resultado(resultado)

def popup_resultado(resultado):
    popup = tk.Toplevel()
    popup.title("Resultado")
    text_resultado = tk.Text(popup, wrap="word")
    text_resultado.insert(tk.END, resultado)
    text_resultado.pack()

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Verificación de Contenidos")

# Menú de opciones
menu = tk.Menu(root)
root.config(menu=menu)

sub_menu = tk.Menu(menu)
menu.add_cascade(label="Seleccionar Aplicación", menu=sub_menu)
sub_menu.add_command(label="Buscar Imagen en Google", command=buscar_imagen_google_gui)
sub_menu.add_command(label="Verificar Autenticidad de Imagen (TinEye)", command=verificar_autenticidad_imagen_gui)
sub_menu.add_command(label="Verificar Autenticidad de Video (InVID)", command=verificar_autenticidad_video_gui)
sub_menu.add_command(label="Obtener Verificación de Claims (ClaimBuster)", command=obtener_verificacion_claims_gui)
sub_menu.add_command(label="Buscar Noticias (Hoaxy)", command=buscar_noticias_gui)
sub_menu.add_command(label="Snopes", command=snopes_gui)
sub_menu.add_command(label="Fotoforensic", command=fotoforensic_gui)
sub_menu.add_command(label="Forensically", command=forensically_gui)

# Entradas para la interfaz
entry_video = tk.Entry(root, width=50)
entry_video.pack()

entry_claim = tk.Entry(root, width=50)
entry_claim.pack()

entry_noticia = tk.Entry(root, width=50)
entry_noticia.pack()

root.mainloop()
