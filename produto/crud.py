import os

import psycopg2

from produto.models import Produto


class Crud:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
        )
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS public."PRODUTO" (
                CODIGO INTEGER PRIMARY KEY,
                NOME TEXT NOT NULL,
                PRECO REAL NOT NULL
            );"""
        )

    def select(self, code: int | None = None) -> list[tuple[Produto, ...]]:
        query = 'SELECT * FROM public."PRODUTO";'
        if code:
            self.cur.execute(f"{query} WHERE CODIGO = {code};", (code,))
        else:
            self.cur.execute(query)
        return self.cur.fetchall()

    def insert(self, produto: Produto) -> None:
        self.cur.execute(
            'INSERT INTO public."PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES (%s, %s, %s)',
            (produto.code, produto.name, produto.price),
        )
        self.conn.commit()

    def update(self, produto: Produto) -> None:
        self.cur.execute(
            """
            UPDATE public."PRODUTO"
            SET "NOME" = %s, "PRECO" = %s
            WHERE "CODIGO" = %s
            """,
            (produto.name, produto.price, produto.code),
        )
        self.conn.commit()

    def delete(self, *, code: int) -> None:
        self.cur.execute(
            """
            DELETE FROM public."PRODUTO"
            WHERE "CODIGO" = %s
            """,
            (code,),
        )
        self.conn.commit()

    def __del__(self) -> None:
        self.cur.close()
        self.conn.close()
