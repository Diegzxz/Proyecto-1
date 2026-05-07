"""
Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.


NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    # Se construye el diccionario con todas las llaves y los valores recibidos por parámetro, los cuales van a ser la informacion de la pelicula 
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }

    # Se retorna el diccionario para que quien llamó la función pueda usarlo.
    # Sin este return, la función retornaría None y no habría manera de guardar la película.
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    # Se convertira el nombre buscado a minúsculas para que la búsqueda no sea sensible y no se confunda por una simple letra mayuscula en el codigo 
    nombre_buscado = nombre_pelicula.lower()

    # Se compara el nombre buscado con el nombre de cada película (también en minúsculas)
    # Si son inguales entonces se retorna ese diccionario inmediatamente
    # Si se quitara alguno de estos bloques, esa película nunca podría ser encontrada 
    if p1["nombre"].lower() == nombre_buscado:
        return p1
    elif p2["nombre"].lower() == nombre_buscado:
        return p2
    elif p3["nombre"].lower() == nombre_buscado:
        return p3
    elif p4["nombre"].lower() == nombre_buscado:
        return p4
    elif p5["nombre"].lower() == nombre_buscado:
        return p5
    else:
        # Si lo que se introduce no coincide con ninguna pelicula entonces se retorna none
        return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    # al momento de buscar la pelicula mas larga se utiliza el metodo de rey de la montaña
    # basicamente se asume que p1 e ¡s la pelicula mas larga y esta se actualizara cuando encuentre a una mas larga
    mas_larga = p1

    # Se compara cada película contra el rey de la montaña actual.
    # Si alguna tiene mayor duración, pasa a ser el nueva rey de la montaña
    if p2["duracion"] > mas_larga["duracion"]:
        mas_larga = p2

    if p3["duracion"] > mas_larga["duracion"]:
        mas_larga = p3

    if p4["duracion"] > mas_larga["duracion"]:
        mas_larga = p4

    if p5["duracion"] > mas_larga["duracion"]:
        mas_larga = p5

    # Se retorna el diccionario de la película más larga encontrada.
    # Sin este return, la consola recibiría None y fallaría al mostrar la información.
    return mas_larga

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    # Paara calcular la duracion promedio de las peliculas se sumaran los minutos de las 5 y luego se dividiran por la cantidad de peliculas
    total_minutos = p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]

    # Se divide entre 5 usando división entera // para ignorar los decimales, ya que con decimales el formato fallara
    promedio_total = total_minutos // 5

    # Se extraen las horas completas dividiendo entre 60.
    # Sin esta línea no se podría construir el formato HH:MM.
    horas = promedio_total // 60

    # El residuo de dividir entre 60 son los minutos restantes.
    # Sin esta línea los minutos siempre serían 0 y el resultado sería incorrecto.
    minutos = promedio_total % 60

    # Se construye y retorna la cadena en formato "HH:MM".
    # :02d garantiza que siempre haya 2 dígitos (ej: "01:05" en lugar de "1:5").
    # Sin el return, la consola recibiría None y fallaría al concatenar el texto.
    return f"{horas:02d}:{minutos:02d}"

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    # Se inicia un string vacío donde se irán acumulando los nombres de los estrenos.
    estrenos = ""

    # Se verifica cada película: si su año es estrictamente mayor al año dado, se agrega al resultado.
    # Se usa > (mayor estricto) porque el enunciado pide películas POSTERIORES al año dado.
    if p1["anio"] > anio:
        estrenos = p1["nombre"]

    if p2["anio"] > anio:
        # Si ya hay nombres en estrenos, se agrega una coma antes del nuevo nombre.
        # Sin esta condición, se agregaría una coma al inicio cuando estrenos está vacío.
        if estrenos == "":
            estrenos = p2["nombre"]
        else:
            estrenos = estrenos + ", " + p2["nombre"]

    if p3["anio"] > anio:
        if estrenos == "":
            estrenos = p3["nombre"]
        else:
            estrenos = estrenos + ", " + p3["nombre"]

    if p4["anio"] > anio:
        if estrenos == "":
            estrenos = p4["nombre"]
        else:
            estrenos = estrenos + ", " + p4["nombre"]

    if p5["anio"] > anio:
        if estrenos == "":
            estrenos = p5["nombre"]
        else:
            estrenos = estrenos + ", " + p5["nombre"]

    # Si después de revisar las 5 películas el string sigue vacío, ninguna cumplió la condición.
    if estrenos == "":
        estrenos = "Ninguna"

    # Se retorna el string con los nombres encontrados o en tal caso "Ninguna"
    return estrenos

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    # Se inicia el contador en 0. Sin esto, la variable no existiría y el programa fallaría.
    cantidad = 0

    # Por cada película con clasificación "18+" se suma 1 al contador.
    if p1["clasificacion"] == "18+":
        cantidad = cantidad + 1

    if p2["clasificacion"] == "18+":
        cantidad = cantidad + 1

    if p3["clasificacion"] == "18+":
        cantidad = cantidad + 1

    if p4["clasificacion"] == "18+":
        cantidad = cantidad + 1

    if p5["clasificacion"] == "18+":
        cantidad = cantidad + 1

    # Se retorna el total contado
    return cantidad

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    # Solo se aplican las restricciones de horario si el usuario activó el control horario.
    # Sin este if, las reglas se aplicarían siempre aunque el usuario no las quisiera.
    if control_horario:

        # Regla 1: No se deben programar documentales a las 22:00 (2200) o más tarde.
        # "in" verifica si la palabra "Documental" aparece dentro del string de géneros.
        # Sin esta regla, se podrían programar documentales en cualquier horario nocturno.
        if "Documental" in peli["genero"] and nueva_hora >= 2200:
            return False

        # Regla 2: No se deben programar dramas los viernes.
        if "Drama" in peli["genero"] and nuevo_dia == "Viernes":
            return False

        # Regla 3: Entre semana no se programan películas a las 23:00 (2300) o más tarde,
        # ni antes de las 6:00 (600) Se lista cada día entre semana explícitamente
        # Sin esta lista, la regla no sabría cuáles días son entre semana
        dias_entre_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        if nuevo_dia in dias_entre_semana:
            if nueva_hora >= 2300 or nueva_hora < 600:
                return False

    # Se calcula la hora de inicio y fin de la nueva programación en minutos totales.
    # La fórmula (hora // 100) * 60 + (hora % 100) convierte formato HHMM a minutos
    # Por ejemplo, 1430 → (14 * 60) + 30 = 870 minutos
    # Sin esta conversión, no se podría detectar solapamiento real entre película
    nueva_inicio_min = (nueva_hora // 100) * 60 + (nueva_hora % 100)
    nueva_fin_min = nueva_inicio_min + peli["duracion"]

    # Se revisa cada película para detectar conflictos de horario.
    #  Al usar "is not peli" evita comparar la película consigo misma (no es conflicto con ella misma)
    # Se verifica si comparten día Y si sus rangos de tiempo se ccruzan
    # Hay cruzamiento si: inicio_nueva < fin_otra  Y  inicio_otra < fin_nueva
    hay_conflicto = False

    if p1 is not peli and p1["dia"] == nuevo_dia:
        p1_inicio_min = (p1["hora"] // 100) * 60 + (p1["hora"] % 100)
        p1_fin_min = p1_inicio_min + p1["duracion"]
        if nueva_inicio_min < p1_fin_min and p1_inicio_min < nueva_fin_min:
            hay_conflicto = True

    if p2 is not peli and p2["dia"] == nuevo_dia:
        p2_inicio_min = (p2["hora"] // 100) * 60 + (p2["hora"] % 100)
        p2_fin_min = p2_inicio_min + p2["duracion"]
        if nueva_inicio_min < p2_fin_min and p2_inicio_min < nueva_fin_min:
            hay_conflicto = True

    if p3 is not peli and p3["dia"] == nuevo_dia:
        p3_inicio_min = (p3["hora"] // 100) * 60 + (p3["hora"] % 100)
        p3_fin_min = p3_inicio_min + p3["duracion"]
        if nueva_inicio_min < p3_fin_min and p3_inicio_min < nueva_fin_min:
            hay_conflicto = True

    if p4 is not peli and p4["dia"] == nuevo_dia:
        p4_inicio_min = (p4["hora"] // 100) * 60 + (p4["hora"] % 100)
        p4_fin_min = p4_inicio_min + p4["duracion"]
        if nueva_inicio_min < p4_fin_min and p4_inicio_min < nueva_fin_min:
            hay_conflicto = True

    if p5 is not peli and p5["dia"] == nuevo_dia:
        p5_inicio_min = (p5["hora"] // 100) * 60 + (p5["hora"] % 100)
        p5_fin_min = p5_inicio_min + p5["duracion"]
        if nueva_inicio_min < p5_fin_min and p5_inicio_min < nueva_fin_min:
            hay_conflicto = True

    # Si hay conflicto con alguna película, no se puede reagendar y se retorna False.
    if hay_conflicto:
        return False

    # Si pasó todas las verificaciones, se actualiza la hora y el día de la película.
    # Sin estas dos líneas, la función retornaría True pero la película NO quedaría reagendada.
    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia

    # Se retorna True indicando que el reagendamiento fue exitoso.
    return True
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    # Se extraen el género y la clasificación de la película para usarlos en las reglas.
    # Sin estas variables, habría que escribir peli["genero"] y peli["clasificacion"] lo cual seria mas demorado y menos organizado
    genero = peli["genero"]
    clasificacion = peli["clasificacion"]

    # Regla 1: Los mayores de 18 pueden ser invitados a cualquier película sin restricción.
    # Este return True detiene la función de inmediato, sin revisar las demás reglas.
    if edad_invitado >= 18:
        return True

    # Regla 2: Los menores de 15 años no pueden ver películas de Terror bajo ninguna condición.
    # "in" verifica si "Terror" aparece en el string de géneros.
    # Sin esta regla, un niño de 10 años podría ver una película de terror con autorización.
    if edad_invitado < 15 and "Terror" in genero:
        return False

    # Regla 3: Los de 10 años o menos solo pueden ver películas de género Familiar.
    # "not in" verifica que "Familiar" NO aparezca en los géneros.
    if edad_invitado <= 10 and "Familiar" not in genero:
        return False

    # Regla 4: Si la edad no cumple la clasificación, se necesita autorización de los padres,
    # EXCEPTO si la película es un documental ya que los documentales no requieren autorización
    # Se verifica cada clasificación por separado para cubrir todos los casos posibles
    if clasificacion == "7+" and edad_invitado < 7:
        if "Documental" in genero:
            return True
        return autorizacion_padres

    if clasificacion == "13+" and edad_invitado < 13:
        if "Documental" in genero:
            return True
        return autorizacion_padres

    if clasificacion == "16+" and edad_invitado < 16:
        if "Documental" in genero:
            return True
        return autorizacion_padres

    if clasificacion == "18+" and edad_invitado < 18:
        if "Documental" in genero:
            return True
        return autorizacion_padres

    # Si llegó hasta aquí sin ser bloqueado por ninguna regla, puede ser invitado.
    # Sin este return True final, la función retornaría None en casos válidos.
    return True
