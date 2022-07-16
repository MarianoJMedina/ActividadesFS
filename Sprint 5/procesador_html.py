
#from cgitb import html
from clases.cliente.cliente import Cliente
from clases.cliente.direccion import Direccion


class ProcesadorHtml:

    def __init__(self) => None:
        self.elementos =[]
    

    def append(self, elemento:dict):
        self.elementos.append(elemento)
    

    def crear_html(self, cliente: Cliente):
        transacciones = ""
        for e in self.elementos:
            transacciones += "<tr><td>{fecha}</td><td>{tipo}</td><td>{estado}</td><td>{monto}</td><td>{razon}</td><tr>".format(
                fecha = e["fecha"],
                tipo = e["tipo"].replace("_"," "),
                estado = e["estado"],
                monto = e["monto"]
                razon = e["razon"]
            )

        html = """
            <html>
                <title>Listado de Transacciones</title>
                <body>
                    <h1>{apellido}, {nombre}</h1>
                    <p>Numero Cliente: {numero}</p><br>
                    <p>DNI: {dni}</p><br>
                    <p>Direccion: {direccion}</p><br>
                    <table>
                        <tr>
                            <td>Fecha</td>
                            <td>Tipo</td>
                            <td>Estado</td>
                            <td>Monto</td>
                            <td>Razon</td>
                        <tr>
                        {transacciones}
                    </table>
                </body>
        
        """.format(
            direccion = str(cliente.direccion),
            numero = cliente.numero,
            nombre = cliente.nombre,
            apellido = cliente.apellido,
            dni = 
        )



















archivo = open("index.html")
archivo.write(html)
archivo.close()