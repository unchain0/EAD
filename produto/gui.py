import tkinter as tk
from typing import Any

from crud import Crud
from tkinter import ttk

from produto.models import Produto


class Gui:
    def __init__(self, win: tk.Tk) -> None:
        self.crud = Crud()
        self.iid = 0

        # Componentes
        self.lb_code = tk.Label(win, text="Código do Produto")
        self.lb_name = tk.Label(win, text="Nome do Produto")
        self.lb_price = tk.Label(win, text="Preço")

        self.txt_code = tk.Entry(bd=3)
        self.txt_name = tk.Entry()
        self.txt_price = tk.Entry()

        self.btn_register = tk.Button(
            win, text="Cadastrar", command=self.register_product
        )
        self.btn_update = tk.Button(win, text="Atualizar", command=self.update_product)
        self.btn_delete = tk.Button(win, text="Deletar", command=self.delete_product)
        self.btn_clear = tk.Button(win, text="Limpar", command=self.clear_screen)

        # Componentes TreeView
        self.columns_data = ("Código", "Nome", "Preço")

        self.products_tree = ttk.Treeview(
            win, columns=self.columns_data, selectmode="browse"
        )

        self.scrollbar = ttk.Scrollbar(
            win, orient="vertical", command=self.products_tree.yview
        )
        self.scrollbar.pack(side="right", fill="x")

        self.products_tree.configure(yscrollcommand=self.scrollbar.set)

        self.products_tree.heading("Código", text="Código")
        self.products_tree.heading("Nome", text="Nome")
        self.products_tree.heading("Preço", text="Preço")

        self.products_tree.column("Código", minwidth=0, width=100)
        self.products_tree.column("Nome", minwidth=0, width=100)
        self.products_tree.column("Preço", minwidth=0, width=100)

        self.products_tree.pack(padx=10, pady=10)

        self.products_tree.bind("<<TreeviewSelect>>", self.show_select_registers)

        # Posicionamento dos componentes na janela
        self.lb_code.place(x=100, y=50)
        self.txt_code.place(x=250, y=50)

        self.lb_name.place(x=100, y=100)
        self.txt_name.place(x=250, y=100)

        self.lb_price.place(x=100, y=150)
        self.txt_price.place(x=250, y=150)

        self.btn_register.place(x=100, y=200)
        self.btn_update.place(x=200, y=200)
        self.btn_delete.place(x=300, y=200)
        self.btn_clear.place(x=400, y=200)

        self.products_tree.place(x=100, y=300)
        self.scrollbar.place(x=805, y=300, height=225)
        self.load_initial_date()

    def register_product(self) -> None:
        p = self.read_fields()
        self.crud.insert(p)
        self.products_tree.insert(
            "", "end", iid=self.iid, values=(p.code, p.name, p.price)
        )
        self.iid += 1

    def update_product(self) -> None:
        p = self.read_fields()
        self.crud.update(p)
        self.products_tree.delete(*self.products_tree.get_children())
        self.load_initial_date()
        self.clear_screen()

    def delete_product(self) -> None:
        p = self.read_fields()
        self.crud.delete(code=p.code)
        # Recarregar dados na tela
        self.products_tree.delete(*self.products_tree.get_children())
        self.load_initial_date()
        self.clear_screen()

    def clear_screen(self) -> None:
        """
        Limpar os componentes da tela
        """
        self.txt_code.delete(0, tk.END)
        self.txt_name.delete(0, tk.END)
        self.txt_price.delete(0, tk.END)

    def show_select_registers(self, event: Any) -> None:
        self.clear_screen()
        for selection in self.products_tree.selection():
            item = self.products_tree.item(selection)
            values = item["values"][:3]
            assert isinstance(
                values, (list, tuple)
            ), "Expected a list or tuple for 'values'"
            code, name, price = values
            self.txt_code.insert(0, code)
            self.txt_name.insert(0, name)
            self.txt_price.insert(0, price)

    def load_initial_date(self) -> None:
        for item in self.crud.select():
            p = Produto(*item)
            self.products_tree.insert(
                "",
                "end",
                iid=self.iid,
                values=(p.code, p.name, p.price),
            )
            self.iid += 1

    def read_fields(self) -> Produto:
        code = int(self.txt_code.get())
        name = self.txt_name.get()
        price = float(self.txt_price.get())
        return Produto(code, name, price)
