print("Conversión Hora")
print("**PROGRAMA PARA CONVERTIR LAS HORAS EN FORMATO DE 24 A 12 HORAS**")

#Inicializacion de variables 

h24 = 0
m24 = 0
h12 = 0
m12 = 0
periodo = str("a.m.")

#Datos de entrada

h24 = int(input("Ingrese la hora en formato 24 a transformar: "))

m24 = int(input("Ingrese los minutos a transformar: "))


#Proceso
periodo = "a.m"
if h24 >= 0 and h24 <= 24 and m24 >= 0 and m24 <= 60:
	if m24 == 60:
		h24 = h24 + 1
		m24 = 0
	else:
		m12 = m24
	if h24 >= 12:
		h12=h24-12
		periodo = "p.m"
	else:
		h12 = h24
	print(" El tiempo de " ,h24, " horas y " ,m24, " minutos, en formato de 24 horas ")
	print(" Equivale a " ,h12, " horas y " ,m12, " minutos " ,periodo)

else:
	print(" Los datos son incorrectos ")

