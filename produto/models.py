from dataclasses import dataclass


@dataclass
class Produto:
    code: int
    name: str
    price: float
