from datetime import datetime
from anuncio import Video, Display, Social  # Importar datetime para trabajar con fechas

class Campania:
    def __init__(self, nombre: str, fecha_inicio: datetime, fecha_termino: datetime, anuncios: list):
        # Constructor de la clase 'Campaña', inicializa los atributos de la superclase
        self.__nombre = nombre  # Asignar el nombre de la campaña
        self.__fecha_inicio = fecha_inicio  # Asignar la fecha de inicio de la campaña
        self.__fecha_termino = fecha_termino  # Asignar la fecha de término de la campaña
        self.__anuncios = anuncios  # Asignar la lista de anuncios asociados con la campaña

    @property
    def nombre(self):
        # Getter para el nombre de la campaña
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Setter para el nombre de la campaniaa
        if len(nuevo_nombre) > 250:  # Verificar que el nuevo nombre no exceda 250 caracteres
            raise ValueError(f"El nombre no puede exceder los 250 caracteres. Ingresaste {len(nuevo_nombre)} caracteres.")
        else:
            self.__nombre = nuevo_nombre  # Actualizar el nombre de la campania si es valido

    @property
    def fecha_inicio(self):
        # Getter para la fecha de inicio de la campania
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        # Setter para la fecha de inicio de la campania
        self.__fecha_inicio = nueva_fecha_inicio  # Actualizar la fecha de inicio de la campania

    @property
    def fecha_termino(self):
        # Getter para la fecha de termino de la campania
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha_termino):
        # Setter para la fecha de termino de la campania
        self.__fecha_termino = nueva_fecha_termino  # Actualizar la fecha de término de la campania

    @property
    def anuncios(self):
        # Getter para obtener la lista de anuncios asociados con la campania
        return self.__anuncios

    def __str__(self):
        # Inicializar contadores para cada tipo de anuncio
        contador_video = 0  # Contador para anuncios de tipo 'Video'
        contador_display = 0  # Contador para anuncios de tipo 'Display'
        contador_social = 0  # Contador para anuncios de tipo 'Social'

        # Iterar sobre la lista de anuncios
        for elemento in self.__anuncios:
            # Verificar el tipo de cada elemento
            if isinstance(elemento, Video):  # Si el elemento es de tipo 'Video'
                contador_video += 1  # Incrementar el contador de 'Video'
            elif isinstance(elemento, Display):  # Si el elemento es de tipo 'Display'
                contador_display += 1  # Incrementar el contador de 'Display'
            elif isinstance(elemento, Social):  # Si el elemento es de tipo 'Social'
                contador_social += 1  # Incrementar el contador de 'Social'
        
        # Crear la cadena de texto de salida, con los conteos de cada tipo de anuncio
        return f"""
    Nombre de la Campaña: {self.__nombre}
    Anuncios: {contador_video} Video, {contador_display} Display, {contador_social} Social
    """
