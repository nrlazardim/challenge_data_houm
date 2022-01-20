# Challenge Data

# Instrucciones del desafío
Un archivo .csv contiene propiedades que fueron publicados en tres portales inmobiliarias. Un porcentaje de las 
propiedades son duplicadas entre portales y también hay propiedades que se repiten en un mismo portal.

El desafío es crear un script en Python3 que lea el archivo y genera un .csv con las propiedades de-duplicadas y al 
cual se agrega indicadores sobre cuantas veces una propiedad fue encontrado en cuál portal.

# Aspectos que se evalúan son:
1. Facilidad de lectura y entendimiento de la transformación por otros desarrolladores.
2. Buenas prácticas de desarrollo como tests y manejo de errores.
3. Eficiencia computacional de la solución.

# Data
1. El archivo original esta disponible en: https://drive.google.com/file/d/1A54vbayZuFbbozE83iGcEgXShXfUYg1I/view (22MB)

Explaya sobre cuáles métodos de de-duplicación adicionales aplicarías cuando tienes acceso a los sets de datos completos.

# Formalidades
1. Debes utilizar Python3 para desarrollar. Debes detallar las versiones de librerías y Python que utilizaste para 
resolver tu desafío. Se recomienda entregar, además de la solución, un archivo requirements.txt.
2. Envíanos tus respuestas también al correo proporcionado.


# IMPORTANTE

1. Carpeta Input. Posee ya el archivo a usar descargado y se encuentra el archivo que maneja los datos.
2. Carpeta Log. Se encuentra archivo -- log.log -- que indican los mensajes de registro.
3. Carpeta utils. Maneja todo lo relacionado al archivo de configuracion -- config_file.ini --
4. Correr archivo -- main.py -- para efectos de los resultados.
5. Correr archivo -- testing_output.py -- si se desean testear los resultados de la carpeta Output
6. Cada metodo tiene la descripcion de lo que hace y que parametros usa (si necesitase)
7. Pueden instalar archivo de requerimientos de la siguiente manera: pip install requirements.txt | IOS pip3 install requirements.txt
8. Version de python usada. Python 3.9.9 (v3.9.9:ccb0e6a345, Nov 15 2021, 13:29:20) 

# Archivo de Configuracion -- config-file.ini --
Para el manejo del TimeZone, en el caso argentina -- America/Buenos_Aires --, para el caso chileno --America/Santiago --
# 1. [INPUT]
Folder = ./Input
TimeZone = America/Buenos_Aires o -> America/Santiago
OriginFile = query_result_2021-11-25T16_27_02.44381Z.csv
# 2. [OUTPUT]
Folder = ./Output
# 3. [LOGGING]
Folder = ./Log/

# Directorios de las carpetas Input, log, Ouput
Es importante que la carpeta Input este creada junto con el archivo query_result_2021-11-25T16_27_02.44381Z.csv. 
Los demas directorios (Log, Output) se crean automaticamente.

# DATOS
Se consideran que los datos proporcionados son una muestra y esta sujeto explicitamente a los que se ha requerido
en el challenge. Considero que para poder identificar una propiedad correctamente deberia de existir mas informacion 
que la latitude y la longitude. Es por esto, que la solucion al challenge esta delimitada a lo que se ha propuesto y
requerido. 

Con el acceso a los set de datos completos y dependiendo que datos tengamos, podemos usar varias tecnicas de 
duplicado de datos, por ejemplo: 

1. Metodo de clasificacion, que consiste en la estimacion de un mapeo del espacio de caracteristicas a un espacio de clases finito.
2. Metodo de replicacion de datos homogeneos con restricciones explicitas en los umbrales.
3. Segmentacion de texto.
4. Algoritmos de hashing casi óptimos para el vecino mas cercano aproximado en dimensiones altas (requiere dataset enorme)
5. Clusterizacion de correlacion (tambien podemos incorporar clusterizacion por covariaciones, dependiendo que tengamos).
6. Deteccion de duplicados adaptables usando una medida de similitud de texto que sean aprendible.
7. ETC.

Dependiendo de la estructura, el prblema que se quiera solucionar y el foco del negocio existen muchas maneras pa el
tratado de los de-duplicados.
