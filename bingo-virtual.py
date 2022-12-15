#hay que instalar la libreria para que imprima el color : pip install termcolor
from termcolor import colored

import random
import os
import copy

# Pre-condicion: ingresa un carton, su minimo, maximo y la fila donde se
# ingresara el numero nuevo
# Post- condicion: no retorna nada, solo actualiza el carton
def generar_unico_carton(carton: list, x: int, y: int, fila: int) -> None:
    
    aux: bool = True
    while aux:
        num: int = random.randint(x, y)
        if num not in carton[0] and num not in carton[1] and num not in carton[2]:
            carton[fila].append(num)
            aux = False

# Pre-condicion: ingresa carto y el numero de elementos por fila a eliminar
# Post- condicion: actualiza el carton   
def elimina_cuatro_elementos_filas(carton: list) -> None:

    for fila in carton:
        for i in range(4):
            aux = True
            # si el numero ya es 0, no cambiarlo y buscar otro
            while aux:
                indice = random.randint(0, 8)

                if fila[indice] != '  ':
                    fila[indice] = '  '
                    aux = False

# Pre-condicion: entra los tamaños de las filas o columnas a para crear los cartones del bingo
# Post- condicion: retorna una lista cargada de cartones determinada en el rango que quiera
def crea_cartones(fila: int, columna: int) -> list:

    carton: list = [[], [], []]
    for i in range(0, fila):
        for j in range(0, columna):

            if j == 0:
                generar_unico_carton(carton, 1, 11, i)

            elif j == 1:
                generar_unico_carton(carton, 12, 22, i)

            elif j == 2:
                generar_unico_carton(carton, 23, 33, i)

            elif j == 3:
                generar_unico_carton(carton, 34, 44, i)

            elif j == 4:
                generar_unico_carton(carton, 45, 55, i)

            elif j == 5:
                generar_unico_carton(carton, 56, 66, i)

            elif j == 6:
                generar_unico_carton(carton, 67, 77, i)

            elif j == 7:
                generar_unico_carton(carton, 78, 88, i)

            elif j == 8:
                generar_unico_carton(carton, 89, 99, i)

    elimina_cuatro_elementos_filas(carton)

    return carton

# Pre-condicion: ingresa una lista con las bolillas salidas para que no se repitan
# Post- condicion: retorna un numero de bolita nuevo que no salio todavia en un rango de 1-99
def genera_bolilla_azar(bolitas_salidas: list) -> int:

    aux: bool = True
    while aux:
        numero_bolita: int = random.randint(1,99)

        if numero_bolita not in bolitas_salidas:
            bolitas_salidas.append(numero_bolita)
            aux: bool = False

    return numero_bolita

# Pre-condicion: ingresa un diccionario de cartones,
# con el numero de filas y columnas que requiere
# Post- condicion: devuleve el diccionario actualizado
def genera_diez_cartas_azar(cartones: dict, fila: int, columna: int) -> dict :

    for i in range(1, 11):
        cartones[i] = crea_cartones(fila, columna)
    return cartones

# Pre-condicion:  entra un dict cargado de cartones y numero usuario
# Post- condicion: retorna una lista con los cartones del usuario
def distri_cartas_usuario(cartones: dict, cartones_usuario:list, numero_usuario: int) -> list:

    for i in range(1,numero_usuario + 1):
        cartones_usuario.append(cartones[i])
    return cartones_usuario

# Pre-condicion: entra un dict cargado de cartones y el numero maquina y numero de cartas maquina
# Post- condicion: retorna una lista con cartones de la  maquina
def distri_cartas_maquina(cartones: dict, cartones_maquina:list,numero_usuario ) -> list:

    for i in range(numero_usuario + 1, 11):
        cartones_maquina.append(cartones[i])
    return cartones_maquina

# Pre-condicion: entra una lista de cartones y el color un numero para el titulo
# Post- condicion: imprime por pantalla una lista de listas
def imprimir_cartas(lista: list, color:str, numero_titulo: int): 

    [print(colored(f"           Bingo {i+numero_titulo}",'green'), end="             ") for i in range(len(lista))]
    print()
    for i in range(len(lista[0])):
        if i!= 0:
            print(colored('╠══╬══╬══╬══╬══╬══╬══╬══╬══╣   ',color)*len(lista))
        else:
            print(colored('╔══╦══╦══╦══╦══╦══╦══╦══╦══╗   ',color)* len(lista))

        for j in range(len(lista)):
            for k in range(len(lista[0][0])):
                if k == 0:

                    print(colored('║',color), end="")
                # si el numero es menor a 10, agregar un 0 delante
                if lista[j][i][k] != '  ' and lista[j][i][k] != '❌':
                    if int(lista[j][i][k]) < 10:
                        if '0' not in str(lista[j][i][k]):
                            lista[j][i][k] = f'0{lista[j][i][k]}'

                print(colored(lista[j][i][k],color), end=colored('║',color))
            print('', end='   ')
        print()
    print(colored('╚══╩══╩══╩══╩══╩══╩══╩══╩══╝   ',color)*len(lista))

# Pre-condicion: ingresa una lista de cartones de cualquier longitud
# Post- condicion: divide los cartones mayores a 5 y imprime por pantallla
def imprime_cartones_longitud(carton, color):
    
    numero_titulo_carton = 1
    if len(carton) <= 5:

        imprimir_cartas( carton, color, numero_titulo_carton )

    elif len(carton) > 5: 
        primera_parte = []
        segunda_parte = []

        for i in range(len(carton)):
            if i <= 4:
                primera_parte.append(carton[i])

        for i in range(len(carton)):
            if i > 4:
                segunda_parte.append(carton[i])

        imprimir_cartas( primera_parte, color, numero_titulo_carton)
        numero_paratitulo = 6
        imprimir_cartas( segunda_parte, color,numero_paratitulo)
                
# Pre-condicion: El nuemro ingresado por el usuario tiene que ser un entero
# Post- condicion: retorna verdadero o falso
def valida_numero_usuario(numero_usuario: int) -> bool:
    return not(numero_usuario >= 1 and numero_usuario <= 5)
     
# Pre-condicion: El nuemro ingresado por el usuario tiene que ser un entero
# Post- condicion: valida que este en el rango 1 al 99
def valida_bolilla_marcado(numero_marcado: int) -> bool:
    return not(numero_marcado >= 1 and numero_marcado <= 99)
    
# Pre-condicion: el parametro que sea un numero
# Post- condicion: valida que este en el rango de 1 al 4
def valida_opcion(numero_marcado: int) -> bool:
    return not(numero_marcado >= 1 and numero_marcado <= 4)

# Pre-condicion: El nuemro ingresado por el usuario tiene que ser un entero
# Post- condicion: valida si esta en en el rango de 1  a 3
def valida_fila(fila: int) -> bool:
    return not(fila >= 1 and fila <= 3)  

# Pre-condicion: ingresa una lista cargada de  listas y un entero
# Post- condicion: retorna una lista de listas
def marca_bolilla(carton_usuario: list, bolilla_marcada: int) -> None:

    for i in range(len(carton_usuario)):
        for j in range(len(carton_usuario[i])):
            for k in range(len(carton_usuario[i][j])):
                if carton_usuario[i][j][k] != '  ' and carton_usuario[i][j][k] != '❌':
                    if bolilla_marcada == int(carton_usuario[i][j][k]):
                            carton_usuario[i][j][k] = '❌'

# Pre-condicion: entra un dict cargada con las lineas echas
# Post- condicion: retorna tru si hay 3 lineas
def verifica_gano(lineas_cartones: dict) -> bool:

    for i in lineas_cartones:
        if lineas_cartones[i] == 3:
            return True
    return False

# Pre-condicion: ingresa un numero ingresado por el usuario
# Post- condicion: valida si esta en el rango de nuemrod e cartas elegido por el usuario
def valida_num_carta(numero_carta: int, copia_usuario: list) -> bool:
    return not(numero_carta >= 1 and numero_carta <= len(copia_usuario))
        
# Pre-condicion: ingresa lista cargada con listas de listas se ejecuta cada 4 jugadas y tiramos una moneda al azar cara o seca 
# Post- condicion: si sale cara eliminamos una un carton de la lista pero si sale cello no hace nada retorna lista modificada 
def jugada_especial(copia_usuario: list ,moneda: int, fila: int, columna: int,carton_usuario: list,color_usuario: str,bolillas_salidas) -> None:

    cara:int = 1

    letra_jugada_especial: str ="""  
       _                               _                                                _           _     _   _ 
      | |                             | |                                              (_)         | |   | | | |
      | |  _   _    __ _    __ _    __| |   __ _      ___   ___   _ __     ___    ___   _    __ _  | |   | | | |
  _   | | | | | |  / _` |  / _` |  / _` |  / _` |    / _ \ / __| | '_ \   / _ \  / __| | |  / _` | | |   | | | |
 | |__| | | |_| | | (_| | | (_| | | (_| | | (_| |   |  __/ \__ \ | |_) | |  __/ | (__  | | | (_| | | |   |_| |_|
  \____/   \__,_|  \__, |  \__,_|  \__,_|  \__,_|    \___| |___/ | .__/   \___|  \___| |_|  \__,_| |_|   (_) (_)
                    __/ |                                        | |                                            
                   |___/                                         |_| """
    letra_cello: str = """  
                _   _                           _   _             _   _ 
               | | (_)                         | | | |           | | | |
  ___    __ _  | |  _    ___       ___    ___  | | | |   ___     | | | |
 / __|  / _` | | | | |  / _ \     / __|  / _ \ | | | |  / _ \    | | | |
 \__ \ | (_| | | | | | | (_) |   | (__  |  __/ | | | | | (_) |   |_| |_|
 |___/  \__,_| |_| |_|  \___/     \___|  \___| |_| |_|  \___/    (_) (_)"""
    letra_cara: str = """ 
                _   _                                             _   _ 
               | | (_)                                           | | | |
  ___    __ _  | |  _    ___       ___    __ _   _ __    __ _    | | | |
 / __|  / _` | | | | |  / _ \     / __|  / _` | | '__|  / _` |   | | | |
 \__ \ | (_| | | | | | | (_) |   | (__  | (_| | | |    | (_| |   |_| |_|
 |___/  \__,_| |_| |_|  \___/     \___|  \__,_| |_|     \__,_|   (_) (_)"""
    letra_carton: str = """         
                        _                                        _   _               _                            
                       | |                                      | | (_)             (_)                         _ 
   ___    __ _   _ __  | |_    ___    _ __       __ _      ___  | |  _   _ __ ___    _   _ __     __ _   _ __  (_)
  / __|  / _` | | '__| | __|  / _ \  | '_ \     / _` |    / _ \ | | | | | '_ ` _ \  | | | '_ \   / _` | | '__|    
 | (__  | (_| | | |    | |_  | (_) | | | | |   | (_| |   |  __/ | | | | | | | | | | | | | | | | | (_| | | |     _ 
  \___|  \__,_| |_|     \__|  \___/  |_| |_|    \__,_|    \___| |_| |_| |_| |_| |_| |_| |_| |_|  \__,_| |_|    (_)
                                                                                                                  """
    
    os.system('cls')
    numero_titulo = 1
    print(colored(f'{letra_jugada_especial}','red'))
    imprimir_cartas(copia_usuario,color_usuario, numero_titulo)
    print(colored("\n\nTIREMOS LA MONEDA !!!, CARA O CELLO SUERTE. \n","yellow"))

    if moneda == cara:

        print(colored(f'{letra_cara}','blue'))
        numero_carta: int = int(input(colored("\n\nIngrese numero de la carta que quiera eliminar : ",'green')))
        while valida_num_carta(numero_carta,copia_usuario):
            numero_carta: int = int(input(colored("\n\nIngrese numero de la carta que quiera eliminar : ",'green')))

        copia_usuario.pop(numero_carta - 1)
        nuevo_carton = crea_cartones(fila,columna)
        copia_nuevo_carton: list = copy.deepcopy(nuevo_carton)
        carta_marcada = marca_carta_nueva(nuevo_carton,bolillas_salidas )
        copia_usuario.append(carta_marcada)

        #Elimina tambien las cartas por usuario
        carton_usuario.pop(numero_carta - 1)
        carton_usuario.append(copia_nuevo_carton)
        tecla_seguir = input(colored("\nPresione Enter para seguir : ",'grey'))
    else:
        print(colored(f'{letra_cello}','blue'))
        tecla_seguir = input(colored("\nPresione Enter para seguir : ",'grey'))

# Pre-condicion: entra una lista de listas cargada con numeros del carton
# Post- condicion:  validamos si el usuario hizo linea en un carton
def valida_linea(carton: list, bolillas_salidas: list, bolillas_usuario: list, copia_usuario: list, color_usuario: str, num_titulo) -> bool:
    letra_caste: str = """ 
   _____                   _                   _              _        _                            _ 
  / ____|                 | |                 | |            | |      (_)                          | |
 | |        __ _   _ __   | |_    __ _   ___  | |_    ___    | |       _   _ __     ___    __ _    | |
 | |       / _` | | '_ \  | __|  / _` | / __| | __|  / _ \   | |      | | | '_ \   / _ \  / _` |   | |
 | |____  | (_| | | | | | | |_  | (_| | \__ \ | |_  |  __/   | |____  | | | | | | |  __/ | (_| |   |_|
  \_____|  \__,_| |_| |_|  \__|  \__,_| |___/  \__|  \___|   |______| |_| |_| |_|  \___|  \__,_|   (_)"""
    
    os.system('cls')
    print(colored(f'{letra_caste}\n','red'))
    imprimir_cartas(copia_usuario, color_usuario, num_titulo)

    num_carton: int = int(input(colored("\nIngrese numero de carton : " ,"grey")))
    while valida_num_carta(num_carton, carton):
        num_carton: int = int(input(colored("\nIngrese numero valido de carton : " ,"grey")))

    fila: int = int(input(colored("\nIngrese numero de la fila : ","grey")))
    while valida_fila(fila):
        fila: int = int(input(colored("\nIngrese numero valido de la fila : ","grey")))

    contador= 0
    for elementos in carton[num_carton-1][fila-1]:
        if elementos != '  ':
            if elementos in bolillas_salidas:
                if elementos in bolillas_usuario:
                    contador+=1
                    if contador == 5:
                        return True
    return False

# Pre-condicion: ingresa un carton nuevo 
# Post- condicion: retorna el carton marcado con las bolillas salidas 
def marca_carta_nueva(carton: list, bolillas_salidas: list) -> list:

    for i in range(len(carton)):
        for j in range(len(carton[i])):
            if carton[i][j] in bolillas_salidas:
                carton[i][j] = '❌'

    return carton

# Pre-condicion: entra un dict bacio 
# Post- condicion: retorna un dict actualizado con las lineas ganadas por carton enumerado
def guarda_lineas_ganadas(cartones: list , bolillas_salidas: list, bolillas_usuario: list, guarda_lineas: dict, cantidad_cartas: int, turno: bool) -> dict:

    lineas_carton: int = 0
    for carton in range(cantidad_cartas):
        contador_numeros = 0
        lineas_carton = 0
        for fila in range(3):
            for elementos in cartones[carton][fila]:
                if turno:
                        if elementos != '  ':
                            if elementos in bolillas_salidas and  elementos in bolillas_usuario:
                                contador_numeros+=1
                                if contador_numeros == 5:
                                    contador_numeros = 0
                                    # numero_lineas_total += 1
                                    lineas_carton += 1
                                    guarda_lineas[carton + 1] = lineas_carton
                            else:
                                contador_numeros = 0
                else:
                    if elementos != '  ': 
                            if elementos in bolillas_salidas:
                                contador_numeros+=1
                                if contador_numeros == 5:
                                    contador_numeros = 0
                                    # numero_lineas_total += 1
                                    lineas_carton += 1
                                    guarda_lineas[carton + 1] = lineas_carton
                            else:
                               contador_numeros = 0
    return guarda_lineas

# Pre-condicion: una lista vacia 
# Post- condicion: carga las opciones y imprime por pantalla
def imprimir_letra_si_gano(lineas_guardadas: dict) -> bool:
    for i in lineas_guardadas:
        if lineas_guardadas[i] == 3:
            return True

# Pre-condicion: ingresa un dcit cargado cada carton con todas las lineas ganadas
# Post- condicion: imprime las lineas ganadas o si hay bingo
def imprime_lineas_bingo(lineas_guardadas: dict, premio_bingo: int, premio_linea: int) -> None:
    lineas_ganadas: int = 0
    formo_tres_lineas_bingo: int = 0

    for i in lineas_guardadas:
        if lineas_guardadas[i] == 3:
            print(colored("\n########## BINGO! ##############",'yellow'))
            print(colored(f'En el carton {i} tienes :  {lineas_guardadas[i]} Linea\n','grey'))
            formo_tres_lineas_bingo += 1
            lineas_ganadas += lineas_guardadas[i]

        if lineas_guardadas[i] != 3:
            print(colored("\n********* LINEA!**************",'yellow'))
            print(colored(f'En el carton {i} tienes :  {lineas_guardadas[i]} Linea\n','yellow'))
            lineas_ganadas += lineas_guardadas[i]

    print(colored(f"\nGanaste Bingo un Monto de ${formo_tres_lineas_bingo * premio_bingo}",'red'))
    print(colored(f"\nGanaste formado lineas un Monto de ${lineas_ganadas * premio_linea}\n",'red'))

# Pre-condicion: una lista vacia 
# Post- condicion: carga las opciones y imprime por pantalla
def opcion_menu(opciones_juego) -> None:

    opciones_juego: list = ["Jugar Bingo","Mostrar Premio","Salir"]
    print(colored("\n#####  MENU #####  ",'grey'))
    for i in range(len(opciones_juego)):
        print(colored(f"\n{i+1}) {opciones_juego[i]}",'grey'))

# Pre-condicion: una lista vacia 
# Post- condicion: carga las opciones y imprime por pantalla
def opcion_menu_principal(opciones_lineas) -> None:

    opciones_lineas: list = ["Marcar bolilla","Cantar Linea","Cantar Bingo","No hacer nada"]
    print(colored("\n#####  MENU #####  \n",'grey'))
    for i in range(len(opciones_lineas)):
        print(colored(f"{i+1}) {opciones_lineas[i]}",'green'))
       
# Pre-condicion: en la todas las variables del juego  
# Post- condicion: retorna true o false
def jugar_bingo(copia_usuario: list, copia_maquina: list, bolitas_salidas: list, bolillas_usuario: list, letra_bingo: str, color_maquina: str,color_usuario: str,carton_usuario: list, carton_maquina: list, fila: int, columna: int, guarda_linea_de_usuario: dict, guarda_linea_de_maquina: dict, num_usuario: int, nombre_usuario: str, letra_computadora:str, letra_usuario: str, jugadores: dict) -> str :
    
    letra_linea: str = """  
  _   _             _                         _   _                        
 | \ | |           | |                       | | (_)                       
 |  \| |   ___     | |__     __ _   _   _    | |  _   _ __     ___    __ _ 
 | . ` |  / _ \    | '_ \   / _` | | | | |   | | | | | '_ \   / _ \  / _` |
 | |\  | | (_) |   | | | | | (_| | | |_| |   | | | | | | | | |  __/ | (_| |
 |_| \_|  \___/    |_| |_|  \__,_|  \__, |   |_| |_| |_| |_|  \___|  \__,_|
                                     __/ |                                 
                                    |___/ """
    premio_bingo: str = """  
                                        _               _    ___     ___     ___     ___  
                                       | |             | |  |__ \   / _ \   / _ \   / _ \ 
   __ _    __ _   _ __     __ _   ___  | |_    ___    / __)    ) | | | | | | | | | | | | |
  / _` |  / _` | | '_ \   / _` | / __| | __|  / _ \   \__ \   / /  | | | | | | | | | | | |
 | (_| | | (_| | | | | | | (_| | \__ \ | |_  |  __/   (   /  / /_  | |_| | | |_| | | |_| |
  \__, |  \__,_| |_| |_|  \__,_| |___/  \__|  \___|    |_|  |____|  \___/   \___/   \___/ 
   __/ |                                                                                  
  |___/ """
    felicitaciones: str = """ 
  ______          _   _          _   _                    _                                  _   _ 
 |  ____|        | | (_)        (_) | |                  (_)                                | | | |
 | |__      ___  | |  _    ___   _  | |_    __ _    ___   _    ___    _ __     ___   ___    | | | |
 |  __|    / _ \ | | | |  / __| | | | __|  / _` |  / __| | |  / _ \  | '_ \   / _ \ / __|   | | | |
 | |      |  __/ | | | | | (__  | | | |_  | (_| | | (__  | | | (_) | | | | | |  __/ \__ \   |_| |_|
 |_|       \___| |_| |_|  \___| |_|  \__|  \__,_|  \___| |_|  \___/  |_| |_|  \___| |___/   (_) (_)"""
    
    menu: list = []
    nadie_gano: str = 'nadie_gano'

    cantidad_jugadas = 1
    numero_titulo = 1
    cantidad_total_cartas: int = 10
    num_carta_maquina = cantidad_total_cartas - num_usuario

    aux: bool = True
    turno_usuario: bool = True
    turno_maquina: bool = False

    while aux:

        print(colored(f'{letra_usuario}\n','red'))
        imprimir_cartas(copia_usuario,color_usuario, numero_titulo)
        if cantidad_jugadas == 1:
            print(colored(f"\nHOLA {nombre_usuario.upper()} Bienvenido al Bingo virtual Suerte !! ",'green'))

        if cantidad_jugadas % 4 == 0:
            moneda: int = random.randint(0,1)
            jugada_especial(copia_usuario, moneda, fila, columna, carton_usuario, color_usuario, bolitas_salidas)
        
        numero_azar: int = genera_bolilla_azar(bolitas_salidas)
        print(colored(f'\nJUGADA {cantidad_jugadas} SALE  BOLILLA : {numero_azar}','yellow'))
        
        opcion_principal: str = input(colored(f'\n{nombre_usuario.upper()} queres jugar esta bolilla [S/N] : ','green'))
        if opcion_principal.upper() == 'S':
            salir: bool = True
            while salir:

                os.system('cls')
                print(colored(f'{letra_usuario}\n','red'))
                imprimir_cartas(copia_usuario,color_usuario, numero_titulo)
                print(colored(f'\nJUGADA {cantidad_jugadas} SALE  BOLILLA : {numero_azar}','yellow'))
                opcion_menu_principal(menu)

                opcion_segundaria:int = int(input(colored("\nIngrese una opcion: ",'grey')))
                while valida_opcion(opcion_segundaria):
                    opcion_segundaria:int = int(input(colored("\nIngrese una opcion que sea valido: ",'grey')))

                if opcion_segundaria == 1:
                    salir = False 
                    bolilla_marcada: int = int(input(colored(f"\nHola {nombre_usuario.upper()} Ingrese el Numero de la bolilla que quiere marcar: ",'grey')))
                    while  valida_bolilla_marcado(  bolilla_marcada):
                        bolilla_marcada: int = int(input(colored(f"\nHola {nombre_usuario.upper()} Ingrese el Numero de la bolilla que este en el rango de [1,99]: ",'grey')))

                    bolillas_usuario.append(bolilla_marcada)
                    marca_bolilla(copia_usuario, bolilla_marcada)
                        
                elif opcion_segundaria == 2:
                    if valida_linea(carton_usuario, bolitas_salidas, bolillas_usuario, copia_usuario,color_usuario,numero_titulo):
                        os.system('cls')
                        print(colored(f'{felicitaciones}','red'))
                        print(colored(f'{premio_bingo}','red'))
                        tecla_seguir = input(colored("\n\n\nPresione Enter para Seguir: ",'grey'))
                    else:
                        os.system('cls')
                        print(colored(f'{letra_linea}','red'))
                        tecla_seguir = input(colored("\n\n\nPresione Enter para Seguir: ",'grey'))
                
                elif opcion_segundaria == 3:
                    opcion = input(colored("\nEstas seguro de que quieres cantar Bingo [S/N]: ",'grey'))
                    if opcion.upper() == 'S':
                        return jugadores['usuario']
                
                elif opcion_segundaria == 4:
                    salir = False     

        if verifica_gano(guarda_linea_de_maquina ):
            return jugadores['computadora']
            
        marca_bolilla(copia_maquina, numero_azar)
        guarda_lineas_ganadas( carton_usuario, bolitas_salidas, bolillas_usuario, guarda_linea_de_usuario, num_usuario, turno_usuario)
        guarda_lineas_ganadas( carton_maquina, bolitas_salidas, bolillas_usuario, guarda_linea_de_maquina, num_carta_maquina, turno_maquina)
            
        os.system('cls')
        print(colored(letra_bingo + "\n" ,'green'))
        print(colored(f'{letra_computadora}\n','blue'))
        imprime_cartones_longitud(copia_maquina,color_maquina)

        cantidad_jugadas += 1
        if len(bolitas_salidas) == 99:
            return nadie_gano

#Programa principal
def main():

    letra_bingo:str = """ 
                 ____    _                                     _          _                     _ 
                |  _ \  (_)                                   (_)        | |                   | |
                | |_) |  _   _ __     __ _    ___     __   __  _   _ __  | |_   _   _    __ _  | |
                |  _ <  | | | '_ \   / _` |  / _ \    \ \ / / | | | '__| | __| | | | |  / _` | | |
                | |_) | | | | | | | | (_| | | (_) |    \ V /  | | | |    | |_  | |_| | | (_| | | |
                |____/  |_| |_| |_|  \__, |  \___/      \_/   |_| |_|     \__|  \__,_|  \__,_| |_|
                                     __/ |                                                       
                                    |___/ """
    letra_premio: str = """ 
  _____    _____    ______   __  __   _____    ____     _____     _ 
 |  __ \  |  __ \  |  ____| |  \/  | |_   _|  / __ \   / ____|   | |
 | |__) | | |__) | | |__    | \  / |   | |   | |  | | | (___     | |
 |  ___/  |  _  /  |  __|   | |\/| |   | |   | |  | |  \___ \    | |
 | |      | | \ \  | |____  | |  | |  _| |_  | |__| |  ____) |   |_|
 |_|      |_|  \_\ |______| |_|  |_| |_____|  \____/  |_____/    (_)
                                                                     """
    letra_gano: str = """ 
  ____    _____   _   _    _____    ____    _   _ 
 |  _ \  |_   _| | \ | |  / ____|  / __ \  | | | |
 | |_) |   | |   |  \| | | |  __  | |  | | | | | |
 |  _ <    | |   | . ` | | | |_ | | |  | | | | | |
 | |_) |  _| |_  | |\  | | |__| | | |__| | |_| |_|
 |____/  |_____| |_| \_|  \_____|  \____/  (_) (_)
                                                  """
    bingo: str = """   
  __         ____    _____   _   _    _____    ____       _    _____    ___     ___     ___     ___  
 /_ |       |  _ \  |_   _| | \ | |  / ____|  / __ \     | |  | ____|  / _ \   / _ \   / _ \   / _ \ 
  | |       | |_) |   | |   |  \| | | |  __  | |  | |   / __) | |__   | (_) | | | | | | | | | | | | |
  | |       |  _ <    | |   | . ` | | | |_ | | |  | |   \__ \ |___ \   > _ <  | | | | | | | | | | | |
  | |  _    | |_) |  _| |_  | |\  | | |__| | | |__| |   (   /  ___) | | (_) | | |_| | | |_| | | |_| |
  |_| (_)   |____/  |_____| |_| \_|  \_____|  \____/     |_|  |____/   \___/   \___/   \___/   \___/  """
    linea: str = """ 
  ___          _        _____   _   _   ______                 _    ___     ___     ___     ___  
 |__ \        | |      |_   _| | \ | | |  ____|     /\        | |  |__ \   / _ \   / _ \   / _ \ 
    ) |       | |        | |   |  \| | | |__       /  \      / __)    ) | | | | | | | | | | | | |
   / /        | |        | |   | . ` | |  __|     / /\ \     \__ \   / /  | | | | | | | | | | | |
  / /_   _    | |____   _| |_  | |\  | | |____   / ____ \    (   /  / /_  | |_| | | |_| | | |_| |
 |____| (_)   |______| |_____| |_| \_| |______| /_/    \_\    |_|  |____|  \___/   \___/   \___/ """
    letra_ganaste: str = """
   _____              _   _               _____   _______   ______     _            _    _____    ___     ___     ___     ___  
  / ____|     /\     | \ | |     /\      / ____| |__   __| |  ____|   | |    _     | |  | ____|  / _ \   / _ \   / _ \   / _ \ 
 | |  __     /  \    |  \| |    /  \    | (___      | |    | |__      | |   (_)   / __) | |__   | (_) | | | | | | | | | | | | |
 | | |_ |   / /\ \   | . ` |   / /\ \    \___ \     | |    |  __|     | |         \__ \ |___ \   > _ <  | | | | | | | | | | | |
 | |__| |  / ____ \  | |\  |  / ____ \   ____) |    | |    | |____    |_|    _    (   /  ___) | | (_) | | |_| | | |_| | | |_| |
  \_____| /_/    \_\ |_| \_| /_/    \_\ |_____/     |_|    |______|   (_)   (_)    |_|  |____/   \___/   \___/   \___/   \___/ 
                                                                                                                               """
    letra_usuario: str ="""  _   _   ___   _   _     _     ___   ___    ___  
 | | | | / __| | | | |   /_\   | _ \ |_ _|  / _ \ 
 | |_| | \__ \ | |_| |  / _ \  |   /  | |  | (_) |
  \___/  |___/  \___/  /_/ \_\ |_|_\ |___|  \___/"""
    letra_computadora: str = """   ___    ___    __  __   ___   _   _   _____     _     ___     ___    ___     _   
  / __|  / _ \  |  \/  | | _ \ | | | | |_   _|   /_\   |   \   / _ \  | _ \   /_\  
 | (__  | (_) | | |\/| | |  _/ | |_| |   | |    / _ \  | |) | | (_) | |   /  / _ \ 
  \___|  \___/  |_|  |_| |_|    \___/    |_|   /_/ \_\ |___/   \___/  |_|_\ /_/ \_\ """
    letra_perdiste = """ 
  _   _    ____       _____              _   _               _____   _______   ______     _ 
 | \ | |  / __ \     / ____|     /\     | \ | |     /\      / ____| |__   __| |  ____|   | |
 |  \| | | |  | |   | |  __     /  \    |  \| |    /  \    | (___      | |    | |__      | |
 | . ` | | |  | |   | | |_ |   / /\ \   | . ` |   / /\ \    \___ \     | |    |  __|     | |
 | |\  | | |__| |   | |__| |  / ____ \  | |\  |  / ____ \   ____) |    | |    | |____    |_|
 |_| \_|  \____/     \_____| /_/    \_\ |_| \_| /_/    \_\ |_____/     |_|    |______|   (_)"""
    letra_gracias = """ 
  __ _   _ _   __ _   __  (_)  __ _   ___    _ __   ___   _ _      (_)  _  _   __ _   __ _   _ _ 
 / _` | | '_| / _` | / _| | | / _` | (_-<   | '_ \ / _ \ | '_|     | | | || | / _` | / _` | | '_|
 \__, | |_|   \__,_| \__| |_| \__,_| /__/   | .__/ \___/ |_|      _/ |  \_,_| \__, | \__,_| |_|  
 |___/                                      |_|                  |__/         |___/"""
    
    jugadores: dict = {
        'usuario': '',
    'computadora': 'computadora'
    }

    premio_linea: int = 2000
    premio_bingo: int = 58000
    color_usuario: str = 'red'
    color_maquina: str = 'blue'
    numero_titulo = 1 
    fila_max: int = 3
    columna_max: int = 9

    cartones: dict = {}

    opciones_juego: list = []

    print(colored(f'{letra_bingo}','green'))
    opcion_menu(opciones_juego)
    opcion: int  = int(input(colored("\nIngrese una opcion: ","grey")))

    while opcion != 3:

        os.system('cls')
        if opcion == 1:
            cartones_usuario: list = []
            cartones_maquina: list = []

            bolitas_salidas: list = []
            bolillas_usuario: list = []

            guarda_linea_de_usuario: dict = {}
            guarda_linea_de_maquina: dict = {}
            
            #Genera 10 Cartas que en cada carton no se repitan los numeron 1 al 99
            genera_diez_cartas_azar(cartones, fila_max, columna_max)

            print(colored(f'{letra_bingo}','green'))

            nombre_usuario: str  = input(colored("Ingrese su Nombre Por Favor  : ",'grey'))
            jugadores['usuario'] = nombre_usuario 

            numero_usuario: int = int(input(colored(f"\nHola {nombre_usuario.upper()} Ingrese el numero de Cartas Para jugar: ",'grey')))
            while valida_numero_usuario(numero_usuario):
                numero_usuario: int = int(input(colored(f"Ingrese el numero de Cartas  Valido {nombre_usuario.upper()} ! que este  en el Rango[1,5]: ",'grey')))

            distri_cartas_usuario(cartones, cartones_usuario, numero_usuario)
            distri_cartas_maquina(cartones, cartones_maquina, numero_usuario)

            #copia de de respaldo de los cartones por usuario
            copia_usuario: list = copy.deepcopy(cartones_usuario)
            copia_maquina: list = copy.deepcopy(cartones_maquina)
            
            ganador: str =  jugar_bingo( copia_usuario, copia_maquina, bolitas_salidas, bolillas_usuario, letra_bingo, color_maquina, color_usuario, cartones_usuario,cartones_maquina, fila_max, columna_max, guarda_linea_de_usuario, guarda_linea_de_maquina, numero_usuario, nombre_usuario, letra_computadora, letra_usuario, jugadores)

            if ganador == jugadores['usuario']:

                os.system('cls')                       
                print(colored(f'{letra_usuario}\n','red'))
                imprimir_cartas( copia_usuario,color_usuario, numero_titulo)

                if imprimir_letra_si_gano(guarda_linea_de_usuario):

                    print(colored(f'{letra_gano}','red'))
                    print(colored(f'{letra_ganaste}','red'))
                    imprime_lineas_bingo(guarda_linea_de_usuario, premio_bingo, premio_linea)
                    seguir: str = input(colored("Enter para seguir : ",'grey'))

                else:
                    print(colored(f'{letra_perdiste}','blue'))
                    imprime_lineas_bingo(guarda_linea_de_usuario, premio_bingo, premio_linea)
                    seguir: str = input(colored("Enter para seguir : ",'grey'))

            
            if ganador == jugadores['computadora']:

                os.system('cls')
                print(colored(f'{letra_computadora}\n','blue'))
                imprime_cartones_longitud( copia_maquina,color_maquina)

                if imprimir_letra_si_gano(guarda_linea_de_maquina):
                    print(colored(f'{letra_gano}','blue'))
                    print(colored(f'{letra_ganaste}','blue'))
                    imprime_lineas_bingo(guarda_linea_de_maquina, premio_bingo, premio_linea)
                    seguir: str = input(colored("Enter para seguir : ",'grey'))

                else:
                    print(colored(f'{letra_perdiste}','blue'))
                    imprime_lineas_bingo(guarda_linea_de_maquina, premio_bingo, premio_linea)
                    seguir: str = input(colored("Enter para seguir : ",'grey'))
                    
            elif ganador == 'nadie':

                os.system('cls')
                print("No gano nadie")
                seguir: str = input(colored("Enter para seguir : ",'grey'))

        if opcion == 2:

            os.system('cls')
            print(colored(f'{letra_premio}','red'))
            print(colored(f'{bingo}','green'))
            print(colored(f'{linea}','green'))
            seguir: str = input(colored("\n\n\nEnter para seguir: ","grey"))

        os.system('cls')
        print(colored(f'{letra_bingo}','green'))

        opcion_menu(opciones_juego)
        opcion: int  = int(input(colored("\nIngrese una opcion: ", 'grey')))
    os.system('cls')
    print(colored(f"\n{letra_gracias}\n\n",'yellow'))

main()