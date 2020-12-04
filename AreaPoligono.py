print("Área Poligono")
print("Programa para calcular el area de un poligono")

#	Declaración de variables

lc = 0 
at = 0
A = 0
A=lc**2
B = 0
D = 0
ats= 0
ar = 0
area = 0

# Lectura de datos

lc=float(input("Ingrese el lado de el cuadrado: "))

A = lc**2
print('El área de el cuadrado es: ',A)

at = float(input("Ingrese la altura de el triángulo: "))

B = (lc+at)/2
print('El área de el triángulo  es: ',B)

ar=float(input("Ingrese la altura de el rectangulo: "))

D=lc*ar
print ('El área de el rectangulo  es: ',D)

ats = at*3
print('EL área de los tres triángulos es: ',ats)

area = (A + ats + D)
print('El area polígono es: ' ,area)


# Salida de datos

print('El área del polígono compuesto es: ',area , 
	'compuesto por un cuadrado de lado' , lc,'un rectángulo de altura',
	 ar, 'y una altura de triángulo',at )