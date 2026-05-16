from validaciones import *
from heroes import lista_heroes


def ejecutar_menu():
    flag = True
    importado = False
    while flag == True:
        print("1 - Importar archivos")
        print("2 - Mostrar lista de héroes")
        print("3 - Agregar héroe")
        print("4 - Eliminar héroe")
        print("5 - Ordenar héroes alfabéticamente de la A a la Z")
        print("6 - Ver héroe más alto")
        print("7 - Ver héroe más fuerte")
        print("8 - Ver héroe más delgado")
        print("9 - Salir")
        opcion = validar_numero_rango(
            min=1, max=9, mensaje="Ingresá una opción: "
        )
        if opcion == 1:
            if importado == True:
                print("-----------------------------")
                print("La lista ya está importada")
                print("-----------------------------")
            else:
                importado = True
                print("-----------------------------")
                print("Lista importada")
                print("-----------------------------")
        elif opcion == 9:
            print("¡Hasta luego!")
            flag = False
        elif importado == True:
            if opcion == 2:
                mostrar_lista_heroes(lista=lista_heroes)
            elif opcion == 3:
                agregar_heroe(lista=lista_heroes)
            elif opcion == 4:
                eliminar_de_lista(
                    lista=lista_heroes,
                    mensaje_no_encontrado="El héroe pedido no existe",
                    mensaje_encontrado="Héroe borrado de la lista"
                )
            elif opcion == 5:
                ordenar_alfabeticamente_heroes(lista=lista_heroes)
            elif opcion == 6:
                print("-----------------------------")
                print("Héroe más alto")
                print("-----------------------------")
                buscar_mayor(lista=lista_heroes, indice=3)
            elif opcion == 7:
                print("-----------------------------")
                print("Héroe más fuerte")
                print("-----------------------------")
                buscar_mayor(lista=lista_heroes, indice=8)
            else:
                print("-----------------------------")
                print("Héroe más delgado")
                print("-----------------------------")
                buscar_menor(lista=lista_heroes, indice=4)
        else:
            print("-----------------------------")
            print("Error, lista no importada.")
            print("-----------------------------")


def mostrar_lista_heroes(lista: list):
    for i in range(len(lista)):
        print(f"NOMBRE = {lista[i][0]}")
        print(f"IDENTIDAD = {lista[i][1]}")
        print(f"EMPRESA = {lista[i][2]}")
        print(f"ALTURA = {lista[i][3]}")
        print(f"PESO = {lista[i][4]}")
        print(f"GÉNERO = {lista[i][5]}")
        print(f"COLOR DE OJOS = {lista[i][6]}")
        print(f"COLOR DE PELO = {lista[i][7]}")
        print(f"FUERZA = {lista[i][8]}")
        print(f"INTELIGENCIA = {lista[i][9]}")
        print("-----------------------------")


def agregar_heroe(lista: list):
    nombre = validar_cadena(
        mensaje="Ingresá un nombre: ",
        mensaje_error="Error, ingresá un nombre: "
    )
    identidad = validar_cadena(
        mensaje="Ingresá una identidad: ",
        mensaje_error="Error, ingresá una identidad: "
    )
    empresa = validar_empresa()
    altura = validar_numero_mayor(
        marca=1,
        mensaje="Ingresá la altura: ",
        mensaje_error="Error, ingresá una altura mayor a 0: "
    )
    peso = validar_numero_mayor(
        marca=1,
        mensaje="Ingresá el peso: ",
        mensaje_error="Error, ingresá un peso mayor a 0: "
    )
    genero = validar_genero()
    color_ojos = validar_cadena(
        mensaje="Ingresá el color de ojos: ",
        mensaje_error="Error, ingresá el color de ojos: "
    )
    color_pelo = validar_cadena(
        mensaje="Ingresá el color de pelo: ",
        mensaje_error="Error, ingresá el color de pelo: "
    )
    fuerza = validar_numero_mayor(
        marca=1,
        mensaje="Ingresá la fuerza: ",
        mensaje_error="Error, ingresá una fuerza mayor a 0: "
    )
    inteligencia = validar_inteligencia()
    nuevo_heroe = [
        nombre, identidad, empresa, altura, peso,
        genero, color_ojos, color_pelo, fuerza, inteligencia
    ]
    lista.append(nuevo_heroe)
    indice_nuevo_heroe = len(lista) - 1
    print("-----------------------------")
    print("Nuevo héroe agregado")
    print("-----------------------------")
    print(f"NOMBRE = {lista[indice_nuevo_heroe][0]}")
    print(f"IDENTIDAD = {lista[indice_nuevo_heroe][1]}")
    print(f"EMPRESA = {lista[indice_nuevo_heroe][2]}")
    print(f"ALTURA = {lista[indice_nuevo_heroe][3]}")
    print(f"PESO = {lista[indice_nuevo_heroe][4]}")
    print(f"GÉNERO = {lista[indice_nuevo_heroe][5]}")
    print(f"COLOR DE OJOS = {lista[indice_nuevo_heroe][6]}")
    print(f"COLOR DE PELO = {lista[indice_nuevo_heroe][7]}")
    print(f"FUERZA = {lista[indice_nuevo_heroe][8]}")
    print(f"INTELIGENCIA = {lista[indice_nuevo_heroe][9]}")
    print("-----------------------------")


def eliminar_de_lista(
    lista: list,
    mensaje_no_encontrado: str,
    mensaje_encontrado: str
):
    encontrado = False
    nombre = validar_cadena(
        mensaje="Ingresá el nombre del héroe que desea borrar: ",
        mensaje_error="Error, ingresá un nombre válido de héroe: "
    )
    for i in range(len(lista)):
        if lista[i][0] == nombre:
            lista.pop(i)
            encontrado = True
            print(mensaje_encontrado)
            break
    if encontrado == False:
        print(mensaje_no_encontrado)
    print("-----------------------------")


def ordenar_alfabeticamente_heroes(lista: list) -> list:
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[j][0] < lista[i][0]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print("-----------------------------")
    print("Héroes ordenados alfabéticamente")
    print("-----------------------------")
    for i in range(len(lista)):
        print(f"NOMBRE = {lista[i][0]}")
        print(f"IDENTIDAD = {lista[i][1]}")
        print(f"EMPRESA = {lista[i][2]}")
        print(f"ALTURA = {lista[i][3]}")
        print(f"PESO = {lista[i][4]}")
        print(f"GÉNERO = {lista[i][5]}")
        print(f"COLOR DE OJOS = {lista[i][6]}")
        print(f"COLOR DE PELO = {lista[i][7]}")
        print(f"FUERZA = {lista[i][8]}")
        print(f"INTELIGENCIA = {lista[i][9]}")
        print("-----------------------------")


def buscar_mayor(lista: list, indice: int):
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i][indice] > mayor[indice]:
            mayor = lista[i]
    print(f"\nNOMBRE = {mayor[0]}")
    print(f"IDENTIDAD = {mayor[1]}")
    print(f"EMPRESA = {mayor[2]}")
    print(f"ALTURA = {mayor[3]}")
    print(f"PESO = {mayor[4]}")
    print(f"GÉNERO = {mayor[5]}")
    print(f"COLOR DE OJOS = {mayor[6]}")
    print(f"COLOR DE PELO = {mayor[7]}")
    print(f"FUERZA = {mayor[8]}")
    print(f"INTELIGENCIA = {mayor[9]}")
    print("-----------------------------")


def buscar_menor(lista: list, indice: int):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i][indice] < menor[indice]:
            menor = lista[i]
    print(f"\nNOMBRE = {menor[0]}")
    print(f"IDENTIDAD = {menor[1]}")
    print(f"EMPRESA = {menor[2]}")
    print(f"ALTURA = {menor[3]}")
    print(f"PESO = {menor[4]}")
    print(f"GÉNERO = {menor[5]}")
    print(f"COLOR DE OJOS = {menor[6]}")
    print(f"COLOR DE PELO = {menor[7]}")
    print(f"FUERZA = {menor[8]}")
    print(f"INTELIGENCIA = {menor[9]}")
    print("-----------------------------")