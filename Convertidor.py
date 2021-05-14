def convertidor():
    i=0
    while i==0:
        opcion=int(input("Por favor,ingre el numero de la opcion que quiera :"))       
        if opcion==1:
            usuario=float(input("Ingrese la cantidad que quiera convertir :"))
            resultado=usuario*1.609
            print("millas ", usuario)
            print("kilometros",resultado)
            i=1          
        elif opcion==2:
            usuario=float(input("Ingrese la cantidad que quiera convertir :"))
            resultado=usuario*0.614
            print("kilometros",usuario)
            print("millas ",resultado)
            i=1
        else:
            print("ingresa una opcion valida")    
                


   

def menu():
    print("""selecione una opcion :
    opcion 1: convertir de millas a kilometros
    opcion 2: convertir de kilometros a millas
    """)
    convertidor()
    
if  __name__=="__main__":
    menu()