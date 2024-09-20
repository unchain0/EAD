from flexx import flx


class Exemplo(flx.Widget):
    def init(self) -> None:
        flx.Button(text="Olá")
        flx.Button(text="Mundo")


if __name__ == "__main__":
    a = flx.App(Exemplo, title="Flexx demonstração")
    m = a.launch()
    flx.run()
