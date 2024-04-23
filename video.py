desde anuncio import Anuncio

class Video(Anuncio):
    # Constantes para el formato y subtipos del anuncio de video
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        # Inicializa el anuncio de video con ancho, alto, URL del archivo, URL de clic, subtipo y duración
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.__duracion = max(duracion, 1)  # Validación de la duración del video
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        pass
    
    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto):
        pass
    
    def comprimir_anuncio(self):
        # Método para comprimir el anuncio de video
        print("Compresión de video aún no implementada")

    def redimensionar_anuncio(self):
        # Método para redimensionar el anuncio de video
        print("Redimensionamiento de video aún no implementado")
