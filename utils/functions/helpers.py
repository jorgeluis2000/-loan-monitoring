def extract_customer_id(customer_id_str: str) -> int:
    """
    Extrae el ID del cliente de un string con el formato '<id> - <external_id>'
    """
    if isinstance(customer_id_str, str):
        return int(customer_id_str.split(' - ')[0])
    raise ValueError("customer_id_str debe ser una cadena")