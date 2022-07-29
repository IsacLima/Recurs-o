class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def __len__(self):
        return self._size
        
    def add(self,elem):
        if(self.head):
            #caso tenha alguem no coco
            aux = self.head
            while(aux.next):
                aux = aux.next
            aux.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1
    
    def __getitem__(self, index):
        #permite que facamos lista[2] ao inves de lista.get(2)
        aux = self.head
        for i in range(index):
            #se existe um cocao
            if aux:
                aux = aux.next
            else:
                raise IndexError("vish, foi longe demais, nem tem ninguém nesse índice")
        if aux:
            return aux.data
        raise IndexError("vish, foi longe demais, nem tem ninguém nesse índice")
            
    
    def __setitem__(self, index, elem):
        #permite que facamos lista[9] = 3 ao inves de lista.set(5, 9)
        aux = self.head
        for i in range(index):
            #se existe um cocao
            if aux:
                aux = aux.next
            else:
                raise IndexError("vish, foi longe demais, nem tem ninguém nesse índice")
        if aux:
            aux.data = elem
        else:
            raise IndexError("vish, foi longe demais, nem tem ninguém nesse índice")
