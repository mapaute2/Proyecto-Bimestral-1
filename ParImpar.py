print("NúmeroParImpar")
print("**PROGRAMA PARA VERIFICAR SI UN NÚMERO ES PAR O IMPAR**")

#Declaración de variables

num = 0
 
#Entrada de datos

num = int(input("Ingrese un número a verificar: "))
num = int(num)

#Proceso

if num%2 == 0:
	print("El número" ,num, "es par")
	
else:
	print("El número" ,num, "es impar")