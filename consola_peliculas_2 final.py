"""
Agenda de peliculas - Modulo de interaccion por consola.
"""
import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict)-> None:
    #Saca los datos del diccionario y los imprime de forma organizada en la consola
    #Aplica lógica para que las horas y minutos siempre muestren dos dígitos (ejemplo 09:05)
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    # Formatea la hora dividiendo por 100 para obtener horas y usando residuo para minutos.
    if (hora//100 < 10): hora_formato = "0"+ str(hora//100)
    else: hora_formato = str(hora//100)
    
    if (hora%100 < 10): min_formato = "0"+ str(hora%100)
    else: min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    #Llama a la función lógica para hallar la película de mayor duración entre las cinco
    #Muestra el resultado final usando la función de impresión de detalles
    print("Pelicula mas larga de la agenda\n" + "-"*50)
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    mostrar_informacion_pelicula(pelicula_mas_larga)

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    # Invoca el cálculo del promedio de tiempo de las películas y lo imprime en pantalla.
    # El resultado se muestra en el formato 'HH:MM' devuelto por el módulo de lógica para que se vea bien el resultado
    print("Duracion promedio de las peliculas de la agenda\n" + "-"*50)
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("Duracion promedio: " + promedio)

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    print("Buscar peliculas estrenadas despues de un anio dado\n" + "-"*50)
    anio = int(input("Ingrese el anio limite: "))
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    print("Peliculas estrenadas despues de " + str(anio) + ": " + estrenos)

     # Solicita un año al usuario y muestra los nombres de las películas estrenadas después de este
    # Convierte la entrada de texto a número entero antes de enviarla al módulo de búsqueda

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    # Consulta al módulo cuántas películas tienen restricción '18+' y muestra el total
    print("Cantidad de peliculas con clasificacion 18+")
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print("Hay " + str(cantidad) + " pelicula(s) con clasificacion 18+")
    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    # Gestiona el cambio de horario de una película pidiendo nombre, nueva hora y día.
    print("Reagendar una pelicula de la agenda\n" + "-"*50)
    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)
    # Si el módulo detecta un cruce o viola una regla horaria, informa que no fue posible el cambio
    
    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        nueva_hora = int(input("Ingrese la nueva hora (formato 24h, ej 1430): "))
        nuevo_dia = input("Ingrese el nuevo dia: ")
        control = input("Desea activar el control horario? (si/no): ").strip().lower() == "si"

        if mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control, p1, p2, p3, p4, p5):
            print("Reagendada exitosamente."); mostrar_informacion_pelicula(pelicula)
        else:
            print("No fue posible por conflicto de horario o restricciones.")

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    # Pregunta por una película, edad y permiso para verificar si un invitado puede verla.
    # Utiliza las reglas de género y clasificación del módulo para dar una respuesta (si o no)
    print("Decidir si se puede invitar a alguien")
    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula:
        edad = int(input("Ingrese la edad del invitado: "))
        autorizacion = input("¿Tiene autorizacion? (si/no): ").strip().lower() == "si"
        if mod.decidir_invitar(pelicula, edad, autorizacion):
            print("Si se puede invitar.")
        else:
            print("No se puede invitar.")
  
def iniciar_aplicacion():
    """Crea las películas iniciales y mantiene el programa activo en un ciclo infinito.
    Muestra el estado actual de la agenda antes de cada elección del menú."""
    pelicula1 = mod.crear_pelicula("Toy Story", "Familiar, Comedia", 81, 1995, 'Todos', 1600, "Lunes")
    pelicula2 = mod.crear_pelicula("March of the Penguins", "Documental", 80, 2005, '7+', 1000, "Martes")
    pelicula3 = mod.crear_pelicula("The Amazing Spider-Man 2", "Acción, Aventura", 142, 2014, '13+', 1800, "Miércoles")
    pelicula4 = mod.crear_pelicula("Titanic", "Romance, Drama", 194, 1997, '16+', 1900, "Sábado")
    pelicula5 = mod.crear_pelicula("Get Out", "Terror, Suspenso", 104, 2017, '18+', 2100, "Domingo")
    
    ejecutando = True
    while ejecutando:            
        print("Mi agenda de peliculas")
        # Se listan todas las películas actuales antes de pedir una acción.
        mostrar_informacion_pelicula(pelicula1)
        mostrar_informacion_pelicula(pelicula2)
        mostrar_informacion_pelicula(pelicula3)
        mostrar_informacion_pelicula(pelicula4)
        mostrar_informacion_pelicula(pelicula5)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)
        if ejecutando: input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1, p2, p3, p4, p5) -> bool:
    # Muestra las opciones disponibles y dirige el flujo del programa según la elección.
    # Retorna False para cerrar el ciclo principal cuando el usuario elige la opción 7
    print("Menu: 1.Larga 2.Promedio 3.Estrenos 4.18+ 5.Reagendar 6.Invitar 7.Salir")
    opcion = input("Ingrese opcion: ").strip()
    
    if opcion == "1": ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion == "2": ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion == "3": ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion == "4": ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion == "5": ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion == "6": ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion == "7": return False
    else: print("Opcion no valida.")
    
    return True

#  por ultimo se llama a la función inicial para arrancar el sistema
iniciar_aplicacion()