#Mi Primer Programa 

#Ejercicio 1
#Guardar = ('Hola Mundo')
#print('Guardar')

#Ejercicio 3
#nombre=input("Escribe tu nombre: ")
#print ('Hola,'+ nombre + ' como estas?')

#Ejercicio 4 
#print(((3+2)/(2*5))**2)

#Ejercicio 5
#numerodehoras=float(input('Escribe tu numero de horas que trabajas: '))
#valordelahora=float(input('Escribe cuanto ganas a la hora en dinero: '))
#pagototal=str(numerodehoras*valordelahora)
#print('tu pago correspondiente debe ser ' + pagototal + ' pesos')

#Ejercicio 6
#enteropositivo=float(input('Introduzca un entero positivo del 1 al 20: '))
#entero=enteropositivo
#print('ahora realizare la siguiente operacion donde N es el entero positivo que pusiste, la formula es (N(N+1))/2')
#resultado=str((entero*(entero+1))/2)
#print('El Resultado Es: '+ resultado)

#Ejercicio 7
#peso=input('Introduzca su peso en Kg ')
#estatura=input('Introduzca su estatura en M ')
#print('Ahora calculare tu masa corporal')
#masacorporal=round(float(peso)/float(estatura)**2,2)
#print('tu masa corporal es ', masacorporal)

#Ejercicio 9
#interesanual=float(input('Cual es tu interes anual? '))
#años=float(input('Un numero de años para su ganancia '))
#capital=str((invertir)*(interesanual/((100+1)**años)))
#print('Tu capital obtenido es: ', capital )

#Ejercicio 10
#print('Introduzca un numero entero positivo ')
#enteropositivo=int(input())
#suma=((enteropositivo*(enteropositivo+1))/2)
#print("Se sumara desde 1 hasta el numero que seleccionaste")
#if suma > 20  : print(" es un gran numero! " , suma)
#print ("El resultado es " , suma)

#print('Hola, que cantidad deseas invertir? ')
#inversion=int(input())
#print('En cuantos años? ')
#años=int(input())
#print('Interes anual? ')
#interes=int(input())
#capital=(inversion*((interes/100)+ 1 )**años)
#if capital < 100000 : print("Baja Inversion " + str(capital))
#if capital > 1000000 : print("Es una buena inversion " + str(capital))
#if 100000 < capital > 1000000 : print("Rentabilidad Moderada " + str(capital))

#payasos= 112
#muñecas= 75
#print('Cuantos payasos se vendieron? ')
#paven=int(input())
#print('Cuantas muñecas se vendieron? ')
#muñven=int(input())
#pesodelpaquete=((payasos*paven)+(muñecas*muñven))
#print("El peso del contenedor es ", pesodelpaquete )
#if pesodelpaquete > 3000 : print('Desea enviar el contenedor? ')
#respuesta=input()
#si=input()
#no=input()
#if respuesta == si : print("Contenedor enviado ")
#if respuesta == no : print("Contenedor NO enviado ")

#ejercicio 1.1
#print("Ingrese un primer numero ")
#numuno=int(input())
#print("Ingrese un segundo numero ")
#numdos=int(input())
#def suma ( numuno,numdos ):
# return  numuno+numdos
#misuma= suma (numuno,numdos)
#print("El resultado de la suma es ", misuma)

#ejercicio 1.2
#print("Ingrese un primer numero ")
#numuno=int(input())
#print("Ingrese un segundo numero ")
#numdos=int(input())
#def suma ( numuno,numdos ):
# return  numuno-numdos
#misuma= suma (numuno,numdos)
#print("El resultado de la suma es ", misuma)

#Ejercicio 66
##d= inv
#if (d>0 and d<1000000) :
 # return 2
#elif(d>1000000 and d < 2000000) :
#  return 5
# else :
#   return 7

#def calBalance(imt, inv):
 # n=int
 # d=inv
#  return round((d*(1+(n/100))),2)
  
#def calAhorro():
 # #inversion,intereses,b1,b2,b3 = 0.0
#  inversion = float(input('Ingrese valor de la inversion: '))
#  intereses = intereses(inversion)
 # b1 =calBalance(interes,inversion)
 # b2 =calBalance(interes,b1)
 # b3 =calBalance(interes,b2)
 # print('Balance año 1: ' + str(b1) + 'Balance año 2: ' + str(b2) + 'Balance año 3: ' + str(b3))

#catAhorro()


#def maximo(a,b):
  #if a>b:
  # return a
  #else:
 #  return b

#def minimo(a,b):
 # if a<b: 
 #   return a
 # else:
 #   return b

#programa principal
#x=int(input("Un numero "))
#y=int(input("Otro numero "))
#print(maximo(x-3,minimo(x+2, y-5)))


#preciosiniva=(int(input("Ingrese el costo del estereo sin el IVA ")))
#descuento1 = (preciosiniva/0.10)
#marquita=int(input("Ingrese que marca tiene "))

#def descuento(presiosiniva):
#  if preciosiniva>=2000000:
#   return descuento1
#  else:
 #  return preciosiniva

#def segundodescuento(marquita)
#  if marquita == 'NOSY'
 # return 





#TALLER 1 
#1. 
#año = int(input("Ingrese un año para saber si es biciesto o no: "))
#if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#    print(año, "es bisiesto")
#else:
#    print(año, "no es bisiesto")


#2. 
#altura = float(input("Ingrese la altura del perro en centímetros: "))
#peso = float(input("Ingrese el peso del perro en kilogramos: "))

#if altura <= 30 and peso <= 15:
 #   tamaño = "Pequeño"
  
#elif 30 < altura <= 40 and 15 < peso <= 25:
 #   tamaño = "Mediano"
  
#elif 40 < altura <= 60 and 25 < peso <= 45:
#    tamaño = "Grande"
  
#else:
#    tamaño = "Nosesabe"

#if tamaño != "Nosesabe":
   # print("El perro es " ,(tamaño))
#else:
   # print("No se puede saber su tamaño. ")


#3. 
#temperaturainicial = float(input("Ingrese la temperatura: "))
#escalainicial = input("Ingrese la escala de temperatura actual (Celsius, Fahrenheit, o Kelvin): ").capitalize()
#escalaaconvertir = input("Ingrese la escala a la que desea convertir (Celsius, Fahrenheit, o Kelvin): ").capitalize()
#if escalainicial == "Celsius" and escalaaconvertir == "Fahrenheit":
#    temperaturaconvertida = temperaturainicial * 9/5 + 32
#    unidad_destino = "Fahrenheit"
#elif escalainicial == "Celsius" and escalaaconvertir == "Kelvin":
#    temperaturaconvertida = temperaturainicial + 273.15
#    unidad_destino = "Kelvin"
#elif escalainicial == "Fahrenheit" and escalaaconvertir == "Celsius":
#    temperaturaconvertida = (temperaturainicial - 32) * 5/9
#    unidad_destino = "Celsius"
#elif escalainicial == "Fahrenheit" and escalaaconvertir == "Kelvin":
#    temperaturaconvertida = (temperaturainicial - 32) * 5/9 + 273.15
#    unidad_destino = "Kelvin"
#elif escalainicial == "Kelvin" and escalaaconvertir == "Celsius":
#    temperaturaconvertida = temperaturainicial - 273.15
#    unidad_destino = "Celsius"
#elif escalainicial == "Kelvin" and escalaaconvertir == "Fahrenheit":
#    temperaturaconvertida = (temperaturainicial - 273.15) * 9/5 + 32
#    unidad_destino = "Fahrenheit"
#else:
#    print("Las escalas ingresadas no son válidas.")
#    temperaturaconvertida = None
#    unidad_destino = ""

#if temperaturaconvertida is not None:
#    print(f"La temperatura convertida es {temperaturaconvertida} {unidad_destino}.")


#4.

#nombre = input("Ingrese el nombre del participante: ")
#edad = int(input("Ingrese la edad del participante: "))
#grupo = ""
#costo = 0

#if edad >= 10 and edad <= 17:
 #   grupo = "Niños"
  #  costo = 25000
#    if edad >= 10 and edad <= 13:
 #       costo *= 0.85  
  #  elif edad > 17:
   #     costo *= 0.92  
#elif edad >= 18 and edad <= 50:
 #   grupo = "Adultos"
  #  costo = 35000
   # if edad >= 18 and edad <= 30:
    #    costo *= 0.89  
    #elif edad > 30:
     #   costo *= 0.91  
#elif edad > 50:
 #   grupo = "Adulto Mayor"
  #  costo = 50000
   # if edad > 65:
    #    costo *= 0.6  

#print(f"Nombre del participante: {nombre}")
#print(f"Grupo: {grupo}")
#print(f"Costo original: ${costo:,.0f}")
#print(f"Valor a pagar con descuento: ${costo:,.0f}")

#5.
#import math
#tipo_recipiente = input("Seleccione el tipo de recipiente (Cubo, Cilindro o Esfera): ").capitalize()
#volumen = 0.0

#if tipo_recipiente == "Cubo":
  #  lado = float(input("Ingrese el lado del cubo: "))
   # volumen = lado ** 3
#elif tipo_recipiente == "Cilindro":
#    radio = float(input("Ingrese el radio de la base del cilindro: "))
#    altura = float(input("Ingrese la altura del cilindro: "))
 #   volumen = math.pi * radio**2 * altura
#elif tipo_recipiente == "Esfera":
 #   radio = float(input("Ingrese el radio de la esfera: "))
  #  volumen = (4/3) * math.pi * radio**3
#else:
 #   print("Tipo de recipiente no válido.")

#if volumen > 0:
 #   print(f"El volumen del {tipo_recipiente} es {volumen:.2f} unidades cúbicas.")

#6.
#cantidad_cubos = int(input("Ingrese la cantidad de cubos Rubik a enviar: "))
#tipo_caja = input("Ingrese el tipo de caja (Pequeña, Mediana, Grande o Extragrande): ").lower()
#volumen_total = cantidad_cubos * 167
#tamaño_caja_litros = 0

#if tipo_caja == "pequeña":
#    tamaño_caja_litros = 5
#elif tipo_caja == "mediana":
#    tamaño_caja_litros = 7
#elif tipo_caja == "grande":
#    tamaño_caja_litros = 10
#elif tipo_caja == "extragrande":
#    tamaño_caja_litros = 15
#else:
#    print("Tipo de caja no válido.")
#    exit()

#cantidad_cajas = volumen_total / (tamaño_caja_litros * 1000) 

#if cantidad_cajas.is_integer():
#    print(f"Se necesitan {int(cantidad_cajas)} cajas de tipo {tipo_caja.capitalize()} para el envío.")
#else:
#    print(f"Se necesitan {int(cantidad_cajas) + 1} cajas de tipo {tipo_caja.capitalize()} para el envío.")


#Valorjamón= 7000
#ValorArepas= 6000
#Valorpantajado= 6500

#jamon=input('Cantidad a comprar jamon ')
#arepas=input('Cantidad a comprar arepas ')
#pantajado=input('Cantidad a comprar pan tajado ')

#def Totaljamon():
 #if jamon == 2:
  # print("Descuento es" , (Valorjamón*2))
# elif jamon > 2 and jamon < 5:
 # print("Descuento es " , ((Valorjamón*jamon) *0.5))
 #elif jamon >= 5:
  #print("Descuento es " , (Valorjamón*jamon)-Valorjamón)
  #return print("El costo es " , Valorjamón)

#Totalarepas=(ValorArepas*arepas)
#print("El costo total de las arepas es de " , Totalarepas)

    






'''#CORTE 2

A=0
while A<10:
  print(A)
  A=A+1
'''
'''
def Menu():
 
def suma():
  a=float(input("Ingrese el PRIMER numero para sumar "))
  b=float(input("Ingrese el SEGUNDO numero para sumar "))
  return a+b

def resta():
  c=float(input("Ingrese el PRIMER numero a restar "))
  d=float(input("Ingrese el SEGUNDO numero a restar "))
  return c-d

def multiplicacion():
  e=float(input("Ingrese el PRIMER numero a multiplicar "))
  f=float(input("Ingresar el SEGUNDO numero a restar "))
  return e*f

def division():
  g=float(input("Ingrese el PRIMER numero a dividir (numerador) "))
  h=float(input("Ingrese el SEGUNDO numero a dividir (denominador) "))
  if h==0:
     print("Error en la division ")
  else:
    return g/h

def Calculadora():
   Menu()
   opcion=0

  while opcion != 5:

   opcion = int(input('Selecciona una opcion '))
  
   if (opcion==1):
      print ("La suma es: ", suma())
   elif (opcion==2):
      print("La resta es: ", resta())
   elif (opcion==3):
      print("La multiplicacion es: ", multiplicacion())
   elif (opcion==4):
      print("La division es: ", division())
   elif(opcion==5):
      print("Se agotaron las opciones, adios")
   else:
     print("La opcion es invalida ")
  
Calculadora() 
'''
'''
for c in range(1,5,1):
   print(c)
'''
'''
print ("Hola, adivina un numero aleatorio de 1 a 100")

import random
def adivina():
  numerorandom = random.randint(1,100)
  adivinado = False 
  
  while not adivinado:    
    intento = int(input("Que numero crees que es? "))
    if intento == numerorandom:
     print("Felicidades! Acabas de acertarlo ")
     adivinado = True
    elif intento < numerorandom:
      print("El numero es mayor ")
    else: 
       print("El numero es menor ")

adivina()
'''
'''
numerousuario = int(input("Ingrese un numero "))

for tabla in range (1,11,1):
  print(numerousuario*tabla)      
'''

'''
def factorial():
  numero = int(input("Ingrese un numero para calcular su factorial "))
  factorial=1

  for i in range (1, numero + 1):
    factorial*= i

  print ("El factorial de tu numero es", factorial)

factorial()
'''
'''
lista=["gato","perro"] + ["caballo","serpiente"]
lista.append("gallina")
print(lista)
'''
'''
uno=input('A continuacion coloque 5 caracteres para enlistarlos ')
dos=input('Segundo caracter ')
tres=input('Tercer caracter ')
cuatro=input('Cuarto caracter ')
cinco=input('Quinto caracter ')

lista=[uno , dos , tres , cuatro , cinco]
print(lista)
'''
'''
def notasLista():
  notas = []
  for indice in range(1,6):
    while True:
      nota = int(input("Introduce la nota "))
      if nota>=0 and nota<=10: break
    notas.append(nota)

  print("Notas: ")
  for nota in notas:
    print(nota)

  print()
  print("Nota media: " ,sum(notas)/len(notas))
  print("Nota Max: ",max(notas))
  print("Nota Min: ",min(notas))

notasLista()
'''
'''
def listanumeros():
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for list in range(1, 11):
    print(numeros[-list], end=", ")
listanumeros()
'''
'''
def listanumeros():
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  numeros.reverse()
  
  for lista in numeros:
    print(lista, end=", ")
listanumeros()
'''

def listaAsignaturas():
  materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
  for Materia in range(len(materias)-1, -1, -1):
    Notas= float(input("Cual es su nota final de la asignatura "+ materias[Materia] + "?"))
    if Notas >= 3:
        materias.pop(Materia)
  print("Tienes que repetir " + str(materias))

listaAsignaturas()
 