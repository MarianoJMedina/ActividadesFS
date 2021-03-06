from .razon import Razon 
from ..cliente import Cliente
from ..evento import Evento

class RazonAltaChequera(Razon):

    def resolver(self, cliente: Cliente, evento: Evento) -> str:

        if not cliente.puede_crear_chequera():
            return 'Su nivel de cuenta no le permite tener una chequera.'

        if cliente.cuenta.total_chequeras < (evento.totalChequerasActualmente + 1):
            return 'Ya tiene el máximo de chequeras disponibles.'
            
        return 'No se puede determinar el motivo de porqué no se creó la chequera.'
