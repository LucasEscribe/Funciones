#Desafío 1:
'''
150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una
botella de PET puede tardar 1.000 años en desaparecer. 

Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se solicite tipo:
Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad
de años que tarda en degradarse.
'''
agnos_bolsa=150
agnos_PET=1000
agnos_tetrabrik=30
agnos_chicle=5

def tipo_elemento(elemento, tipo):
    if tipo==1:
        print(f"{elemento} tarda {agnos_bolsa} años en degradarse.")
    elif tipo==2:
        print(f"{elemento} tarda {agnos_PET} años en degradarse.")
    elif tipo==3:
        print(f"{elemento} tarda {agnos_tetrabrik} años en degradarse.")
    elif tipo==4:
        print(f"{elemento} tarda {agnos_chicle} años en degradarse.")
    else:
        print("Ingresó un dato incorrecto.")

try:       
    elemento = str(input("Ingrese el elemento: "))
    tipo = int(input("Escriba el número que coresponde al tipo de elemento:\n1 Bolsa de plástico\n2 Botella PET\n3 Envase tetrabrik\n4 Chicle\n"))
except ValueError:
    print("Ingresó un valor incorrecto.")
    exit()

tipo_elemento(elemento,tipo)


#Desafío 2:
'''
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas
de dos ciudades se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.
'''

def relacion(a, b):
    if a > b:
        print(f"La ciudad de {ciudad1} recicla más que {ciudad2}")
    elif b > a:
        print(f"La ciudad de {ciudad2} recicla más que {ciudad1}")
    elif b == a:
        print(f"{ciudad1} y {ciudad2} reciclan lo mismo")

try:
    ciudad1=str(input("Ingrese el nombre de la primer ciudad: "))
    ton1=int(input("Ingrese las toneladas recicladas de la primer ciudad: "))
    ciudad2=str(input("Ingrese el nombre de la segunda ciudad: "))
    ton2=int(input("Ingrese las toneladas recicladas de la segunda ciudad: "))
except ValueError:
    print("Ha ingresado datos incorrectos.")
    exit()

relacion(ton1,ton2)

#Desafío 3:
'''
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad
de árboles plantados en diferentes ciudades de Argentina durante la cuarentena.
Luego la función debe devolver dos listas ordenadas. La primera con las cantidades
que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
'''

cant_arboles_plantados=[11, 4946, 2, 154, 1, 0, 78, 164, 1698, 55, 99, 100]


def separar(lista):
    cant_arboles_mas100=list()
    cant_arboles_menos100=list()
    cant_ciudades_mas100=0
    
    for i in lista:
        if i > 100:
            cant_arboles_mas100.append(i)
            cant_ciudades_mas100 += 1
        elif 0<= i <= 100:
            cant_arboles_menos100.append(i)
        else:
            continue

    cant_arboles_mas100.sort()
    cant_arboles_menos100.sort()
    
    print("Lista con las cantidades de árboles mayores a 100: ", cant_arboles_mas100)
    print("Lista con las cantidades de árboles menor o igual a 100: ", cant_arboles_menos100)
    print("Cantidad de ciudades que han plantado más de 100 árboles durante cuarentena: ", cant_ciudades_mas100)

separar(cant_arboles_plantados)


#Calculadora Básica:

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	
	try:
		return num1/num2
	
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		return "Operación erronea"

while True:
	try:
		op1=(int(input("Introduzca el primer número: ")))

		op2=(int(input("Introduzca el segundo número: ")))

		break

	except ValueError:

		print("Debe ingresar sólo números enteros. Intente de nuevo.")
	
operacion=int(input("Introduzca la operación a realizar.\n1) suma\n2) resta\n3) multiplicación\n4) divide:\n"))

print("El resultado es: ")

if operacion==1:
	print(suma(op1,op2))

elif operacion==2:
	print(resta(op1,op2))

elif operacion==3:
	print(multiplica(op1,op2))

elif operacion==4:
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


# Ahorcado:

palabra_secreta=str.lower(input("Ingrese la palabra para ser adivinada: "))
intentos_ahorcado=6
pista = ["-"]*len(palabra_secreta)

def jugar(secreto):
    cont_intentos=0
    while cont_intentos < intentos_ahorcado:    
        letra=str.lower(input("¿Qué letra hay en la palabra: ?"))
    
        if letra in secreto and len(letra)==1:
            for i, l in enumerate(secreto):
                if l.lower() == letra.lower():
                    pista[i] = l
                    print(pista)
                    if not "-" in pista:
                        print("¡Ganaste!")
                        exit()
        else:
            print(f"La letra no está en la palabra.\nTe quedan {intentos_ahorcado-cont_intentos-1} intentos")
            cont_intentos+=1

jugar(palabra_secreta)