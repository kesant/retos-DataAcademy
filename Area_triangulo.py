import math
def definicion(a,b,c):
    if a==b and b ==c :
        forma="equilatero"
        altura=( math.sqrt(3)*a)/2
        base=a
    elif (a!=b and b ==c):
        forma = "isoceles"
        altura=math.sqrt((b**2)-((a**2)/4))
        base=a
    elif (a==b and b !=c) :
        forma = "isoceles"
        altura=math.sqrt((a**2)-((b**2)/4))
        base=c
    elif (a==c and c !=b) :
        forma = "isoceles"
        altura=math.sqrt((a**2)-((c**2)/4))
        base=b   
    elif(a!=b and b !=c):
        forma="rectangulo"
        altura=a*b/c
        base=b
    return forma,altura,base    

def Area_del_triangulo (altura,base):
    area=(base*altura)/2
    return area
def run():
    a=float(input("ingrese un lado del triangulo:"))
    b=float(input("ingrese el otro  lado del triangulo:"))
    c=float(input("ingrese el otro lado  lado del triangulo:"))
    forma,altura,base=definicion(a,b,c)
    area=Area_del_triangulo(altura,base)
    print("El triangulo es : ",forma)
    print("El area del triangulo es : ",area )

if __name__=="__main__":
    run()
