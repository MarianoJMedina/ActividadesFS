from .cuenta import Cuenta
from .direccion import Direccion
from ..evento import Evento

black = 'black'
gold = 'gold'
classic = 'classic'

class Cliente:
    def __innit__(self, **kwargs) -> None:
        self.cuenta = Cuenta(**kwargs)
    
    def inicializacion(self, datos):
        self.numero = datos['numero']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.dni = datos['dni']
        self.direccion = Dirección(**datos['direccion'])
    def puede_crear_chequera(self) -> bool:
        return False
    def puede_comprar_dolar(self) -> bool:
        return False
    def puede_crear_tarjeta_credito(self) -> bool:
        return False
    def get_costo_transferencia(self, monto: int) -> int:
        return monto * self.cuenta.costo_transferencia
    def tiene_cuenta_corriente(self) -> bool:
        return False
    def necesita_autorizar_transferencia_recibida(self) -> bool:
        return True
    