from obj_juegos import Games

class lista_Games:

    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    def insert(self,codigo,nombre,plats):
        games = Games(nombre,codigo,plats)
        if self.primero is None:
            self.primero = games
            self.ultimo = games
        else:
            games.anterior = self.ultimo
            self.ultimo.siguiente = games
            self.ultimo = games
    
    def insertOrdenadas(self,codigo,nombre,plats):
        games = Games(nombre,codigo,plats)
        if self.primero is None:
            self.primero = games
            self.ultimo = games
        else:
            if games.Code < self.primero.Code:
                games.siguiente = self.primero
                self.primero.anterior = games
                self.primero = games
            elif games.Code > self.ultimo.Code:
                games.anterior = self.ultimo
                self.ultimo.siguiente = games
                self.ultimo = games
            else:
                aux = self.primero
                while aux.Code < games.Code:
                    aux = aux.siguiente
                games.anterior = aux.anterior
                games.siguiente = aux
                aux.anterior.siguiente = games
                aux.anterior = games

    def mostrar(self):
        if self.primero is None:
            print("Lista Vacia")
        else:
            aux = self.primero
            while aux is not None:
                print(aux.Code,aux.Name,aux.Plats)
                aux = aux.siguiente

    def arch(self,cadena):
        if self.primero is None:
            print("La lista vacia")
        else:
            cadena+="\t\t<ListadoJuegos>\n"    
            aux = self.primero
            while aux is not None:
                cadena += f"\t\t\t<juego>\n"
                cadena += f"\t\t\t\t<codigo>{aux.Code}</codigo>\n"
                cadena += f"\t\t\t\t<nombre>{aux.Name}</nombre>\n"
                cadena += f"\t\t\t\t<Plataformas>\n"
                for plt in aux.Plats:
                    cadena += f"\t\t\t\t\t<Plataforma>\n"
                    cadena += f"\t\t\t\t\t\t<codigo>{plt}</codigo>\n"
                    cadena += f"\t\t\t\t\t</Plataforma>\n"
                cadena += f"\t\t\t\t</Plataformas>\n"
                cadena += f"\t\t\t</juego>\n"
                aux = aux.siguiente
            cadena+="\t\t</ListadoJuegos>\n"    
        return cadena
