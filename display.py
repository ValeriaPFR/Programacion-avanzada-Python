from anuncio import Anuncio

class Display(Anuncio):
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncios(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
