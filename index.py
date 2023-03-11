import xml.etree.ElementTree as ET

from obj_Plat import Plataformas #lista
from obj_Plat import plataforma #objeto

from obj_juegos import Games #objeto
from obj_juegos import Juegos #arr

Doc = "Ejemplo.xml"
arrPL = Plataformas
arrGames = Juegos
xmlfile = Doc
tree = ET.parse(xmlfile)
root = tree.getroot()

#ListaPlataformas
for elm in root.findall("ListaPlataformas"):
    for plataformas in elm.findall("Plataforma"):
        codigo = plataformas.find("codigo").text
        nombre = plataformas.find("nombre").text
        plats = plataforma(nombre,codigo)
        arrPL.append(plats)

#listadoJuegos
for elm in root.findall("ListadoJuegos"):
    for juegos in elm.findall("Juego"):
        codigo = juegos.find("codigo").text
        nombre = juegos.find("nombre").text 
        for plts in juegos.findall("Plataformas"):
            arrplt = [] 
            for plt in plts.findall("Plataforma"):   
                codigoP = plt.find("codigo").text
                arrplt.append(codigoP)
                Game = Games(nombre,codigo,arrplt)
                arrGames.append(Game)


print("***Lista Plataformas***")
for i in arrPL:
    print(i.__str__())

print("***Listado Juegos***")
for i in arrGames:
    print(i.__str__())