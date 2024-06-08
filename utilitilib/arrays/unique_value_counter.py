from .remove_duplicate import remove_duplicate

def unique_value_counter(arr: list) -> dict:
    """Generates a dictionary that contains occurences of unique values

    Args:
        arr (list): the list that the dict needs to be generated on

    Returns:
        dict: a dictionary that contains the occurences of each unique value in a list
    """
    unique_arr = remove_duplicate(arr)
    value_counter_dict = {}
    temp = 0
    
    for unique in unique_arr:
        for item in arr:
            if unique == item:
                temp += 1
                value_counter_dict[unique] = temp
        
        temp = 0
        
    return value_counter_dict
