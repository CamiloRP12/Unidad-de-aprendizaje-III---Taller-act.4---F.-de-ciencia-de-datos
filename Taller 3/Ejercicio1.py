#Ejercicio 1
#Cada grupo de estudiantes debe crear un conjunto de datos de 30 estudiantes de un curso de Fundamentos de ciencia de datos, 
# los datos que se deben relacionar por cada estudiante son:
#● Sexo
#● Edad,
#● Estatura
#● Nota
#● Ciudad
#Con estos datos y usando la herramienta RStudio cada grupo debe:
#1. Realizar una tabla de frecuencias absolutas y otra de frecuencias relativas para la variable Calificación. Almacena las 
#tablas anteriores en dos variables y llámalas absolutas y relativas.
#2. Representar la variable ciudad mediante un diagrama de barras y un diagrama de sectores. Incluye un título adecuado 
# para cada gráfico y colorea las barras y los sectores de colores diferentes.
#3. Para la variable Edad, realizar un histograma y un diagrama de caja y bigotes considerando la opción range = 1.5. 
# Incluye un título apropiado para cada gráfico y colorea las barras del histograma de color amarillo. 
# ¿Existe algún valor atípico en esta variable? Reduce el valor del argumento range hasta 0.5. ¿Varían las conclusiones?
#4. Realizar un resumen de la variable Puntuación mediante la orden summary. Comprueba que las medidas que proporciona 
# summary coinciden con las medidas calculadas de forma individual usando su función específica.
#5. Calcular la estatura media de los estudiantes y proporcionar al menos, dos medidas que indiquen la dispersión de 
# esta variable.
#6. Finalmente se espera que el grupo presente las conclusiones a las que puede llegar con el desarrollo del taller



#!!!__ Primero iniciaremos creando los datos de los 30 estudiantes, para ello vamos a importar dos bibliotecas: pandas 
# (para crear y manipular los DataFrames/las tablas) y numpy (para poder generar el contenido de las tablas, lo que 
# vienen siendo los datos numéricos)
import pandas as pd
import numpy as np

#Acá usamos random.seed para generar los valores "aleatorios", pero nos ayudamos con el seed para que estos sigan un patrón
#determinista, es decir, para que ya sea el profe o cualquier persona, al ejecutar el código obtenga de manera "aleatoria" los
#mismo resultados que yo o que cualquier otro compañero. Lo que vendría a ser sembrar una semilla
np.random.seed(123)  

#Acá se usa el np.random para usar numpy con un valor aleatorio según sea el caso, y choise (sirve para dar aleatoriedad
# respecto de las opciones que damos tipo Masculino o Femenino), 
sexo = np.random.choice(["Masculino", "Femenino"], size=30)
#randint(nos ayudará a dar número aleatorios ENTEROS entre el rango proporcionado que para este caso será 18 a 40 años)
#Para la función random es importante tener en cuenta que se maneja de la siguiente forma np.random.randint(low, high, size) 
#por lo que si se quiere ir hasta los 40 años será (18, 41) pues el high representa el valor máximo excluido
edad = np.random.randint(18, 41, size=30)
#Usaremos el .round(1) para limitar los decimales y lograr así que la información se pueda leer fácilmente
estatura = np.random.uniform(150, 191, size=30).round(1)
#uniform (nos ayudará a dar número aleatorios DECIMALES entre el rango proporcionado que para este caso será 0 a 10)
nota = np.random.uniform(0, 10, size=30).round(2)
ciudad = np.random.choice(["Bogota", "Medellin", "Cartagena"], size=30)

#Acá se crea el DataFrame o lo que viene siendo la tabla la cual se llamará df
df = pd.DataFrame({
    "Sexo": sexo,
    "Edad": edad,
    "Estatura": estatura,
    "Nota": nota,
    "Ciudad": ciudad
})
#Acá se usará el head sobre el df para ver solamente los primeros 5 registros de la tabla y no imprimir los 30 sin necesidad
print(df.head())  

#Una vez tenemos la base de datos armada, procedemos con el punto 1 que pide variables con tablas de frecuencias absolutas y de 
# frecuencias relativas para la variable calificación

#Las frecuencias absolutas y frecuencias relativas son conceptos importantes en el análisis de datos que se utilizan 
# para describir cuántas veces ocurre un valor en un conjunto de datos (frecuencia absoluta) y el porcentaje 
# de esa ocurrencia en relación con el total (frecuencia relativa)

# Frecuencias absolutas
#con el .value_counts(bins=5) contaremos cuántas notas caen en cada uno de los 5 intervalos (bins) de 1 a 10
#Y con el sort_index se ordenarán los resultados por el índice
frecuencia_absoluta = df["Nota"].value_counts(bins=5).sort_index()
print("\nFrecuencia Absoluta:")
#Este print nos dirá cuántos estudiantes tienen las notas de cada intervalo
print(frecuencia_absoluta)

# Frecuencias relativas
#Se usó el .round(4) para que el resultado solo muestre 4 decimales, así un resultado de 0.2333 será lo mismo que 23.33% 
# de la muestra
#El normalize=True se usó para convertir los datos de frecuencia absoluta a frecuencia relativa, dejando ver la proporción
# de cada valor respecto del total
frecuencia_relativa = df["Nota"].value_counts(bins=5, normalize=True).sort_index().round(4)
print("\nFrecuencia Relativa:")
#Este print nos va a mostrar el % de estudiantes que pertenece a cada rango de calificaciones
print(frecuencia_relativa)



#!!!__ Ahora pasamos al punto 2 que pide representar la variable ciudad con un diagrama de barras y un diagrama de sectores

#Primero importaremos la biblioteca matplotlip.pyplot para poder crear los gráficos y le daremos el "alias" de
# plt por medio del as. Esto para que el código no quede tan cargado
import matplotlib.pyplot as plt

# Diagrama de barras
#Tomamos ciudad de la tabla df, contaremos la cantidad de estudiantes con .value_counts
#Por medio de .plot crearemos el gráfico, y con kind eligiremos el tipo de gráfico a crear, en este caso será "bar" o sea
#un gráfico de barras, para kind contamos con las siguientes opciones de gráficos:
#bar: Gráfico de barras verticales.
#barh: Gráfico de barras horizontales.
#line: Gráfico de líneas (por defecto si no se especifica el tipo de gráfico en kind).
#scatter: Diagrama de dispersión.
#hist: Histograma.
#pie: Gráfico circular o lo que viene siendo una torta

df["Ciudad"].value_counts().plot(kind="bar", color=["blue", "green", "red"])
#Con title añadiremos título al gráfico
plt.title("Distribución de Estudiantes por Ciudad")
#Con xlabel añadiremos un nombre al eje horizontal del gráfico
plt.xlabel("Ciudad")
#Con ylabel añadiremos un nombre al eje vertical del gráfico
plt.ylabel("Cantidad de Estudiantes")
#Con .show mostraremos el gráfico como tal
plt.show()

# Diagrama de sectores - gráfico de torta
#Con el autopct="%1.1f%%" se controlará cómo se muestran los % en el gráfico. El 1.1f nos ayudará a que solo se 
# muestre un decimal, el %% sirve para que los valores se muestren con un %
df["Ciudad"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["blue", "green", "red"])
plt.title("Distribución porcentual por Ciudad")
plt.ylabel(" ")
plt.show()


#!!!__ Ahora procederemos con el punto 3, para lo cual exportaremos la biblioteca seaborn, esta nos va a ayudar a realizar
#visualizaciones estadísticas puntualmente para el diagrama de caja. Le daremos el apodo de sns

import seaborn as sns

# Histograma para la variable Edad
#Aqui también manejaremos la distribución de edades en 5 intervalos, con color daremos colos a las barras y con edgecolor
#daremos color al borde de las barras
plt.hist(df["Edad"], bins=5, color="yellow", edgecolor="black")
plt.title("Histograma de Edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia - estudiantes")
plt.show()

# Diagrama de caja para la variable Edad, el cual nos ayudará a a tener una representación gráfica del resumen y distribución 
#del conjunto de datos, también permitirá ver si hay simetrís o sesgo en la información, algunos puntos a tener en cuenta serán:

#Los outliers vienen siendo los valores atípicos, los cuales se observan significativamente alejados del resto de datos y 
#se encuentran fuera de los bigotes
#La línea dentro de la caja indica la mediana de las edades
#La caja abarcará el 50% centrsl de los datos
#Los bigotes son los que se extienden desde la caja y representan el rango de datos que no se considera valores atípicos
sns.boxplot(x=df['Edad'])
plt.title('Diagrama de caja de edad (range = 1.5)')
plt.show()



#!!!__ Ahora procederemos con el punto 4, en el cual se hará un resumen de la variable nota mediante la orden summary

# Resumen de la variable Nota
#Creamos la nueva variable resumen_nota, traemos los datos de nota mediante df["nota"]
#Usamos el .describe para obtener estadísticas descriptivas de los datos

resumen_nota = df["Nota"].describe()

#Al imprimir obtendremos los siguientes datos:

#Count: 30 estudiantes tienen notas registradas.
#Mean: La nota promedio es 4.94.
#Std: La desviación estándar es 2.91, lo que indica variabilidad en las notas.
#Min: La nota más baja es 0.16.
#25%: El primer cuartil es 2.59, lo que significa que el 25% de los estudiantes tiene notas de 2.59 o menos.
#50%: La mediana es 5.55, lo que indica que la mitad de los estudiantes tiene notas por debajo de este valor.
#75%: El tercer cuartil es 7.19, lo que significa que el 75% de los estudiantes tiene notas de 7.19 o menos.
#Max: La nota más alta es 9.95.

print(resumen_nota)

# Comprobar medidas específicas
#Con .mean sacaremos la media
media_nota = df["Nota"].mean()
#Con .median sacaremos la mediana
mediana_nota = df["Nota"].median()
print(f"\nMedia: {media_nota}, Mediana: {mediana_nota}")



#!!!__ Ahora pasaremos al punto 5, en el cual se solicita calcular la estatura media de los estudiantes y proporcionar
#la dispersión 
# Calcular la estatura media
#Primero se creará la variable media_estatura, luego traeremos de df la estatura de los estudiantes y 
# con .mean sacaremos la media
media_estatura = df['Estatura'].mean()
#Luego al imprimir usaremos \n para darle un enter adicional y .2f para que el valor cuente solo con dos decimales
print(f"\nEstatura Media: {media_estatura:.2f} cm")

#Ahora procedemos con las dos medidas que permitan ver la dispersión de esa variable
# Usaremos las medidas de dispersión: varianza y desviación estándar

#Procedemos a crear ambas variables, y usando .var para la varianza y .std para la desviación estandar
#La varianza nos servirá para cuantificar cuán dispersos están los datos en relación con la media
varianza_estatura = df['Estatura'].var()
#La desviación estandar es la raíz cuadrada de la varianza. Esta medida también indica la dispersión de los datos, 
# pero se expresa en las mismas unidades que los datos originales, lo que la hace más fácil de interpretar
desviacion_estandar_estatura = df['Estatura'].std()

print(f"\nVarianza de Estatura: {varianza_estatura:.2f} cm²")
print(f"\nDesviación Estándar de Estatura: {desviacion_estandar_estatura:.2f} cm")


#CONCLUSIONES

#1. Si bien un 40% de los estudiantes se encuentran en Bogotá, la muestra se encuentra bastante balanceada entre las
# tres ciudades, por lo que se puede decir que el curso es bastante popular en las tres ciudades
#2. La mayor cantidad de estudiantes tiene entre 20 y 25 años, de 30/32 a 40 la muestra disminuye respecto de los estudiantes
# con 30/32 o menos años por lo que puede pensarse que el curso es muy llamativo para los jóvenes con respecto a los mayores
#de 30/32 años
#3. La nota promedio es 4.94. lo cuales indica un desempeño bajo respecto de la nota máxima que es 10, el grupo de estudiantes
# se encuentra polarizado pues según la mediana de 5.55 la mitad de los estudiantes cuentan con una nota superior a 5.55 
# mientras que la otra mitad cuenta con notas inferiores, por lo cual es importante proponer un plan de mejora
# para inclinar aún más estudiantes a superar esa mediana





