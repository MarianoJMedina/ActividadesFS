from .cliente import Cliente

class ClienteGold(Cliente):
    def __innit__(self, **kwargs) -> None:
        super(ClienteGold, self).__innit__(**kwargs)
    def puede_crear_chequera(self) -> bool:
        return True
    def puede_crear_tarjeta_credito(self) -> bool:
        return False
    def puede_comprar_dolar(self) -> bool:
        return True
    def tiene_cuenta_corriente(self) -> bool:
        return True
    def necesita_autorizar_transferencia_recibida(self) -> bool:
        return True