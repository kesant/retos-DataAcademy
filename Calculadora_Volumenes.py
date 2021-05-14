import math
def convertidor():
    i=0
    while i==0:
        opcion=int(input("Por favor,ingre el numero de la opcion que quiera :"))       
        if opcion==1:
            altura=float(input("Ingrese la altura del cilindro:"))
            radio=float(input("Ingrese el radio del cilindro:"))
            volumen=math.pi*(radio**2)*altura
            print("El volumen del cilindro es :", volumen)
            i=1
        elif opcion==2:
           altura=float(input("Ingrese la altura del cilindro:"))
           latitud=float(input("Ingrese la altura del latitud:"))
           longitud=float(input("Ingrese la altura del longitud:"))
           volumen=altura*longitud*latitud
           print("El volumen del cubo es :", volumen)
           i=1
        else:
            print("ingresa una opcion valida")    
                
def main():
    print("""Selecione la figura la cual quiere obtener el volumen :
    opcion 1: cilindro 
    opcion 2: cubo
    """)
    convertidor()

if  __name__=="__main__":
   main()