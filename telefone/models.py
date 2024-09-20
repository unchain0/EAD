import os
import psycopg2
import logging


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
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%H:%M:%S",
        )

    def select(self) -> None:
        self.cur.execute('SELECT * FROM public."PRODUTO"')
        for row in self.cur.fetchall():
            logging.info(row)

    def insert(self, code: int, name: str, price: float) -> None:
        self.cur.execute(
            'INSERT INTO public."PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES (%s, %s, %s)',
            (code, name, price),
        )
        self.conn.commit()

    def update(self, code: int, name: str, price: float) -> None:
        self.cur.execute(
            """
            UPDATE public."PRODUTO"
            SET "NOME" = %s, "PRECO" = %s
            WHERE "CODIGO" = %s
            """,
            (name, price, code),
        )
        self.conn.commit()

        self.cur.execute(
            """
            SELECT "NOME", "PRECO" FROM public."PRODUTO"
            WHERE "CODIGO" = %s
            """,
            (code,),
        )
        logging.info(self.cur.fetchone())

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
