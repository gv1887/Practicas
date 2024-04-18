'''
Mascota:Cree la clase Mascota con los siguientes métodos y atributos:
Atributos:
nombre : string
raza : string
edad : int
Métodos:
Método constructor con todos los atributos pasados por parámetro. (__init__)
saludar: retorna el nombre, la raza y la edad en un solo string.
Debe probar el programa creando instancias de la clase.
'''
class Mascota:
    def __init__(self,nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = int(edad)

Perro_1 = Mascota ("Mora","Mestizo",5)
Perro_2 = Mascota ("Evans","Mestizo",1)

def saludar(nombre,raza,edad):
    print(f"El nombre es: {nombre}\nSu raza es: {raza}\nSu edad es: {edad}")
    #print(f"El nombre es: {nombre},","Su raza es: ,","Su edad es:")

llamada = saludar(Perro_1.nombre,Perro_1.raza,Perro_1.edad)

