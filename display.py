from anuncio import Anuncio

class Display(Advertisement):
    # Atributos de clase que definen el formato y los subtipos del anuncio Display
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "nativo")
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        # Inicializa el anuncio Display con los atributos proporcionados
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncios(self):
        # Método para comprimir anuncios Display
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        # Método para redimensionar anuncios Display
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
