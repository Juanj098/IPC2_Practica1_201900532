Plataformas = []

class plataforma:
    def __init__(self, nom, code) -> None:
        self.nombre = nom
        self.codigo = code

        self.siguiente = None
        self.anterior = None
    
    def __str__(self) -> str:
        return f"codigo -> {self.codigo}, nombre -> {self.nombre}"