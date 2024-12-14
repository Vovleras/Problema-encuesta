# **PROCESAMIENTO DE ENCUESTA**

Una consultoría de datos desea realizar un análisis de los resultados de una gran encuesta, 
con la finalidad de identificar cuáles temas, con base en ciertas preguntas, 
tienen opiniones más favorables y poder también responder otras preguntas afines.

Las encuestas están divididas en diversos temas, cada tema
tiene diferentes preguntas, donde cada pregunta consulta sobre hasta qué punto se está de
acuerdo sobre una propuesta; a su vez, cada pregunta fue realizada a ciertas personas
(encuestados), cada persona solo puede participar respondiendo sólo
una pregunta.

La encuesta está organizada en K temas, cada uno de los temas tiene un
nombre, además, cada tema consiste de M preguntas, donde cada pregunta
puede contar con una cantidad mínima Nmin y máxima Nmax de encuestados,
cada encuestado tendrá un número como identificador, su nombre, su nivel de
experticia sobre la pregunta, cuyo valor es entero entre 0 y 10, y su opinión
(respuesta a la pregunta), este último tomará valores enteros de 0 a 10, donde 0
indica que se tiene una opinión completamente desfavorable y 10 una opinión
completamente favorable.

La consultoría obtiene los siguientes datos además de:

- Pregunta con mayor promedio de opiniones
- Pregunta con menor promedio de opiniones
- Pregunta con mayor promedio de experticia
- Pregunta con menor promedio de experticia
- Encuestado con el mayor nivel de experticia
- Encuestado con el menor nivel de experticia
- Encuestado con el menor valor de opinión
- Encuestado con el mayor valor de opinión
- Promedio de experticia de los encuestados
- Promedio del valor de opinión de los encuestados

# **ESTRUCTURA IMPLEMENTACIÓN**

Para llevar a cabo el ordenamiento y procesamiento de datos se implementaron dos soluciones:

- **Primera solución**: Se ordenan los datos mediante el algoritmo de ordenamiento Insertion sort. Dicho algoritmo funciona con estructura de datos listas.
- **Segunda solución**: Se ordenan los datos mediante el algoritmo de ordenamiento Quick sort. Dicho algoritmo funciona con estructura de datos pilas extendida.

La estructura pilas es extendida ya que se implementó un método adicional `peek()` que retorna el elemento asociado a top.

El código se estructura en tres carpetas y un archivo `main`:

- **La carpeta entradas_pruebas** contiene todas las encuestas de prueba.

- **La carpeta solucion_listas** contiene:
  - **Archivo clases_listas**:
    - Se encuentra la implementación de las clases encuestados, temas y preguntas.
  - **Archivo datos_listas**:
    - Se encuentra toda la lógica que procesa los datos y obtiene los resultados utilizando la estructura listas.
  - **Archivo lista**:
    - Se encuentra la implementación de la clase lista que es la estructura de datos utilizada por Insert.

- **La carpeta solucion_pilas** contiene:
  - **Archivo algoritmos**:
    - Se encuentra la implementación de la clase pila extendida que es la estructura de datos utilizada por Quicksort.
  - **Archivo clases**:
    - Se encuentra la implementación de las clases encuestados, temas y preguntas.
  - **Archivo leerArchivoPilas**:
    - Se encuentra toda la lógica que procesa los datos y obtiene los resultados utilizando la estructura pilas.

- **El archivo main** tiene la GUI de la aplicación.

# **GUIA DE USUARIO**
- La GUI implementada permite cargar un archivo desde el ordenador. Luego, se debe seleccionar con qué estructura de datos
  se quiere realizar la consultoría. Una vez obtenga el mensaje de validación que el resultado fue exitoso, haciendo click sobre el botón
  "descargar", se descarga el archivo de resultados en el ordenador del usuario con el nombre que él decida colocarle.




    
    
      


