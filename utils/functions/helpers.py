def extract_customer_id(customer_id_str: str) -> int:
    """
    Extrae el ID del cliente de un string con el formato '<id> - <external_id>'.

    Args:
        customer_id_str (str): El string que contiene el ID del cliente y el ID externo separados por ' - '.

    Returns:
        int: El ID del cliente extraído del string.

    Raises:
        ValueError: Si el string no está en el formato esperado o no se puede convertir a un entero.
    """
    if isinstance(customer_id_str, str):
        try:
            return int(customer_id_str.split(' - ')[0])
        except (IndexError, ValueError) as e:
            raise ValueError("El string no está en el formato esperado o no se puede convertir a un entero.") from e


def jsonDefault(object):
    """
    Convierte un objeto en un diccionario para su serialización JSON.

    Args:
        object (object): El objeto a convertir.

    Returns:
        dict: El diccionario que representa el objeto.
    """
    return object.__dict__
