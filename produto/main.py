from tkinter import Tk

from produto.gui import Gui


def main() -> None:
    window = Tk()
    Gui(window)
    window.title("Bem Vindo a Aplicação de Banco de Dados")
    window.geometry("820x600+10+10")
    window.mainloop()


if __name__ == "__main__":
    main()
