print("Area Terreno")
print("**PROGRAMA PARA CALCULAR EL ÁREA DE UN TERREBO**")

#Declaracion e inicializacion de variables

ac = float(0)
b = float(0)
ar = float(0)
at = float(0)
area = float(0)

#Lectura de datos 

ac = float(input("Ingrese la altura del rectángulo: "))
b = float(input("Ingrese la base del rectángulo: "))

ar = ac*b
print('El área del cuadrado es ',ar)

at = (ac*b)//2
print('El área del triángulo es' ,at)

area = (ar + at)
print ('El área del terreno es' ,area)

print('El área del terreno es:', area , 'compuesto por un triangulo y un rectangulo de altura',ac ,'y un triangulo y rectangulo de base',b)


