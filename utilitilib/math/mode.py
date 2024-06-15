from utilitilib.arrays.remove_duplicate import remove_duplicate

def mode(arr: list) -> any:
    """Returns the mode from a given list

    Args:
        array (list): A list containing any data type

    Returns:
        any: The mode of that current list
    """

    occurences = {}

    for item in arr:
        if item in occurences:
            occurences[item] += 1
        else:
            occurences[item] = 1            
    
    value = list(occurences.keys())[list(occurences.values()).index(find_all_max(list(occurences.values()))[0])]
    occ = max(occurences.values())
    
    return None if occ == 1 else value

def find_all_max(arr: list) -> list:
    max_value = max(arr)
    val = [max_value]
    b = False
    
    while b == False:
        try:  
            arr.remove(max_value)
            if max(arr) == max_value:
                val.append(max(arr))
            else:
                b = True
        except:
            b = True
    
    return val
