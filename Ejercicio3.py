#Escribir un programa en Python que guarde la temperatura mínima y máxima de los
#últimos 5 días. El programa debe recibir la información, almacenarla y mostrar:
#● La temperatura media de cada día
#● Los días con menor temperatura
#● Después de almacenar la información de los 5 días, el programa debe recinir una
#temperatura más por teclado y mostrar los días cuya temperatura máxima coincide
#con ella. si no existe ningún día se muestra un mensaje de información.


temperaturas_minimas=[]
temperaturas_maximas=[]

for i in range(5):
    while True:
        try:
            #Acá vamos a solicitar el dato de las temperaturas, el cual se agregará a las temperaturas ya registradas (que 
            #serán las que irá dando el ususario)
            #Se usó el float y no el int debido a que como el dato son temperaturas, nos sirve más que traiga decimales
            #a que sea un número entero
            minima=float(input(f"\nBuen día, por favor ingrese la tempratura minima registrada el día {i+1} de la semana: "))
            maxima=float(input(f"Buen día, por favor ingrese la tempratura máxima registrada el día {i+1} de la semana: "))
            temperaturas_minimas.append(minima)
            temperaturas_maximas.append(maxima)
            break
        except ValueError:
            print("Por favor agrega un valor válido, el que nos compartes no es válido")

#Ahora vamos a calcular la temperatura media de cada día
temperaturas_medias=[(temperaturas_minimas[i]+temperaturas_maximas[i])/2 for i in range(5)]

#Ya con eso mostramos la temperatura media de cada día
#Acá usamos el \n para que la respuesta sobre las temperaturas medias quede un enter más abajo, para resaltarlo y que
#sea más visible
print("\nTemperaturas medias de cada día: ") 
for i in range(5):
    print(f"Día {i+1}:{temperaturas_medias[i]:.2f}°") #Acá usamos el .2f para que el resultado solo tenga 2 decimales

#Ahora si procedemos a buscar el día con la menor temperatura y los días con menor temperatura
menor_temperatura=min(temperaturas_minimas)
dias_con_menor_temperatura=[i+1 for i in range(5) if temperaturas_minimas[i]==menor_temperatura]

print(f"\nLos días con la temperatura más baja ({menor_temperatura}°) son: {dias_con_menor_temperatura}")

#Ahora para el punto final se procede con los días de mayor temperatura
temperatura_dada_por_el_usuario=float(input("\nPor favor ingrese una temperatura para validar si coincide con\
 alguno de los días con temperatura más alta: "))
dias_con_temperatura_mas_alta=[i+1 for i in range(5) if temperaturas_maximas[i]==temperatura_dada_por_el_usuario]

#Por último se procede a dar el resultado de la búsqueda según la información dada por el usuario
if dias_con_temperatura_mas_alta:
    print(f"\nDías con temperatura más alta de {temperatura_dada_por_el_usuario}°:{dias_con_temperatura_mas_alta}")
else:
    print(f"\nNo se encontraron días con la temperatura más alta con el dato {temperatura_dada_por_el_usuario}")