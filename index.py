import xml.etree.ElementTree as ET

from obj_Plat import Plataformas #lista
from obj_Plat import plataforma #objeto

from obj_juegos import Games #objeto
from obj_juegos import Juegos #arr

from lista_plataformas import lista_Plataforma
listP = lista_Plataforma()
from lista_juegos import lista_Games
listG = lista_Games()

Doc = "Ejemplo.xml"
arrPL = Plataformas
arrGames = Juegos
xmlfile = Doc
tree = ET.parse(xmlfile)
root = tree.getroot()

#ListaPlataformas
for elm in root.findall("ListaPlataformas"):
    for plataformas in elm.findall("Plataforma"):
        nombre = plataformas.find("nombre").text
        codigo = plataformas.find("codigo").text
        listP.insertOrdenadas(nombre,codigo)

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
            listG.insertOrdenadas(codigo,nombre,arrplt)


print("***Lista Plataformas***")
listP.mostrar()


print("***Listado Juegos***")
listG.mostrar()


#cadena
cadena = ""
cadena += "<?xml version='1.0'?>\n"
cadena += "\t<JuegosViejos>\n"
cadena = listP.arch(cadena)
cadena = listG.arch(cadena)
cadena += "\t</JuegosViejos>\n"

with open("salida.xml","w") as docXml:
    docXml.write(cadena)
    docXml.close()