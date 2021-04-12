'''
Created on 9 abr. 2021

@author: erido
'''
import csv
from Nodo import nuevoN
from numpy.random.mtrand import randint
from random import randrange
from numpy import random
from cmath import sqrt
from Arista import aristasMalla, aristasDorogobsev, aristaBarbasi,\
    aristaErdosRenyi, aristasGeografico
from xmlrpc.client import boolean


class Grafo():
    nodos=[]
    aristas={}
    x={}
    y={}

#n es el numero de nodos a lo largo y m a lo ancho para un arreglo rectangular 
def malla(n,m,dirigido):
    lim=n*m
    nuevoN(lim)
    Grafo.aristas= aristasMalla(lim,n, dirigido)
    aristas=list(Grafo.aristas)
    with open("listAristasMalla500nodos.csv", "w") as fichero:
        writer = csv.writer(fichero)
        if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
        if dirigido==False:writer.writerow(['Source', 'Target'])
        writer.writerows(aristas)         

#n=numero de nodos m= numero de aristas aleatorias         
def ErdosRenyi(n,m, dirigido): 
    nuevoN(n)
    Grafo.aristas= aristaErdosRenyi(n,m, dirigido )     
    aristas=list(Grafo.aristas)   
    with open("listAristas.csv", "w") as fichero:
        writer = csv.writer(fichero)
        if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
        if dirigido==False:writer.writerow(['Source', 'Target'])
        writer.writerows(aristas)       

def gilbert(n,p, dirigido):# n es numero de nodos, p es la probabilidad 
    nuevoN(n)
    Grafo.aristas= (n,p,dirigido)        
    aristas=list(Grafo.aristas)    
    with open("listAristas.csv", "w") as fichero:
        writer = csv.writer(fichero)
        if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
        if dirigido==False:writer.writerow(['Source', 'Target'])
        writer.writerows(aristas) 
    
def geografico(n,r, dirigido= boolean): # N es el numero de nodos y r es la distancia a la que deben estar los nodos para generar arista
    nuevoN(n)
    Grafo.aristas= aristasGeografico(n,r,dirigido)
    aristas=list(Grafo.aristas)    
    with open("listAristas.csv", "w") as fichero:
        writer = csv.writer(fichero)
        if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
        if dirigido==False:writer.writerow(['Source', 'Target'])
        writer.writerows(aristas) 

def Barabasi(n,g, dirigido=boolean): # n es el numero de nodos y g es el maximo numero de aristas por nodo 
    nuevoN(n)
    Grafo.aristas=aristaBarbasi(n,g)            
    aristas=list(Grafo.aristas)    
    with open("listAristas.csv", "w") as fichero:
        writer = csv.writer(fichero)
        if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
        if dirigido==False:writer.writerow(['Source', 'Target'])
        writer.writerows(aristas) 


def DorogobsevM(n, dirigido=boolean): #n es igual al numero de nodos 
    nuevoN(n)
    Grafo.aristas=aristasDorogobsev(n, dirigido)
    aristas=list(Grafo.aristas)    
    with open("listAristas.csv", "w") as fichero:
        writer = csv.writer(fichero)
        if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
        if dirigido==False:writer.writerow(['Source', 'Target'])
        writer.writerows(aristas) 
            
malla(25, 20, True)


    

