print("Conversión Temperatura")
print("**PROGRAMA PARA TRANSFORMAR DE GRADOS CENTÍGRADOS A GRADOS FRARENHEIT Y A GRADOS KELVIN**")

#Inicializacion de variables 

gC = float(0)
gF = float(0)
gK = float(0)

#Datos de entrada

gC = float(input("Ingrese los graods centígrados: "))
gC = float(gC)

#Proceso

if gC > 0:
   gF = (gC * 9/5)+32
   gK = gC + 273.75
   print(" La equivalencia en grados F es: " ,gF)
   print(" La equivalencia en grados K es: " ,gK)
            