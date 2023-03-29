import linkedlist as link
from algo1 import *

""" Implementar un algoritmo Contiene-Suma(A,n) 
que recibe una lista de enteros A y un entero n y devuelve 
True si existen en A un par de elementos que sumados den n. 
Analice el costo computacional. """


def ContieneSuma(A,n):
    if A.head == None:
        return
    else:
        return ContieneSumaR(A.head,A.head,n)

def ContieneSumaR(node,node2,n): #node2 es siempre head al principio

    if node != node2:
        if node2!=None:
            if node.value + node2.value == n:
                return True
            else:
                ContieneSumaR(node,node2.nextNode,n)
        else:
            ContieneSumaR(node.nextNode,node2,n)
    return None

