def validar_numero_rango(min: int, max: int, mensaje: str) -> int:
    opcion = int(input(mensaje))
    while opcion < min or opcion > max:
        opcion = int(input(mensaje))
    return opcion


def validar_numero_mayor(marca: int, mensaje: str, mensaje_error: str) -> int:
    opcion = int(input(mensaje))
    while opcion < marca:
        opcion = int(input(mensaje_error))
    return opcion


def validar_cadena(mensaje: str, mensaje_error: str) -> str:
    cadena = input(mensaje)
    while len(cadena) == 0:
        cadena = input(mensaje_error)
    return cadena


def validar_empresa() -> str:
    empresa = input("Ingresá una empresa (DC Comics / Marvel Comics): ")
    while (
        empresa.lower() != "dc comics"
        and empresa.lower() != "marvel comics"
    ):
        empresa = input(
            "Error, ingresá una empresa válida (DC Comics / Marvel Comics): "
        )
    if empresa.lower() == "dc comics":
        empresa = "DC Comics"
    else:
        empresa = "Marvel Comics"
    return empresa


def validar_genero() -> str:
    genero = input("Ingresá su género (M/F/NB): ")
    while (
        genero.upper() != "M"
        and genero.upper() != "F"
        and genero.upper() != "NB"
    ):
        genero = input("Error, ingresá un género válido (M/F/NB): ")
    return genero.upper()


def validar_inteligencia() -> str:
    inteligencia = input(
        "Ingresá la inteligencia (low/average/good/high/genius): "
    )
    while (
        inteligencia.lower() != "low"
        and inteligencia.lower() != "average"
        and inteligencia.lower() != "good"
        and inteligencia.lower() != "high"
        and inteligencia.lower() != "genius"
    ):
        inteligencia = input(
            "Error, ingresá una inteligencia válida"
            " (low/average/good/high/genius): "
        )
    return inteligencia.lower()