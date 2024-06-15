from utilitilib.strings.replace_one import replace_one

def format_num(num: int, custom_comma=",", custom_negative="-", custom_decimal=".") -> str:
    """Makes a number more readable by adding commas or by shortening it.

    Args:
        num (int): the number that needs to be formatted or shortened (more readable)

    Returns:
        str: the formatted or shortened string
    """
    formatted_num = ("{:,}".format(num))
    formatted_num = (
        formatted_num
        .replace(",", custom_comma)
        .replace("-" if formatted_num[0] == "-" else "", custom_negative if formatted_num[0] == "-" else "")
    )
    return replace_one(formatted_num, ".", custom_decimal)
