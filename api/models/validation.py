def empty_field(self, value):
        """Checks if an object field is empty
    Args:
        value(object): can be a dict or a str
    Returns:
        bool: False for empty, True otherwise
    """
        none = value == None or value is None
        dict_len = type(value) == dict and len(value) == 0
        str_len = type(value) == str and len(value.strip()) == 0
        if none or dict_len or str_len:
            return True
        return False
