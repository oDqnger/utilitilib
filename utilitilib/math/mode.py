from utilitilib.arrays.unique_value_counter import unique_value_counter

def mode(arr: list):
    """Returns the mode from a given list

    Args:
        array (list): A list containing any data type

    Returns:
        any: The mode of that current list
    """
    dict_of_vals = unique_value_counter(arr)
    arr_of_mode = []
    temp_val = 0

    for x,y in dict_of_vals.items():
        if y > temp_val:
            if len(arr_of_mode) != 0:
                arr_of_mode.clear()
            
            arr_of_mode.append(x)
            temp_val = y
        elif y == temp_val:
            arr_of_mode.append(x)
            temp_val = y

    return arr_of_mode[0] if len(arr_of_mode) == 1 else arr_of_mode

