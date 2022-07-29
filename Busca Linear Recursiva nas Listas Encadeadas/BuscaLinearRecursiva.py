from moduloLE import *

def buscaRecursiva(elem, pointer):
    i = 1
    if(pointer):
        if(pointer.data != elem):
            return i + buscaRecursiva(elem, pointer.next)
        return i - 1
        
        
lista = LinkedList()
lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(5)
lista[2] = 9

print(buscaRecursiva(9, lista.head))   
    