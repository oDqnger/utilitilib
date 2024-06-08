import random

def shuffle(array: list) -> list:
    """
    Shuffles a list

    Args:
        array (list): the list to be shuffled

    Returns:
        list: the shuffled list
    """
    new_array = []
    indexes_of_array = [x for x in range(0, len(array))]
    
    for item in array:
        random_index = random.randrange(0, len(indexes_of_array))
        new_array.append(array[indexes_of_array[random_index]])
        
        indexes_of_array.remove(indexes_of_array[random_index])
        
    return new_array
