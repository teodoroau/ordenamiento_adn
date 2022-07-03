import os

# 1
def validar_archivo_de_entrada(nombre_archivo):
    """ Valida que el archivo 'ADN.dat' se encuentre según lo establecido:
        - Primera linea: un numero mayor que 0 y menor que 50. (), que indicara la cantidad
        de casos de prueba.

        - Segunda linea: dos numeros enteros entre 5 y 50. (), el primer numero ingresado
        debe ser menor o igual al segundo y definira la longitud minima de la cadena, mientras
        que el 2do definira la longitud maxima que puede tener la cadena.
        En caso de no ser asi, terminará el programa.

        - Tercera línea: la cantidad de cadenas de ADN que se deben procesar, debe ser mayor que 0 y menor que 50

        -Luego habran tantas L donde cada una contendra una cadena de ADN

        Si no cumple, lo indica y acaba el programa.

        La funcion devuelve True o False
    """
    if nombre_archivo not in os.listdir():
        print(f"{nombre_archivo} no esta en la carpeta actual")
        return False

    print(f"Validando {nombre_archivo}")

    with open(nombre_archivo, "r") as archivo:
        L = []
        for linea in archivo:
            L.append(linea.strip())

        primera = L[0]
        if len(primera.split()) != 1:  # la primera linea debe tener solo una "palabra"
            print("La primera linea solo debe contener un numero")
            return False

        if not primera.isnumeric():
            print("Debe ser un numero")
            return False
        primera = int(primera)

        if (primera < 1) or (primera > 49):
            print("Primera linea debe ser un numero mayor que 0 y menor que 50")
            return False

        segunda = L[1]
        if len(segunda.split()) != 2:
            print(f"La segunda linea del archivo {nombre_archivo} no tiene 2 numeros")
            return False
        else:
            segunda = segunda.split()
            segundaA, segundaB = segunda
            if not all([segundaA.isnumeric(), segundaB.isnumeric()]):
                print(
                    f"La segunda linea del archivo {nombre_archivo} no tiene 2 numeros")
                return False
            else:
                segundaA = int(segundaA)
                segundaB = int(segundaB)

        if segundaA < 6 or segundaA > segundaB:
            print("El primer valor de la segunda linea debe ser mayor q 5 y a lo sumo igual al segundo")
            return False
        if segundaB >= 50:
            print("En la tercera linea los dos numeros deben ser menor a 50")
            return False

        tercera = L[2]  # Se pasa la tercera linea de el archivo a una variable para evaluar que siga el formato
        try:
            tercera = int(tercera)  # se intenta convertir la tecera linea a numero entero
        except:  # si falla:
            print("La tercera linea debe contener 1 número")
            return False  # funcion validar retorna False

        if tercera <= 0 or tercera >= 50:
            print("error, debe ser un valor mayor o a 0 y menor que 50 ")
            return False

        cadenas_adn = L[3:]

        if len(cadenas_adn) != tercera:  # valida cantidad indicada de cadenas en el archivo
            print(f"\nLa cantidad de cadenas de adn debe ser la indicada en la tercera linea de '{nombre_archivo}'")
            return False

        for i in cadenas_adn:
            for letra in i:  # Revisar que las cadenas solo tengan bases nitrogenadas de ADN
                if letra not in ("A", "C", "G", "T"):
                    print("Una de las cadenas de ADN se encuentrá mal:\n ", end="")
                    print(i)
                    return False

            if len(i) < segundaA:  # cadena de menor tamaño dentro del rango
                print("Una de las cadenas es mas corta de lo que deberia")
                return False
            if len(i) > segundaB:  # cadena de mayor tamaño dentro del rango
                print("Una de las cadenas es mas larga de lo indicado")
                return False

        print(f"'{nombre_archivo}' validado correctamente.\n")
        return True


# 2
def obtener_cadenas(nombre_archivo):
    """ Recibe el nombre del archivo del que obtener las cadenas a ordenar
    Devuelve una lista con las cadenas en el mismo orden que en el archivo
    """
    archivo = open(f"{nombre_archivo}")
    L = list()
    for i in archivo:
        L.append(i.strip("\n"))
    cadenas = L[3:]
    return cadenas


def desorden_cadena(cadena):
    nueva_cadena = ""
    for i in cadena:  # generando cadena de numeros
        if i == "A":
            nueva_cadena = nueva_cadena + "1"
        if i == "C":
            nueva_cadena = nueva_cadena + "2"
        if i == "G":
            nueva_cadena = nueva_cadena + "3"
        if i == "T":
            nueva_cadena = nueva_cadena + "4"

    # viendo desorden
    contador = 0
    for indice in range(len(nueva_cadena)):
        evaluar = int(nueva_cadena[indice])
        for i in nueva_cadena[indice + 1:]:
            if evaluar > int(i):
                contador += 1
    return contador


# 3
def ordenar_cadenas(cadenas_adn):
    """ Recibe una lista de cadenas desordenadas y
    devuelve una lista con las cadenas ordenadas decrecientemente
    segun las siguintes reglas:

    1. Le otorgaremos un valor a cada letra segun su orden alfabetico, posteriormente analizaremos letra por letra
    y por cada letra que se ubique posteriormente a la cadena y posea un valor menor a la letra analizada se sumara
    "1" a la medida de desorden para asi despues de analizar cada letra de una cadena, obtendremos su medida de desorden.

    2. La más ordenada será la cadena con una menor medida de desorden lo que significa que necesita
    menos inversiones para dejar aquella secuencia en orden.
        
    3. En caso de que dos o mas cadenas poseen la misma medida de desorden estas deben ordenarse 
    desde la que posee mayor longitud hasta la que tiene menor longitud.

    4. Si hay empate con los dos anteriores, irá antes aquel más alfabético
        
    """
    def ordenar_por_grado_desorden(cadenas_adn):
        lista = []
        cont = 0
        while cont < 500:
            cont = cont + 1
            lista.append(" ")

        for l in cadenas_adn:
            lista.insert(desorden_cadena(l), l)

        while ' ' in lista:
            lista.remove(' ')

        return lista


    def ordenar_por_len_decendente(lista_de_strings):
        """ Del más largo al más corto
        """
        mayor_a_menor = list()
        for string in reversed(sorted(lista_de_strings, key=len)):
            mayor_a_menor.append(string)

        return mayor_a_menor

    def orden_alfabetico(lista):
        lista_alfabetica = sorted(lista)

        return lista_alfabetica
        
    ordenado_por_grado_desorden = ordenar_por_grado_desorden(cadenas_adn)
    resultado_ordenado = ordenado_por_grado_desorden[:]
    
    # orden
    n = len(resultado_ordenado) #veces que se ordena
    while n > 0:
        n -= 1
        for i in range(len(ordenado_por_grado_desorden) - 2):
            
            if desorden_cadena(resultado_ordenado[i]) == desorden_cadena(resultado_ordenado[i + 1]):
                
                if len(resultado_ordenado[i]) != len(resultado_ordenado[i + 1]):
                    resultado_ordenado[i], resultado_ordenado[i + 1] = orden_alfabetico(
                        resultado_ordenado[i], resultado_ordenado[i + 1])
                
                else:
                    resultado_ordenado[i], resultado_ordenado[i + 1] = ordenar_por_len_decendente(resultado_ordenado[i + 1], resultado_ordenado[i])

        
    return resultado_ordenado


# 4
def generar_archivo_ordenado(cadena_ordenada, nombre_archivo):
    """ Recibe la una lista de cadenas ordenadas y crea un archivo
        de nombre f"{nombre_archivo}.dat" 
    """
    if nombre_archivo in os.listdir():
        entrada = input(
            "Ya existe el archivo {} en la carpeta, ¿desea sobreescribirlo?. (s / n)\n".format(nombre_archivo))
        if entrada != "s":
            print("Programa finalizado")
            exit()

    with open(nombre_archivo, "w") as archivo_salida:
        archivo_salida.writelines("\n".join(cadena_ordenada))

    print(f"Se ha creado el archivo {nombre_archivo}")


# Acá abajo inicia el programa
print("Ordenamiento de cadenas de ADN.\n")

while not validar_archivo_de_entrada(archivo := input("Indique el nombre del archivo que desea analizar y se creará un archivo con las cadenas ordenadas: \n")):
    reintentar = input("Validación fallida, ¿ desea intentar nuevamente ? (s/n): ")
    if reintentar == "s":
        archivo = input("Indique el nombre del archivo que desea analizar y se creará un archivo nuevo con las cadenas "
                        "ordenadas: \n")
        continue
    else:
        print("\nPrograma finalizado.\n")
        exit()

cadenas = obtener_cadenas("ADN.dat")

cadenas_ordenadas = ordenar_cadenas(cadenas)

generar_archivo_ordenado(cadenas_ordenadas, "SALIDA_{}".format(archivo))

print('Cadenas ordenadas:\n')
for i in cadenas_ordenadas:
    print(i)
