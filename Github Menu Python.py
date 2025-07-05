https://github.com/Kaky2727
def saludar(nombre): 
    print("Holax", nombre)
    print("aqui hay una calculadora creada con python")


def sumar(): 
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: "))
    resultado= a + b
    print(resultado)


def restar():
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: ")) 
    resultado= a - b
    print(resultado)
 

def multiplicar():
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: ")) 
    resultado= a * b
    print(resultado)
  

def dividir():
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: ")) 
    resultado= a / b
    print(resultado)
 

def menu(): 
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


nombre=input("Ingrese su nombre: ")
saludar(nombre)
menu()
opcion=int(input("Ingrese una opción: "))
if opcion==1:
    sumar()   
elif opcion==2:
    restar()    
elif opcion==3:
    multiplicar()   
elif opcion==4:
    dividir()    
elif opcion==5:
    print("Adiós")
else:
    print("Opción inválida")

    print("Adiós")  

    