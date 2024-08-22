class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaE:
    def __init__(self):
        self.head = None
        
    def insertar_al_principio(self,dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo

    def insertar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
        actual = self.head
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_al_principio(self):
        self.head = self.head.siguiente

    def eliminar_al_final(self):
        actual = self.head
        while actual.siguiente.siguiente:
            actual = actual.siguiente 
        actual.siguiente = None
    
    
    def imprimir_lista(self):
        actual = self.head
        contador = 0
        while actual:   
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
            contador = contador + 1
        print("\nTotal de elementos:", contador)

    def ordenamiento_burbuja(self):
        fin = None
        while fin != self.head:
            actual = self.head
            while actual.siguiente != fin:
                siguiente = actual.siguiente
                if actual.dato > siguiente.dato:
                    actual.dato, siguiente.dato = siguiente.dato, actual.dato
                actual = actual.siguiente
            fin = actual
                


prueba = ListaE()


prueba.insertar_al_principio(22)
prueba.imprimir_lista()
prueba.insertar_al_final(1887)
prueba.imprimir_lista()
