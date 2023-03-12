Juegos = []

class Games:
    def __init__(self, name, codigo, plataformas) -> None:
        self.Name = name
        self.Code = codigo
        self.Plats = plataformas

        self.siguiente = None
        self.anterior = None

    # def __str__(self) -> str:
    #     return f"name -> {self.Name}, code -> {self.Code}, plats -> {self.Plats}"