from anuncio import Anuncio

class Social(Anuncio):
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)  # Llamada correcta a super()
        
    def comprimir_anuncios(self):
        print("Compresión de social no implementada aún")

    def redimensionar_anuncio(self):
        print("Recorte de social no implementada aún")
