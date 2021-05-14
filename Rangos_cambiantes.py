def main():
   limite_inferior=float(input("Ingrese el limite inferior: "))
   limite_superior=float(input("Ingrese el limite superior: "))
   comparador=float(input( "ingrese el numero a comparar: "))
   if comparador>=limite_inferior and comparador<=limite_superior:
       print("**************************************************************")
       print("tu numero esta dentro del rango establecido")
       print("El numero ",comparador, "esta dentro del limite")
   else:
       print("**************************************************************")
       print("El numero no esta dentro del limite")
if __name__=="__main__":
    main()