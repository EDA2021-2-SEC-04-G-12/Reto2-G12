﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Imprimir los n mas antiguos por medio")
    

catalog = None
def initCatalog() : 
    return controller.initCatalog() 

def loadData (catalog) : 
    controller.loadData(catalog) 
def oldestArtworksbyMedium(catalog,medium,n): 
    return controller.oldestbyMedium(catalog,medium,n) 
def transportarObras(depto,catalog) : 
    return controller.transportarObras(depto,catalog)
def ArtistArtworksbymedium(catalog,Artista): 
    return controller.ArtistArtworksbymedium(catalog,Artista)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog() 
        loadData(catalog)
        print('Se cargaron: ' + str(lt.size(catalog['Artwork'])) + ' artworks')


        

    elif int(inputs[0]) == 2:
        Medium = input('Ingrese un medio a buscar: ')
        n = int(input('Ingrese el numero de obras a consultar: '))
        oldestbymedium = oldestArtworksbyMedium(catalog,Medium,n)
        for artWork in oldestbymedium : 
            print(oldestbymedium)
    
    elif int(inputs[0]) == 4 : 
        anioinicial = int(input("Ingrese el año inicial: "))
        aniofinal = int(input("Ingrese el año final: ")) 
        artistas = controller.listCronoArtist(anioinicial,aniofinal,catalog) 
        i = 1 
        while i <= 3 :
            print(lt.getElement(artistas,i))
            i += 1 
        j = lt.size(artistas) 
        print('-'*50)
        while j > lt.size(artistas) - 3 : 
            print(lt.getElement(artistas,j))
            j -= 1 
    elif int(inputs[0]) == 5 : 
        Depto = input('Ingrese el departamento a transportar: ')
        Transporte = transportarObras(Depto,catalog)
    
    elif int(inputs[0]) == 8: 
        Artista = input('Ingrese el artista a consultar: ')
        Value = ArtistArtworksbymedium(catalog,Artista) 
        print(Value[0])
        print(Value[1])
        print(Value[2])

        
        



        
        

    else:
        sys.exit(0)
sys.exit(0)
