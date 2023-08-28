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
 # if a>b:
 #  return a
 # else:
 #   return b

#def minimo(a,b):
 # if a<b: 
   # return a
#  else:
  #  return b

#programa principal
#x=int(input("Un numero "))
#y=int(input("Otro numero "))
#print(maximo(x-3,minimo(x+2, y-5)))


preciosiniva=(int(input("Ingrese el costo del estereo sin el IVA ")))
descuento1 = (preciosiniva/0.10)
marquita=int(input("Ingrese que marca tiene "))

def descuento(presiosiniva):
  if preciosiniva>=2000000:
   return descuento1
  else:
   return preciosiniva

def segundodescuento(marquita)
  if marquita == 'NOSY'
  return 


