from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    @abstractmethod
    def formato(self):
        pass

    @staticmethod
    def mostrar_formatos(formato: str, subTipos: tuple):
        print(f"""
FORMATO {formato}
==========
- {subTipos[0]}
- {subTipos[1]}
==========
""")

class Video(Anuncio):
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.duracion = max(duracion, 1)

    @property
    def formato(self):
        return self.FORMATO

    def comprimir_anuncios(self):
        # Implementar la lógica específica para comprimir un anuncio de video
        # (por ejemplo, utilizando una biblioteca de compresión de video)
        print("COMPRESIÓN DE VIDEO IMPLEMENTADA")  # Mensaje informativo

    def redimensionar_anuncio(self):
        # Implementar la lógica específica para redimensionar un anuncio de video
        # (por ejemplo, utilizando una biblioteca de manipulación de imágenes)
        print("REDIMENSIONAMIENTO DE VIDEO IMPLEMENTADO")  # Mensaje informativo

class Display(Anuncio):
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncios(self):
        # Implementar la lógica específica para comprimir un anuncio de display
        # (por ejemplo, utilizando técnicas de optimización de imágenes)
        print("COMPRESIÓN DE ANUNCIOS DISPLAY IMPLEMENTADA")  # Mensaje informativo

    def redimensionar_anuncio(self):
        # Implementar la lógica específica para redimensionar un anuncio de display
        # (por ejemplo, ajustando el tamaño de la imagen)
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY IMPLEMENTADO")  # Mensaje informativo

class Social(Anuncio):
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncios(self):
        # Implementar la lógica específica para comprimir un anuncio de redes sociales
        # (por ejemplo, utilizando herramientas de optimización de contenido)
        print("COMPRESIÓN DE ANUNCIOS SOCIALES IMPLEMENTADA")  # Mensaje informativo

    def redimensionar_anuncio(self):
        # Implementar la lógica específica para redimensionar un anuncio de redes sociales
        # (por ejemplo, ajustando el formato de la imagen o el texto)
        print("REDIMENSIONAMIENTO DE ANUNCIOS SOCIALES IMPLEMENTADO")  # Mensaje informativo
