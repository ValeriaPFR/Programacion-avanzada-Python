from abc import ABC, abstractmethod

class Anuncio(ABC):
    # Metodo constructor para la clase 'Anuncio'
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        # Inicializa los atributos para ancho, alto, url_archivo, url_clic y sub_tipo
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        # Metodo getter para el atributo ancho
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho):
        # Metodo setter para el atributo ancho
        if nuevo_ancho > 0:
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("El ancho debe ser un valor positivo.")

    @property
    def alto(self):
        # Metodo getter para el atributo alto
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto):
        # Metodo setter para el atributo alto
        if nuevo_alto > 0:
            self.__alto = nuevo_alto
        else:
            raise ValueError("La altura debe ser un valor positivo.")

    @property
    def url_archivo(self):
        # Metodo getter para el atributo url_archivo
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, nueva_url):
        # Metodo setter para el atributo url_archivo
        self.__url_archivo = nueva_url

    @property
    def url_clic(self):
        # Metodo getter para el atributo url_clic
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, nueva_url):
        # Metodo setter para el atributo url_clic
        self.__url_clic = nueva_url

    @abstractmethod
    def formato(self):
        # Metodo abstracto para determinar el formato del anuncio
        pass

    @staticmethod
    def mostrar_formatos(formato: str, sub_tipos: tuple):
        # Metodo estático para mostrar los formatos disponibles
        print(f"""
FORMATO {formato}
==========
- {sub_tipos[0]}
- {sub_tipos[1]}
==========
""")

class AnuncioVideo(Anuncio):
    # Define el formato y los subtipos para AnuncioVideo
    FORMATO = "Vídeo"
    SUBTIPOS = ("instream", "outstream")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        # Inicializa el atributo de duracion y asegura que sea al menos 1
        self.duracion = max(duracion, 1)

    @property
    def formato(self):
        # Metodo getter para el formato del anuncio
        return self.FORMATO

    def comprimir_anuncios(self):
        # Metodo para comprimir anuncios de video
        print("COMPRESIÓN DE ANUNCIOS DE VÍDEO IMPLEMENTADA")

    def redimensionar_anuncio(self):
        # Metodo para redimensionar anuncios de video
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE VÍDEO IMPLEMENTADO")

class AnuncioDisplay(Anuncio):
    # Define el formato y los subtipos para AnuncioDisplay
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "nativo")

    def comprimir_anuncios(self):
        # Metodo para comprimir anuncios de display
        print("COMPRESIÓN DE ANUNCIOS DE DISPLAY IMPLEMENTADA")

    def redimensionar_anuncio(self):
        # Metodo para redimensionar anuncios de display
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE DISPLAY IMPLEMENTADO")

class AnuncioSocial(Anuncio):
    # Define el formato y los subtipos para AnuncioSocial
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def comprimir_anuncios(self):
        # Metodo para comprimir anuncios sociales
        print("COMPRESIÓN DE ANUNCIOS SOCIALES IMPLEMENTADA")

    def redimensionar_anuncio(self):
        # Metodo para redimensionar anuncios sociales
        print("REDIMENSIONAMIENTO DE ANUNCIOS SOCIALES IMPLEMENTADO")
