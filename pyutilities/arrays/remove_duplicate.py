def remove_duplicate(array: list) -> list:
    """A function that removes duplicates from an array

    Args:
        array (list): Can be any length list, with any type

    Returns:
        array (list): Returns a list with unique characters (all duplicates removed)
    """
    new_array = []

    for item in array:
        if item not in new_array:
            new_array.append(item)

    return new_array
