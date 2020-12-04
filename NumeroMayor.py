print("Número Mayor")
print("**PROGRAMA PARA SABER EL MAYOR DE TRES NÚMEROS**")

print("ESTRUCTURA CONCIONAL SIMPLE")

#Inicialización de variables 

N1 = 0
N2 = 0
N3 = 0
str = ""

#Ingresar los datos de entrada

N1 = int(input("Ingrese un número: "))
N1 = int(N1)
N2 = int(input("Ingrese un número: "))
N2 = int(N2)
N3 = int(input("Ingrese un número: "))
N3 = int(N3)

#Proceso

if N1 > N2 and N1 > N3:
	print(" El número: " ,N1, " es mayor")
        
if N2 > N3 and N2 > N1:
    print(" El número: " ,N2, " es mayor")
        
if N3 > N2 and N3 > N1:
	print(" El número: " ,N3, " es mayor")


print("ESTRUCTURA CONCIONAL COMPUESTA")

#Ingresar los datos de entrada

N1 = int(input("Ingrese un número: "))
N1 = int(N1)
N2 = int(input("Ingrese un número: "))
N2 = int(N2)
N3 = int(input("Ingrese un número: "))
N3 = int(N3)

#Proceso

if N1 > N2 and N1 > N3:
	str = "Mayor"
	print(" El número: " ,N1, " es " ,str)

else:
	str = "Menor"

if N2 > N3 and N2 > N1:
    str = "Mayor"
    print(" El número: " ,N2, " es " ,str)
        
else:
    str = "Menor"

if N3 > N2 and N3 > N1:
   str = "Mayor"
   print(" El número: " ,N3, " es " ,str)

else:
    str  = "Menor"


print("ESTRUCTURA CONCIONAL ANIDADA")

#Ingresar los datos de entrada

N1 = int(input("Ingrese un número: "))
N1 = int(N1)
N2 = int(input("Ingrese un número: "))
N2 = int(N2)
N3 = int(input("Ingrese un número: "))
N3 = int(N3)

#Proceso

if N1 > N3: 
    if N1 > N2:    			
        print(" El " ,N1, " es Mayor")
            
if N2 > N1:
    if N2 > N3:
       print(" El " ,N2, " es Mayor")
              
if N3 > N1:
    if N3 > N2:
    	print(" El " ,N3, " es Mayor") 
       
