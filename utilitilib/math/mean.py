from typing import List, Union

def mean(array: List[Union[int, float]]) -> Union[int, float]:
    """Calculates the mean of all the numbers in a list

    Args:
        array (list): List containing numbers

    Returns:
        number: returns a int/float  
    """
    
    try:
        return (sum(array))/len(array)
    except Exception as e:
        raise e
    
