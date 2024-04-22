from anuncio import Anuncio

class Video(Anuncio):
    #definicion de formato de los anuncios, en video y en dos subtipos; 'instream' y 'outstream'
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        # funcion integrada de Python que permite acceder a los metodos y atributos de la superclase 'Anuncio'.
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo) 
        # atributos de los objetos de la superclase 'Anuncio'
        self.__alto = 1
        self.__ancho = 1
        self.__duracion = duracion if duracion > 0 else 5 # configuracion de la duracion del video
        
    @property
    def ancho(self, ):
        return self.__ancho
    
    @ancho.setter #configuracion de nuevas dimensiones de ancho en 'nuevo_ancho'
    def ancho(self, nuevo_ancho): 
        pass
    @property
    def alto(self, ):
        return self.__alto

    @alto.setter #configuracion de nuevas dimensiones de alto en 'nuevo_alto'
    def alto(self, nuevo_alto):
        pass
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


