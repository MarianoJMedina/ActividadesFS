from .razon import Razon
from ..cliente import Cliente
from ..evento import Eventos

class RazonComprarDolar(Razon):

    def resolver (self, cliente: Cliente, evento: Evento) -> str:
        if not cliente.puede_comprar_dolar():
            return "Este tipo de cuenta no puede comprar dolares"
        
        if evento.monto > evento.saldoEnCuenta:
            return "No tiene saldo suficiente para comprar dolares"
        
        return "No se pudo determinar la razon de la compra de dolares"