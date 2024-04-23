desde anuncio import Anuncio

class Social(Anuncio):
    # Constantes para el formato y subtipos de los anuncios sociales
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        # Inicializa el anuncio social con el ancho, alto, URL del archivo, URL de clic y subtipo
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)  
        
    def comprimir_anuncios(self):
        # Método para comprimir anuncios sociales
        print("Compresión de anuncios sociales aún no implementada")

    def redimensionar_anuncio(self):
        # Método para redimensionar anuncios sociales
        print("Redimensión de anuncios sociales aún no implementada")
