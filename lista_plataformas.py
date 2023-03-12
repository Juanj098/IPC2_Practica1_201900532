from obj_Plat import plataforma

class lista_Plataforma:
    
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def insert(self,nombre,codigo):
        juegos = plataforma(nombre,codigo)
        if self.primero is None:
            self.primero = juegos
            self.ultimo = juegos
        else:
            juegos.anterior = self.ultimo
            self.ultimo.siguiente = juegos
            self.ultimo = juegos
    
    def insertOrdenadas(self,nombre,codigo):
        juegos = plataforma(nombre,codigo)
        if self.primero is None:
            self.primero = juegos
            self.ultimo = juegos
        else:
            if juegos.codigo < self.primero.codigo:
                juegos.siguiente = self.primero
                self.primero.anterior = juegos
                self.primero = juegos
            elif juegos.codigo > self.ultimo.codigo:
                juegos.anterior = self.ultimo
                self.ultimo.siguiente = juegos
                self.ultimo = juegos
            else:
                aux = self.primero
                while aux.codigo < juegos.codigo:
                    aux = aux.siguiente
                juegos.anterior = aux.anterior
                juegos.siguiente = aux
                aux.anterior.siguiente = juegos
                aux.anterior = juegos

    def mostrar (self):
        if self.primero is None:
            print("Lista Vacia")
        else:
            aux = self.primero
            while  aux is not None:
                print(aux.codigo, aux.nombre)
                aux = aux.siguiente
   
    def arch(self,cadena):
        if self.primero is None:
            print("La lista esta vacia")
        else:
            cadena +="\t\t<ListaPlataformas>\n"
            aux = self.primero
            while aux is not None:
                cadena +=f"\t\t\t<Plataforma>\n"
                cadena +=f"\t\t\t\t<codigo>{aux.codigo}</codigo>\n"
                cadena +=f"\t\t\t\t<codigo>{aux.nombre}</codigo>\n"
                cadena +=f"\t\t\t</Plataforma>\n"
                aux = aux.siguiente
            cadena +="\t\t</ListaPlataformas>\n"
        return cadena