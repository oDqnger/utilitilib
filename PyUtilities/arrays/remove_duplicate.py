def remove_duplicate(array: list) -> list:
    new_array = []

    for item in array:
        if item not in new_array:
            new_array.append(item)

    return new_array
