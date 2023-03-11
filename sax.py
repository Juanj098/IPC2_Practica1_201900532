import xml.sax

from obj_Plat import plataforma #objeto
from obj_Plat import Plataformas #lista

Doc ="Ejemplo.xml"
list_Plataformas = Plataformas
class Doc_X(xml.sax.ContentHandler):

    def __init__(self):
        self.current = ""
        #plataforma
        self.code = ""
        self.nom = ""
        self.codeP = ""
        # juegos 
        self.plats = []
        self.game = ""
        self.plataformas = None

    def startElement(self, tag, attrs):
        self.current = tag
        if tag == "ListaPlataformas":
            print("----------------------------")
            print("***Lista Plataformas***")
        
        elif tag == "ListadoJuegos":
            print("----------------------------")
            print("***Listado Juegos***")

    def characters(self, content):
        if self.current == "codigo":
            self.code = content
        elif self.current == "nombre":
            self.nom = content
    
    def endElement(self,tag):
        if tag == "ListaPlataformas":
            print(f"nombre --> {self.nom}")
            print(f"codigo --> {self.code}")
        # if tag == "nombre":
        #     print(f"nombre -> {self.nom}")
        # elif tag == "codigo":
        #     print(f"codigo -> {self.code}")

        self.current = ""

handler = Doc_X() 
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('Ejemplo.xml')

# for objeto in list_Plataformas:
#     print(objeto.__str__())

    

