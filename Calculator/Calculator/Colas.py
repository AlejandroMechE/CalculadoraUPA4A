class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
                
    def __str__(self):
        return self.dato + "->" + str(self.sig)

class Cola:
    def __init__(self):
        self.primero = None
        
    def isEmpty(self):
        return not self.primero  
    
    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.isEmpty():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo  
    
    def size(self):
        contador = 0
        actual = self.primero
        while actual:
            contador += 1
            actual = actual.sig
        return contador
    
    def desencolar(self):
        if self.isEmpty():
            return None  
        else:
         dato = self.primero.dato
         self.primero = self.primero.sig
         return dato
    
    def posicion(self, dato): # Que turno es o tengo, si el dato no  existe o no esta en la cola retorna none o -1
            actual = self.primero
            indice = 0
            while actual:
                if actual.dato == dato:
                    return indice
                actual = actual.sig
                indice += 1
            return -1
        
    def posicion2( self, valor):
        lista = self.get_datos()
        posicion = lista.index(valor) if valor in lista else -1
        
        return posicion
        
    def get_datos(self): # Los datos en lista [], si es de 4 personas, dame las 4 personas en lista
            datos = []
            actual = self.primero
            while actual:
                datos.append(actual.dato)
                actual = actual.sig
            return datos


colas = Cola()

# cola.encolar("Jesus")
# cola.encolar("Maria")
# cola.encolar("Jose")
# cola.encolar("Santo")

# print(cola.posicion("Jose"))
# print(cola.posicion("Pepe"))

# print(cola.get_datos())