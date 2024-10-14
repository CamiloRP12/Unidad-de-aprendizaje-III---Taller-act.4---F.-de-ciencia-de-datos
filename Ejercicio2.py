lista1=[]
lista2=[]
lista3=[]

#Iniciaremos limitando el número de interacciones del bucle a 5
for i in range(5):
    #Ahora iniciaremos el bucle de si es verdadero puede continuar, si no, dará otra respuesta
    while True:
        try:
            #Usaremos al igual que el ejercicio anterior el \n para dar claridad a las respuestas del programa
            #Se usó el int para que el valor sea tomado como entero, y de paso se usó el input para que el porgrama entienda
            #que se le está pidiendo un dato al usuario sin el cual no podrá continuar
            numero=int(input(f"\nHola hola! por favor introduce el número {i+1} para la lista1: "))
            lista1.append(numero)
            break
        #Habiendo usado el try con el except (igual que en el ejercicio anter), 
        #evitamos que si el programa bota error se detenga, y le damos la opción de que continue de otra forma
        except ValueError:
            print("\nMomento momento, acabas de colocar algo diferente a un número?, intenta de nuevo!")
            
#Mismo proceso para obtener la info para la lista2            
for i in range(5):
    while True:
        try:
            numero=int(input(f"\nGenial, ahora por favor introduce el número {i+1} para la lista2: "))
            lista2.append(numero)
            break
        except ValueError:
            print("\nMomento momento, acabas de colocar algo diferente a un número?, intenta de nuevo!")
for i in range(5):
    lista3.append(lista1[i]+lista2[i])

print(f"\nlista1:{lista1}")
print(f"lista2:{lista2}")
print(f"\nlista3(es el resultado de la suma de la lista1 y la lista2):{lista3}")