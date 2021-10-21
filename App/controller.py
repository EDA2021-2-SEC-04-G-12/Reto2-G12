﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
import timeit
import datetime as date



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama a la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog  
# Funciones para la carga de datos
def loadData(catalog) : 
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog) : 
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv' 
    input_file = csv.DictReader(open(artistsfile,encoding='utf-8'))
    for artist in input_file: 
        model.addArtist(catalog,artist)

def loadArtworks(catalog): 
    artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile,encoding='utf-8'))
    model.sortArtistID(catalog['Artist'],3)
    for artwork in input_file : 

        model.addArtWork(catalog,artwork)
# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo
def oldestbyMedium(catalog,medium,n) : 
    Artworks = model.artWorksbyMedium(catalog,medium)
    sortedArtworks = model.sortArtworkDate(Artworks,3)
    return model.oldestn(sortedArtworks,n)

def listCronoArtist(anioinicial,aniofinal,catalog):
    artists = model.listCronoArtist(int(anioinicial),int(aniofinal),catalog) 
    model.sortArtistBegin(artists[0],3)
    return artists[0],artists[1]

def listArtworkbyDate (fecha_inicial, fecha_final,catalog) : 
    fecha_A = date.datetime.strptime(fecha_inicial,'%Y-%m-%d')
    fecha_B = date.datetime.strptime(fecha_final,'%Y-%m-%d')
    artWorks = model.listArtworkbyDate(fecha_A, fecha_B,catalog)
    Cuenta_purchase = model.countPurchasedArtwork(artWorks[0])
    return artWorks[0],Cuenta_purchase,artWorks[1]

def transportarObras(depto,catalog) : 
    transportar = model.transportarObras(depto,catalog)
    return transportar 

def Artworksbynationality (catalog):
    catalog = model.Artworksbynationality(catalog)
    obra = model.Artworksbynationality_2 (catalog)
    return obra
    
def ArtistArtworksbymedium(catalog,Artista) : 
    Value = model.ArtistArtworksbyMedium(Artista,catalog)
    muestraListado = model.masUtilizada(Value[0],Value[1]) 
    return Value[2],Value[1],muestraListado[0],muestraListado[1],muestraListado[2]





    

   
# Funciones de conteo
def countobrasnationality(nationality, catalog):
    obras = model.countobrasnationality(nationality, catalog)
    return obras