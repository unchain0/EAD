from pyforms import start_app
from pyforms_gui.basewidget import BaseWidget
from pyforms_gui.controls.control_text import ControlText
from pyforms_gui.controls.control_button import ControlButton


class ExemploSimples(BaseWidget):  # type: ignore
    def __init__(self) -> None:
        super(ExemploSimples, self).__init__("ExemploSimples")

        # Definition of the forms fields
        self._nome: ControlText = ControlText("Nome", "Default value")
        self._sobrenome: ControlText = ControlText("Sobrenome")
        self._nomeCompleto: ControlText = ControlText("Nome completo")
        self._button: ControlButton = ControlButton("Pressione o Botão")

        self.set_margin(10)


if __name__ == "__main__":
    start_app(ExemploSimples, geometry=(100, 100, 400, 300))
