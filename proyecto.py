#Proyecto final Python

from datetime import datetime

print("Liga de fútbol de Querétaro")
print("Registro de puntos por partido\n")

equipos = []
"""
Lista anidada donde se guardará cada equipo junto con sus puntos.
"""

def agregar_puntos(nombre_equipo, resultado):
    """
    Función que recibe el nombre del equipo (str) y el resultado (int).
    Resultado es: 1 = ganó (3 puntos), 2 = empató (1 punto), 3 = perdió (0 puntos)
    Busca el equipo en la lista 'equipos' y le suma los puntos correspondientes.
    Regresa True si encontró el equipo y pudo sumar puntos, sino False.
    """
    for equipo in equipos:
        if equipo[0].lower() == nombre_equipo.lower():
            if resultado == 1:
                equipo[1] += 3
            elif resultado == 2:
                equipo[1] += 1
            return True  
    return False  


def registrar_equipos():
    """
    Función que pregunta cuántos equipos habrá en la liga
    y luego pide el nombre de cada uno para guardarlos.
    """
    cantidad = int(input("¿Cuántos equipos participarán?: "))
    for i in range(cantidad):
        nombre = input(f"Nombre del equipo {i + 1}: ")
        """
        # Su guarda el equipo como [nombre, puntos_iniciales]
        """
        equipos.append([nombre, 0])

registrar_equipos() 

def registrar_partidos():
    """
    Función que permite ingresar los resultados de partidos uno por uno.
    Pregunta el nombre del equipo y el resultado (1, 2 o 3).
    Se utiliza un ciclo en el que si es True se prosigue y si es False, te marca el error,
    si el usuario escribe 'FIN', se termina el registro.
    Esta función no regresa nada, pero SÍ modifica la lista 'equipos'.
    """
    print("\nRegistro de partidos")
    print('Escribe "FIN" cuando ya no quieras registrar más partidos.\n')

    while True:
        nombre = input("¿Qué equipo jugó? (o escribe FIN para terminar): ")

        if nombre.upper() == "FIN":
            break

        resultado = int(input("Resultado (1=ganó, 2=empató, 3=perdió): "))

        valido = agregar_puntos(nombre, resultado)

        if valido:
            print(f"Puntos agregados a {nombre}.\n")
        else:
            print("Equipo no encontrado, verifica el nombre.\n")

registrar_partidos()    


def mostrar_ranking():
    """
    Función que ordena la lista de equipos por puntos de mayor a menor
    y luego muestra el ranking final. También utiliza la función import,
    para llamar a la fecha del día y hora en el que se hizo el registro.
    No devuelve nada, solo imprime resultados.
    """
    
    equipos.sort(key=lambda x: x[1], reverse=True)

    print("\nTabla de posiciones")
    fecha_actual = datetime.now()
    print("Registro realizado el:", fecha_actual.strftime("%d/%m/%Y %H:%M:%S"))
    for posicion, equipo in enumerate(equipos, start=1):
        print(f"{posicion}) {equipo[0]} = {equipo[1]} puntos")
    


    print("\nEso sería todo")

mostrar_ranking()       


    

