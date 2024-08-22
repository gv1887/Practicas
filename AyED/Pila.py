class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def estado_pila(self):
        if self.cima is None:
            print("No hay dato en la pila")
        else:
            print("Hay dato en la pila")

    def apilar (self,dato):
        nuevo_nodo = Nodo(dato)
        if self.cima == None:
            self.cima == nuevo_nodo
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        
    def desapilar(self):
        if self.cima == None:
            print ("No hay dato en la pila para desapilar")
        self.cima = self.cima.siguiente

    def imprimir(self):
        if self.cima == None:
            print("No hay dato en la pila")
        else:
            aux = self.cima
            while aux != None:
                print(aux.dato, "->" ,end=" ")
                aux = aux.siguiente
            print("None")

    def longitud(self):
        if self.cima == None:
            print("No hay dato en la pila")
        else:
            cont = 0
            aux = self.cima
            while aux != None:
                aux = aux.siguiente
                cont = cont + 1
            print(cont)
            
            





pila = Pila()

pila.apilar(22)
pila.apilar(23)
pila.apilar(24)
pila.apilar(25)
pila.desapilar()
pila.longitud()
# pila.estado_pila()