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

#Ejercicio 8

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

payasos= 112
muñecas= 75
print('Cuantos payasos se vendieron? ')
paven=int(input())
print('Cuantas muñecas se vendieron? ')
muñven=int(input())
pesodelpaquete=((payasos*paven)+(muñecas*muñven))
print("El peso del contenedor es ", pesodelpaquete )
if pesodelpaquete > 3000 : print('Desea enviar el contenedor? ')
respuesta=input()
si=input()
no=input()
if respuesta == si : print("Contenedor enviado ")
if respuesta == no : print("Contenedor NO enviado ")