import time

class Cuenta:
    def __init__(self,user="",contraseña=""):
        self.user = user
        self.contraseña = contraseña


        

    def registro(self):
        count = 0
        while True:
            
            
            self.user = input("Ingrese usuario: ").lower().strip()
            if self.user == "":
                count +=1
                print("No puede estar vacio")
                if count > 3:
                    print("Superacion de intentos")
                    print("Saliendo")
                    print()
                    time.sleep(2)
                    exit()
            else:
                break
           
        while True:
            self.contraseña = input("Ingrese contraseña").lower().strip()
            if self.contraseña == "":
                print("No puede estar vacio")
            else:
                break
        
        print("Registro Exitoso")

       

    def login(self):
        while True:
            usuario = input("Introduzca nombre de ususario: ")
            contraseña = input("Introduzca contraseña de ususario: ")
            if usuario == self.user and contraseña == self.contraseña:
                print("inicio ")
                break
            else:
                print("Usuario o contraseña Invalido: ")
    def menu(self):
        print("Seleccione una opciòn:","\n1.Acceso","\n2.Registro ","\n3.Salir")
        opcion = input("Que desea hacer: ").lower()
        while True:
            if opcion == "1" or opcion == "acceso":
                self.login()
                break
            elif opcion == "2" or opcion == "registro":
                self.registro()
                break 
            elif opcion == "3" or opcion == "salir":
                print("Saliendo")
                time.sleep(2)
                break

            else:
                print ("Error")
                print()  
                self.menu()
                
cuenta1 = Cuenta()
cuenta1.menu()
