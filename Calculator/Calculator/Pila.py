class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class Pilas:        
    def __init__(self):
        self.top = None
        self.size = 0 
        
    def push(self, item):
        nuevo_nodo = Nodo(item)
        nuevo_nodo.sig = self.top
        self.top = nuevo_nodo
        self.size += 1
           
    def pop(self):
        if self.top is not None:
            dato = self.top.dato
            self.top = self.top.sig
            self.size -= 1
            return dato
        return None
    
    def get_size(self):
        return self.size
    
    def get_top(self):
        if self.top is not None:
            return self.top.dato
        return None
    
    def peek(self):
        if self.top is not None:
            return self.top.dato
        return None
    
    def is_empty(self):
        return self.top is None
        
    def mostrar_elementos(self):
        if self.esta_vacia():
            print("La pila está vacía.")
        else:
            for item in self.items:
                print(item)
        

pila = Pilas()




        

