from google_images_downloader import GoogleImagesDownloader

downloader = GoogleImagesDownloader(browser="chrome", show=False, debug=False,
                                    quiet=False, disable_safeui=False)  # Valores

downloader.download("melon cat", destination=r"C:\Users\User\Downloads\Busqueda")  # Destino de Descarga


downloader.close()  # Cerrar el Driver
