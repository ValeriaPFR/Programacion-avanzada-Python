from anuncio import Anuncio

class Display(Anuncio):
    #atributos de clase 'Display', subclase de la superclase 'Anuncio'
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native") #tupla 'Display'
    
    def __init__(self,ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str): #definicion de atributos de la superclase 'Anuncio' en el constructor
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo) #ejecutar atributos de superclase 'Anuncio'

    def comprimir_anuncios(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


