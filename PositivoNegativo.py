print("PositivoNegativo")
print("**PROGRAMA PARA SABER SI UN NÚMERO ES POSITIVO O NEGATIVO**")

#Declaración de variables

n = 0
srt = ""

#Datos de entrada

n = int(input("Ingrese un número diferente a cero: "))
n = int(n)

#Proceso

if n > 0:
	print("El número" ,n, "es positivo")
else:
	print("El número" ,n, "es negativo")