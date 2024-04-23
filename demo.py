from advertisement import Advertisement, Video, Display, Social
from campania import Campania
from datetime import datetime, timedelta
from error import TipoSubTipoInvalidoError  


def solicitar_tipo_y_subtipo(clase_anuncio):
    """
    Solicita al usuario el tipo y subtipo de anuncio y valida la entrada.

    Args:
        clase_anuncio (type): La clase del anuncio (Video, Display o Social).

    Returns:
        tuple: Tupla que contiene el tipo y subtipo de anuncio ingresados.
    """
    tipos_validos = {
        "video": Video,
        "display": Display,
        "social": Social,
    }

    while True:
        tipo_ingresado = (
            input(f"Ingrese el tipo de anuncio ({', '.join(tipos_validos.keys())}): ")
            .lower()
            .strip()
        )
        if tipo_ingresado in tipos_validos:
            clase_anuncio = tipos_validos[tipo_ingresado]
            subtipo_ingresado = solicitar_subtipo_anuncio(clase_anuncio)
            return tipo_ingresado, subtipo_ingresado
        else:
            print(
                f"Error: El tipo de anuncio '{tipo_ingresado}' no es válido. Los tipos válidos son: {', '.join(tipos_validos.keys())}"
            )


def solicitar_subtipo_anuncio(clase_anuncio):
    """
    Solicita al usuario un subtipo válido para el anuncio de la clase especificada.

    Args:
        clase_anuncio (type): La clase del anuncio (Video, Display o Social).

    Returns:
        str: El subtipo de anuncio ingresado por el usuario.
    """
    subtipos_validos = (
        clase_anuncio.SUBTIPOS
    )  # Obtener los subtipos válidos de la clase
    while True:
        subtipo_ingresado = (
            input(f"Ingrese un subtipo válido para {clase_anuncio.FORMAT.lower()}: ")
            .lower()
            .strip()
        )  # Normalizar el input
        if subtipo_ingresado in subtipos_validos:
            return subtipo_ingresado
        else:
            print(
                f"Error: El subtipo '{subtipo_ingresado}' no es válido. Los subtipos válidos son: {subtipos_validos}"
            )


def solicitar_nombre_campaña():
    """
    Solicita al usuario un nuevo nombre para la campaña y realiza validación.

    Returns:
        str: El nuevo nombre de la campaña ingresado por el usuario.
    """
    while True:
        nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
        if len(nuevo_nombre) <= 250:
            return nuevo_nombre
        else:
            print("Error: El nombre de la campaña no puede exceder los 250 caracteres.")


def crear_anuncio(tipo, subtipo):
    """
    Crea un anuncio en base al tipo y subtipo seleccionados.

    Args:
        tipo (str): El tipo de anuncio (video, display, social).
        subtipo (str): El subtipo de anuncio.

    Returns:
        Anuncio: Objeto Anuncio creado.
    """
    try:
        if tipo == "video":
            ancho = int(input("Ingrese el ancho del video: "))
            alto = int(input("Ingrese el alto del video: "))
            #url_archivo = input("Ingrese la URL del archivo de video: ")
            #url_clic = input("Ingrese la URL de clic del video: ")
            duracion = int(input("Ingrese la duración del video (en segundos): "))
            anuncio = Video(ancho, alto, url_archivo, url_clic, subtipo, duracion)
        elif tipo == "display":
            ancho = int(input("Ingrese el ancho del anuncio display: "))
            alto = int(input("Ingrese el alto del anuncio display: "))
            #url_archivo = input("Ingrese la URL del archivo de imagen: ")
            #url_clic = input("Ingrese la URL de clic del anuncio display: ")
            anuncio = Display(ancho, alto, url_archivo, url_clic, subtipo)
        elif tipo == "social":
            ancho = int(input("Ingrese el ancho del anuncio social: "))
            alto = int(input("Ingrese el alto del anuncio social: "))
            #url_archivo = input("Ingrese la URL del anuncio social: ")
        else:
            raise ValueError(f"Tipo de anuncio no válido: '{tipo}'")
    except ValueError as e:
        print(f"Error: {e}")
        return None


def manejar_error(e):
    """
    Maneja las excepciones y escribe el mensaje de error en el archivo "error.log".

    Args:
        e (Exception): La excepción que se produjo.
    """
    with open("error.log", "a+") as log:
        log.write(f"{e}\n")
    print("Ha ocurrido un error. Consulte el archivo 'error.log' para más detalles.")


def main():
    nuevo_video = [
        Video(640, 480, "video.mp4", "http://example.com", "Video_campania", 60)
    ]
    f_inicio = datetime.now()
    f_termino = f_inicio + timedelta(days=2)
    nueva_campania = Campania("Campaña1", f_inicio, f_termino, nuevo_video)

    try:
        nuevo_nombre = solicitar_nombre_campaña()
        nueva_campania.nombre = nuevo_nombre

        tipo_anuncio, subtipo_anuncio = solicitar_tipo_y_subtipo(Video)
        nuevo_anuncio = crear_anuncio(tipo_anuncio, subtipo_anuncio)
        if nuevo_anuncio:
            nueva_campania.agregar_anuncio(nuevo_anuncio)

    except Exception as e:
        manejar_error(e)


if __name__ == "__main__":
    main()
