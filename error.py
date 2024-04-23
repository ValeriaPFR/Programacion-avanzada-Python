class LongitudExcedidaError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)  # Llama al constructor de la clase base Exception
        self.mensaje = mensaje

class TipoSubTipoInvalidoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)  # Llama al constructor de la clase base Exception
        self.mensaje = mensaje
