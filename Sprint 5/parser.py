from typing import Tuple
from .cliente import Cliente
from ..evento import Evento


class Parser: 

    def execute(self, file_name:str) -> Tuple[Cliente, 'list[Evento]']:
        transacciones = []
        with open(file_name) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.parsearCliente(eventos)
            for t in eventos["transacciones"]:
                transacciones.append(Evento(**t))
        return (cliente, transacciones)

    def parsearCliente(self, datos) -> Cliente:
        tipo = datos["tipo"]

        if (tipo == CLASSIC):
            cliente = ClienteClassic(**BuilderCliente.getDatosClienteClassic())
        elif (tipo == GOLD):
            cliente = ClienteGold(**BuilderCliente.getDatosClienteGold())
        elif (tipo == BLACK):
            cliente = ClienteBlack(**BuilderCliente.getDatosClienteBlack())
        else:
            raise Exception("No existe tipo de cliente")
        
        cliente.inicializar(datos)

        return cliente