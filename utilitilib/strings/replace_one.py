def replace_one(string: str, replace_char: str, char) -> str:
    """Replaces one occurence of a value, instead of multiple occurences

    Args:
        string (str): the string that has the characters that needs to be replaced
        replace_char (str): the character that needs to be replaced in the string
        char (str): the character that replace_char needs to be replaced with

    Returns:
        str: the newly created string with the char removed from it
    """
    string_list = list(string)
    if (string.rfind(replace_char) != -1):
        string_list[string.rfind(replace_char)] = char
        return "".join(string_list)
    else:
        return string
