from clases import Parser, BuscadorProblema, ProcesadorHtml


if __name__ == "__main__":
    Parser = Parser()
    cliente, eventos = parser.execute("eventos.json")
    salidaHtml = ProcesadorHtml()
    buscador = BuscadorProblema(cliente)
    for e in eventos:
        salidaHtml.append(buscador.getResultado(e))

    salidaHtml.crear_html(cliente)