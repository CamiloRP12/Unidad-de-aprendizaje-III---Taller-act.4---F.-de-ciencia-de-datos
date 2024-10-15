# Cada grupo de estudiantes trabajará con dos grupos de datos (Gr1, Gr2) de 20 personas para un análisis de
# los datos se comparten a continuación

#Exportaremos la biblioteca pandas para la creación de las tablas de cada grupo de datos
#Exportaremos la biblioteca de numpy para poder trabajar con los datos numericos, así podremos realizar
#operaciones matemáticas y podremos ocuparnos de los valores nulos de las tablas, que vamos a ir reemplazando 
#con np.nan para representarlos como datos no númericos o indeifinidos
import pandas as pd
import numpy as np
#Exportaremos la biblioteca matplotlip.pyplot para poder crear los gráficos y le daremos el "alias" de
# plt por medio del as. Esto para que el código no quede tan cargado
import matplotlib.pyplot as plt
#Exportaremos la biblioteca seaborn, esta nos va a ayudar a realizar visualizaciones estadísticas (debido a que nos
#piden histogramas y diagramas de sectores)
import seaborn as sns

# Definir los datos de la tabla para el Grupo 1
data_grupo_1 = {
    "Sexo": ["Mujer", "Hombre", "Mujer", "Mujer", "Mujer", 
             "Hombre", "Mujer", "Hombre", "Hombre", "Mujer", 
             "Mujer", "Hombre", "Hombre", "Mujer", "Mujer", 
             "Hombre", "Mujer", "Mujer", "Mujer", "Mujer"],
    "Edad": [25, 30, 28, 20, 23, 
             22, 22, 22, 21, 21, 
             22, 20, 22, 29, 29, 
             21, 30, 21, 22, 23],
    "Estatura": [1.82, 1.83, 1.78, 1.79, 1.80, 
                 1.90, 1.79, 1.83, np.nan, 1.65, 
                 1.73, 1.79, 1.80, 1.77, 1.69, 
                 1.75, 1.66, np.nan, 1.79, 1.80],
    "Grupo Sanguíneo": ["A", "B", "A", "AB", "O",
                        "A", "B", "A", "B", "AB",
                        "A", "B", "O", "O", "A",
                        "B", "AB", "B", "B", "B"]
}
# Crear DataFrame
grupo_1 = pd.DataFrame(data_grupo_1)
print(grupo_1)

#Agregaremos una línea en blanco entre las dos tablas para que sea más fácil leerlas
print("\n")  

# Definir los datos de la tabla para el Grupo 2
data_grupo_2 = {
    "Sexo": ["Mujer", "Hombre", "Hombre", "Mujer", "Hombre", 
             "Hombre", "Mujer", "Hombre", "Hombre", "Mujer", 
             "Mujer", "Hombre", "Hombre", "Mujer", "Mujer", 
             "Hombre", "Mujer", "Hombre", "Mujer", "Hombre"],
    "Edad": [25, 30, 38, 26, 23, 
             22, 32, 26, 25, 28, 
             22, 30, 22, 39, 29, 
             25, 30, 23, 32, 33],
    "Estatura": [1.72, 1.73, 1.78, 1.79, 1.83, 
                 1.90, 1.79, 1.83, np.nan, 1.75, 
                 1.79, 1.79, 1.85, 1.77, 1.79, 
                 1.75, 1.66, np.nan, 1.79, 1.83],
    "Grupo Sanguíneo": ["B", "B", "A", "AB", "O",
                        "AB", "B", "B", "B", "AB",
                        "A", "B", "O", "O", "B",
                        "B", "A", "O", "B", "B"]
}
# Crear DataFrame
grupo_2 = pd.DataFrame(data_grupo_2)
print(grupo_2)



# --- Ahora procederemos con el punto 1, haremos un diagrama de sectores de la variable del grupo sanguineo, uno por cada 
#uno de los grupos

# Diagrama de Sectores para Grupo 1
#Se usará .figure para crear la nueva ventana para el gráfico nuevo y figsize se usará para darle el tamaño en pulgadas
# a esta ventana, 8 es el ancho y 6 la altura. Optar por usar figsize puede servir para gráficos más complejos, en este
#caso no era del todo necesario, pero se colocó para ver como funcionaba
plt.figure(figsize=(8, 6))
#Con el .value.counts() contaremos la cantidad de veces que aparece cada grupo sanguineo en la tabla/dataframe 
#plot.pie para elegir el tipo de gráfico, el cual será la torta
#Con el autopct="%1.1f%%" se controlará cómo se muestran los % en el gráfico. El 1.1f nos ayudará a que solo se 
# muestre un decimal, el %% sirve para que los valores se muestren con un %
grupo_1["Grupo Sanguíneo"].value_counts().plot.pie(autopct='%1.1f%%', colors=["blue", "yellow", "pink", "green"])
plt.title("Distribución del Grupo Sanguíneo en el Grupo 1")
plt.ylabel("")  
plt.show()

# Diagrama de Sectores para Grupo 2
plt.figure(figsize=(8, 6))
grupo_2["Grupo Sanguíneo"].value_counts().plot.pie(autopct='%1.1f%%', colors=["blue", "yellow", "pink", "green"])
plt.title("Distribución del Grupo Sanguíneo en el Grupo 2")
plt.ylabel("")  # Quitar la etiqueta del eje y
plt.show()

# --- Ahora procederemos con el punto 2, representando el histogramade la estatura para cada uno de los grupos
#Acá crearemos los histogramas por medio de seaborn, usaremos matplotlib.pyplot para crear la ventana para poder
# generar el gráfico, y seaborn para ya generar el histograma como tal

# Histograma para Grupo 1
plt.figure(figsize=(8, 6))
#Con histplot se crea el histograma, para cada grupo se traerá la variable estatura, con bins se definirá el número de 
# intervalos en los que definiremos el gráfico, las barras serán azules y con kde agregaremos una Estimación de 
# Densidad de Kernel para superponer una curva que representa la densidad de la probabilidad de los datos mostrando
# las áreas donde los valores son más densamente agrupados; así nos ayudamos paraa visualizar mejor la forma general 
# de la distribución de los datos
sns.histplot(grupo_1["Estatura"], bins=10, color='blue', kde=True)
plt.title("Histograma de Estatura en el Grupo 1")
plt.xlabel("Estatura (m)")
plt.ylabel("Frecuencia")
plt.show()

# Histograma para Grupo 2
plt.figure(figsize=(8, 6))
sns.histplot(grupo_2["Estatura"], bins=10, color='blue', kde=True)
plt.title("Histograma de Estatura en el Grupo 2")
plt.xlabel("Estatura (m)")
plt.ylabel("Frecuencia")
plt.show()


# --- Ahora procederemos con el punto 3, encontrar los datos atipicos en la edad de ambos grupos, para ello debemos tener en 
#cuenta que:
#Un dato atípico es un valor que se encuentra significativamente alejado de los demás en un conjunto de datos.
#Para lo cual utilizaremos el método IQR que es el método del rango intercuartílico, en el cual tendremos en cuenta 
#la diferencia entre el Q1 (25% de los datos están por debajo de este valor) y Q3 (75% de los datos están por debajo 
# de este valor)

# Datos atípicos en el Grupo 1 (grupo_1)
#Primero definiremos las variables de los datos atípicos/outliers, las variables contendrán, de cada grupo, 

#La técnica de detección de valores atípicos que se está utilizando aquí se basa en el rango intercuartílico (IQR).
#  Un valor se considera atípico si se encuentra por debajo de Q1 - 1.5 * IQR o por encima de Q3 + 1.5 * IQR donde Q1
# es el primer cuartil y Q3 es es el tercer cuartil. El IQR se calcula como IQR=Q3-Q1

#Se procede con la creación de un nuevo DataFrame llamado grupo_1_outliers para cada grupo
#Con esto encontramos el Q1: grupo_1["Edad"].quantile(0.25)
grupo_1_outliers = grupo_1[(grupo_1["Edad"] < (grupo_1["Edad"].quantile(0.25) - 1.5 * 
     (grupo_1["Edad"].quantile(0.75) - grupo_1["Edad"].quantile(0.25)))) | 
#Con esto encontramos el Q3: grupo_1["Edad"].quantile(0.75)
    (grupo_1["Edad"] > (grupo_1["Edad"].quantile(0.75) + 1.5 * 
#Con esto encontramos el IQR: (grupo_1["Edad"].quantile(0.75) - grupo_1["Edad"].quantile(0.25))
     (grupo_1["Edad"].quantile(0.75) - grupo_1["Edad"].quantile(0.25))))
]
#La condición principal que se está utilizando para identificar los valores atípicos está dividida en dos partes, 
# conectadas por el operador lógico |, que significa "o". Esto indica que se seleccionarán los registros que cumplan 
# cualquiera de las dos condiciones

# Datos atípicos en el Grupo 2 (grupo_2)
grupo_2_outliers = grupo_2[(grupo_2["Edad"] < (grupo_2["Edad"].quantile(0.25) - 1.5 * 
     (grupo_2["Edad"].quantile(0.75) - grupo_2["Edad"].quantile(0.25)))) | 
    (grupo_2["Edad"] > (grupo_2["Edad"].quantile(0.75) + 1.5 * 
     (grupo_2["Edad"].quantile(0.75) - grupo_2["Edad"].quantile(0.25))))
]


#Y así es como estableceremos el límite inferior y el límite superior para la búsqueda de los valores atípicos
# Q1 - 1.5 * IQR o por encima de Q3 + 1.5 * IQR

# Mostrar resultados
#Si estos muestran el mensaje Empty DataFrame significa que no hay datos atípicos (o sea no hay filas para las columnas), 
# si bien la respuesta mostrará el esquema definido (columnas) del DataFrame que es Columns: [Sexo, Edad, Estatura, 
# Grupo Sanguíneo], no hay individuos que cumplan con las condiciones que definimos para identificar datos atípicos en la edad
print("\n")
print("Datos atípicos en el Grupo 1:")
print(grupo_1_outliers)

print("\n")
print("Datos atípicos en el Grupo 2:")
print(grupo_2_outliers)

#LA RESPUESTA PARA EL PUNTO 3 ES: NO, NO HAY DATOS ATÍPICOS EN LA VARIABLE DE EDAD DE AMBOS GRUPOS



# --- Ahora procederemos con el punto 4, para el cual hallaremos el valor máximo del 40% de las estaturas más pequeñas del 
# grupo A y el valor mínimo del 30% de las estaturas mayores del grupo B
#  


# Valor máximo del 40% de las estaturas más pequeñas en el Grupo 1
#Acá ordenaremos las estaturas con .sort_values de manera ascendente
grupo_a_1_sorted = grupo_1["Estatura"].sort_values()

#Con .iloc accederemos a una fila específica usando su índice
#Con int haremos que el resultado sea un entero
#Con len obtendremos la longitud del objeto usado como argumento, es decir de la estatura del grupo 1
#Como piden hacer el ejercicio sobre el 40%, se procede a multiplicar por 0.4
# -1 porque el índice inicia en 0
valor_maximo_40 = grupo_a_1_sorted.iloc[int(len(grupo_a_1_sorted) * 0.4) - 1]  

# Valor mínimo del 30% de las estaturas mayores en el Grupo 2
#Acá ordenaremos las estaturas con .sort_values de manera descendente con ayuda del ascending=False y haremos el resto igual 
grupo_b_2_sorted = grupo_2["Estatura"].sort_values(ascending=False)
valor_minimo_30 = grupo_b_2_sorted.iloc[int(len(grupo_b_2_sorted) * 0.3) - 1]  

print("\n")
print("Valor máximo del 40% de las estaturas más pequeñas en el Grupo 1:", valor_maximo_40)
print("\n")
print("Valor mínimo del 30% de las estaturas mayores en el Grupo 2:", valor_minimo_30)

#LA RESPUESTA PARA EL VALOR MÁXIMO DEL 40% DE LAS ESTATURAS MÁS PEQUEÑAS DEL GRUPO A ES 1.79, Y LA RESPUESTA PARA EL VALOR
#MÍNIMO DEL 30% DE LAS ESTATURAS MAYORES DEL GRUPO B ES 1.79

# --- Ahora procederemos con el punto 5, donde buscaremos si las variables de edad y estatura son más homogéneas en el grupo
#A o en el B

# Cálculo de la desviación estándar para Edad y Estatura en ambos grupos por medio de .std
# La desviación estándar mide cuánto varían los datos respecto a su media. Si los datos están muy dispersos, la desviación 
# estándar será alta, y si están muy agrupados cerca de la media, la desviación será baja.
homogeneidad_edad = {
    "Grupo 1": grupo_1["Edad"].std().round(2),
    "Grupo 2": grupo_2["Edad"].std().round(2)
}

homogeneidad_estatura = {
    "Grupo 1": grupo_1["Estatura"].std().round(2),
    "Grupo 2": grupo_2["Estatura"].std().round(2)
}
print("\n")
print("Desviación estándar de Edad:")
print(homogeneidad_edad)

print("\n")
print("Desviación estándar de Estatura:")
print(homogeneidad_estatura)

#LA RESPUESTA A EN QUE GRUPO LA VARIABLE DE EDAD ES MÁS HOMOGENEA ES EN EL GRUPO A CON UNA DESVIACIÓN ESTÁNDAR DE APENAS 3.48
#EN COMPARACIÓN CON LA DESVIACIÓN DE 5.05 DEL GRUPO B
#LA RESPUESTA A EN QUE GRUPO LA VARIABLE DE ESTATURA ES MÁS HOMOGENEA ES EN EL GRUPO B CON UNA DESVIACIÓN ESTÁNDAR DE APENAS 0.05
#EN COMPARACIÓN CON LA DESVIACIÓN DE 0.06 DEL GRUPO A


# --- Ahora procederemos con el punto 6, donde nos piden saber en qué grupo presentan los individuos la altura media mayor y 
# la altura mediana menor

# Altura media
#Para hallar la media se usará .mean para cada grupo
media_altura = {
    "Grupo 1": grupo_1["Estatura"].mean().round(2),
    "Grupo 2": grupo_2["Estatura"].mean().round(2)
}

# Altura mediana
#Para hallar la mediana se usará .median para cada grupo
mediana_altura = {
    "Grupo 1": grupo_1["Estatura"].median().round(2),
    "Grupo 2": grupo_2["Estatura"].median().round(2)
}

print("\n")
print("Altura media:")
print(media_altura)

print("\n")
print("Altura mediana:")
print(mediana_altura)

#LA RESPUESTA A QUÉ GRUPO DE INDIVIDUOS REPRESENTA UNA ALTURA MEDIA MAYOR ES EL GRUPO B CON 1.79 POR ENCIMA DE LA MEDIA DEL
#GRUPO A CON 1.78. RESPECTO DE LA ALTURA MEDIANA MENOR SE PRESENTA UN EMPATO PUES AMBOS GRUPOS TIENEN ALTURA MEDIANA DE 1.79



# --- Ahora procederemos con el punto 7, donde nos piden estudiar la asimetría y la curtosis de la estatura del grupo A, para lo
#cual es importante tener en cuenta:

#La asimetría mide qué tan "desbalanceada" o "sesgada" está una distribución con respecto a su media. Nos dice si los datos están 
# distribuidos simétricamente o si hay una inclinación hacia un lado.
#La curtosis mide la "altura" y "ancho" de las colas de la distribución. En otras palabras, indica si los datos tienen una mayor 
# o menor concentración de valores en los extremos (colas) en comparación con una distribución normal

# Asimetría y Curtosis de la Estatura del Grupo 1
#Para hallar la asimetría podemos usar .skew y para hallar la curtosis podemos usar .kurtosis
asimetria_a = grupo_1["Estatura"].skew().round(2)
curtosis_a = grupo_1["Estatura"].kurtosis().round(2)

print("\n")
print("Asimetría y Curtosis del Grupo 1:")
print("Asimetría:", asimetria_a)
print("Curtosis:", curtosis_a)



# --- Ahora procederemos con el punto 8, las conclusiones a las que se pudo llegaron fueron las siguientes

# Para ambos grupos de datos no se presentan datos atípicos en las edades, lo que significa que las edades son consistentes
# y se encuentran dentro de un rango esperado
# Respecto de la altura, ambos grupos comparten datos muy similares, son una media que difiere por casi nada y una mediana 
# exactamente igual
# Los datos de la asimetría y la curtosis del grupo 1 respecto de la altura, nos dan a entender que los datos no son 
# simétricos, adicional a ello según la curtosis los datos no presentan demasiados valores extremos ni outliers






