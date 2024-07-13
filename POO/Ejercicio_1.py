'''Persona: Realizar un programa que tenga una clase Persona con las siguientes características. 
La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, 
mostrar los datos e indicar si la persona es mayor de edad o no.'''

class Persona:
    def __init__(self,nombre,edad):
      self.nombre = nombre
      self.edad = edad
    def mayor_menor(self):
       if self.edad < 18:
         return "Menor de edad"
       return "Mayor de edad"
         

persona1 = Persona("Ejemplo", 2)

print(persona1.mayor_menor())







