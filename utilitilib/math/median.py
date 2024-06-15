from utilitilib.math.mean import mean

def median(arr: list) -> float:
    """Finds the median (middle value) from a list of numbers

    Args:
        arr (list): the list that contains the numbers

    Returns:
        float: the median (or middle) value from that list
    """
    sorted_list = sorted(arr)
    
    if len(sorted_list) == 0:
        return None
    elif len(sorted_list) == 1:
        return sorted_list[0]
    elif len(sorted_list) % 2 != 0:
        return sorted_list[len(sorted_list) // 2]
    else:
        return mean([sorted_list[len(sorted_list)//2 - 1], sorted_list[len(sorted_list)//2]])
