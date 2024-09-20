from models import Crud


def main() -> None:
    crud = Crud()

    crud.insert(1, "Bombril", 3.99)
    crud.select()

    crud.update(1, "Azeite", 12.50)

    crud.delete(code=1)
    crud.select()


if __name__ == "__main__":
    main()
