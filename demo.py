from anuncio import Video
from campania import Campania
from datetime import datetime, timedelta

def solicitar_nombre_campaña():
    """
    Solicita al usuario un nuevo nombre para la campaña y realiza validación.
    """
    while True:
        nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
        if len(nuevo_nombre) <= 250:
            return nuevo_nombre
        else:
            print("Error: El nombre de la campaña no puede exceder los 250 caracteres.")

def solicitar_subtipo_anuncio():
    """
    Solicita al usuario un nuevo subtipo para el anuncio y realiza validación.
    """
    while True:
        nuevo_subtipo = input("Ingrese un nuevo subtipo para el anuncio: ")
        # Validar el subtipo aquí según tus criterios
    return nuevo_subtipo

def manejar_error(e):
    """
    Maneja las excepciones y escribe el mensaje de error en el archivo "error.log".
    """
    with open("error.log", "a+") as log:
        log.write(f"{e}\n")
    print("Ha ocurrido un error. Consulte el archivo 'error.log' para más detalles.")

def main():
    nuevo_video = [Video(640, 480, "video.mp4", "http://example.com", "Video_campania", 60)]
    f_inicio = datetime.now()
    f_termino = f_inicio + timedelta(days=2)
    nueva_campania = Campania("Campaña1", f_inicio, f_termino, nuevo_video)

    try:
        nuevo_nombre = solicitar_nombre_campaña()
        nueva_campania.nombre = nuevo_nombre
        nuevo_subtipo = solicitar_subtipo_anuncio()
        nueva_campania.anuncios[0].sub_tipo = nuevo_subtipo

    except Exception as e:
        manejar_error(e)

if __name__ == "__main__":
    main()
