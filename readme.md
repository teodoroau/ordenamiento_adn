# Programa para order cadenas de ADN
---
El programa imprime las cadenas ordenadas de mayor a menor, y también puede generar un archivo de salida en el mismo formato, con
las cadenas ordenadas en cada caso de prueba.

## Ejecución
---
Para ejecutarlo, hay que poner el archivo 'tarea_semestral.py', en la misma carpeta donde se encuentre
el documento de texto en el que se extraeran las cadenas de ADN junto con los otros datos para el ordenamiento.

### Opciones de ejecucion
- En windows teniendo python instalado y por defecto para ejecutar archivos .py, podemos iniciar el programa haciendo doble click.

- Para todos los sistemas operativos se puede ejecutar el programa desde la consola llamando al interprete:
> python3 tarea_semestral.py

## Formato del archivo de entrada
---
Puede ser cualquier archivo de texto plano, estructurado de la siguiente forma:
1. La **primera linea** indica la cantidad de **casos de prueba**(grupos de cadenas de adn, con sus dos previas lineas indicando las caracteristicas).
2. La **segunda linea** indicará el **tamaño minimo y el máximo** de las **cadenas**(dos numeros separados por un espacio (mayores que 50 y menores que 50)).
3. La **tercera linea** son la **cantidad** de **cadenas** de ADN que se van **a procesar**(un numero mayor que 0 y menor que 50).
4. Finalmente las **cadenas de ADN**, **una por linea**().

## Reglas para el ordenamiento
---
Se entregarán las cadenas desde la más ordenada a la menos desordenada, según las siguientes reglas

1. La que tenga menor **grado de desorden** () es la más ordenada. 
2. Más ordenada es la más larga en caso de pares de cadenas con el mismo grado de desorden.
3. Si tienen mismo grado de desorden y mismo largo, más ordenada es la más alfabetica.