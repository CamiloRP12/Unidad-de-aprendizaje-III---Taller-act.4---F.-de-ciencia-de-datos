#Escribir un programa en Python que declare una lista y la vaya llenando de números hasta
#que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los
#valores introducidos).

lista_de_numeros=[]

#Acá usamos While True para generar el bucle, y hasta que la condición no sea verdadera, romper el bucle
while True:
    try:
        #Se usa Int para que la entrada se presente como número entero
        numero=int(input("Buen día, por favor introduce el número que desees, pero recuerda\
 solo pueden ser números positivos: "))
        #Acá se coloca la condición de si el número es menor a 0, se rompa el bucle
        if numero <0:
            break
        #Con este punto vamos añadiendo los números a nuestra lista con .append
        lista_de_numeros.append(numero)
        #Y acá imprimimos pero con f (format) para poder incluir la variable lista_de_numeros dentro de la cadena de texto
        print(f"\nBien hecho, seguiste las indicaciones a cabalidad, la lista de números\
 introducidos hasta el momento es la siguiente: {lista_de_numeros}")
        #Habiendo usado el try con el except, evitamos que si el programa bota error se detenga, y le 
        #damos la opción de que continue de otra forma
    except ValueError:
        print("\nMmm parece que usaste un carácter que no es un número ni positivo ni\
 negativo (o en su defecto usaste un decimal), por favor intenta de nuevo")
    

print(f"\nOh como lo siento, la regla era solo usar números positivos, la lista de\
 números introducidos hasta el momento es la siguiente: {lista_de_numeros}")