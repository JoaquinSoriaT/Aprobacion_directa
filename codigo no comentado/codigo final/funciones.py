from validaciones import *


def agregar_heroe(lista: list) -> None:
    """
    Descripción: Solicita los datos de un nuevo héroe al usuario y lo agrega a la lista.
    Parámetros: lista: Lista bidimensional donde se agregará un héroe nuevo.
    """
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
    fuerza = int(validar_numero_mayor(
        marca=1,
        mensaje="Ingresá la fuerza: ",
        mensaje_error="Error, ingresá una fuerza mayor a 0: "
    ))
    inteligencia = validar_inteligencia()
    nuevo_heroe = [
        nombre, identidad, empresa, altura, peso,
        genero, color_ojos, color_pelo, fuerza, inteligencia
    ]
    lista.append(nuevo_heroe)


def eliminar_de_lista_heroe(
    lista: list,
    mensaje_no_encontrado: str,
    mensaje_encontrado: str
) -> None:
    """
    Descripción: Elimina un héroe de la lista según el nombre ingresado por el usuario.
    Parámetros:
        lista: Lista bidimensional de héroes.
        mensaje_no_encontrado: Mensaje a mostrar si no se encuentra.
        mensaje_encontrado: Mensaje a mostrar si se elimina con éxito.
    """
    encontrado = False
    nombre = validar_cadena(
        mensaje="Ingresá el nombre del héroe que desea borrar: ",
        mensaje_error="Error, ingresá un nombre válido de héroe: "
    )
    for i in range(len(lista)):
        if lista[i][0] == nombre:
            lista.pop(i)
            encontrado = True
            print("-----------------------------")
            print(mensaje_encontrado)
            break
    if encontrado == False:
        print(mensaje_no_encontrado)
    print("-----------------------------")



