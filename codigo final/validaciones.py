def validar_numero_rango(min: int, max: int, mensaje: str, mensaje_error: str) -> int:
    """
    Descripción: Valida que el número ingresado esté dentro del rango indicado.
    Parámetros:
        min: Valor mínimo aceptado.
        max: Valor máximo aceptado.
        mensaje: Mensaje que se muestra al pedir el número.
        mensaje_error: Mensaje que se muestra si el número no es válido.
    Retorno: Número validado dentro del rango.
    """
    opcion = int(input(mensaje))
    while opcion < min or opcion > max:
        opcion = int(input(mensaje_error))
    return opcion


def validar_numero_mayor(marca: float, mensaje: str, mensaje_error: str) -> float:
    """
    Descripción: Valida que el número ingresado sea mayor a la marca indicada.
    Parámetros:
        marca: Valor mínimo exclusivo aceptado.
        mensaje: Mensaje que se muestra al pedir el número.
        mensaje_error: Mensaje que se muestra si el número no es válido.
    Retorno: Número validado mayor a la marca.
    """
    opcion = float(input(mensaje))
    while opcion < marca:
        opcion = float(input(mensaje_error))
    return opcion


def validar_cadena(mensaje: str, mensaje_error: str) -> str:
    """
    Descripción: Valida que la cadena ingresada no esté vacía.
    Parámetros:
        mensaje: Mensaje que se muestra al pedir la cadena.
        mensaje_error: Mensaje que se muestra si la cadena está vacía.
    Retorno: Cadena validada no vacía.
    """
    cadena = input(mensaje)
    while len(cadena) == 0:
        cadena = input(mensaje_error)
    return cadena


def validar_empresa() -> str:
    """
    Descripción: Valida que la empresa ingresada sea DC Comics o Marvel Comics.
    Retorno: Empresa validada con formato correcto.
    """
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
    """
    Descripción: Valida que el género ingresado sea M, F o NB.
    Retorno: Género validado en mayúsculas.
    """
    genero = input("Ingresá su género (M/F/NB): ")
    while (
        genero.upper() != "M"
        and genero.upper() != "F"
        and genero.upper() != "NB"
    ):
        genero = input("Error, ingresá un género válido (M/F/NB): ")
    return genero.upper()


def validar_inteligencia() -> str:
    """
    Descripción: Valida que la inteligencia ingresada sea uno de los valores permitidos:
    low, average, good, high o genius.
    Retorno: Inteligencia validada en minúsculas.
    """
    inteligencia = input(
        "Ingresá la inteligencia"
        " (low/average/good/high/genius): "
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