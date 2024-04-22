from datetime import datetime
from anuncio import Video, Display, Social  # Importar datetime para trabajar con fechas

class Campania:
    def __init__(self, nombre: str, fecha_inicio: datetime, fecha_termino: datetime, anuncios: list):
        # constructor de la clase 'Campania', inicializa los atributos de la superclase
        self.__nombre = nombre  # asignar el nombre de la campania
        self.__fecha_inicio = fecha_inicio  # asignar la fecha de inicio de la campania
        self.__fecha_termino = fecha_termino  # asignar la fecha de termino de la campania
        self.__anuncios = anuncios  # asignar la lista de anuncios asociados a la campania

    @property
    def nombre(self):
        # getter para el nombre de la campania
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        # setter para el nombre de la campania
        if len(nuevo_nombre) > 250:  # verificar que el nuevo nombre no exceda los 250 caracteres
            raise ValueError(f"El nombre no puede exceder los 250 caracteres. Ingresaste {len(nuevo_nombre)} caracteres.")
        else:
            self.__nombre = nuevo_nombre  # actualizar el nombre de la campania si es válido

    @property
    def fecha_inicio(self):
        # getter para la fecha de inicio de la campania
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        # setter para la fecha de inicio de la campania
        self.__fecha_inicio = nueva_fecha_inicio  # actualizar la fecha de inicio de la campania

    @property
    def fecha_termino(self):
        # getter para la fecha de termino de la campania
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha_termino):
        # setter para la fecha de termino de la campania
        self.__fecha_termino = nueva_fecha_termino  # actualizar la fecha de termino de la campania

    @property
    def anuncios(self):
        # getter para obtener la lista de anuncios asociados a la campania
        return self.__anuncios

def __str__(self):
    # inicializar contadores para cada tipo de anuncio
    cant_video = 0  # contador para anuncios de tipo Video
    cant_display = 0  # contador para anuncios de tipo 'Display'
    cant_social = 0  # contador para anuncios de tipo 'Social'

    # iterar sobre la lista de anuncios
    for elemento in self.__anuncios:
        # verificar el tipo de cada elemento
        if isinstance(elemento, Video):  # vi el elemento es de tipo 'Video'
            cant_video += 1  # incrementar el contador de 'Video'
        elif isinstance(elemento, Display):  # si el elemento es de tipo 'Display'
            cant_display += 1  # incrementar el contador de 'Display'
        elif isinstance(elemento, Social):  # si el elemento es de tipo 'Social'
            cant_social += 1  # Incrementar el contador de 'Social'
    
    # Crear la cadena texto de salida, con los conteos de cada tipo de anuncio
    return f"""
    Nombre de la Campaña: {self.__nombre}
    Anuncios: {cant_video} Video, {cant_display} Display, {cant_social} Social
    """
