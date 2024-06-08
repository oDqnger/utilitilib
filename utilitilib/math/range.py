def range(arr: list) -> float:
    """Returns the range of a list (the difference between the lowest value and the highest)

    Args:
        arr (list): array of numbers

    Returns:
        float: the range of the array (difference between lowest and highest)
    """
    try:
        return float(max(arr) - min(arr))
    except:
        raise TypeError("Please provide an array with numbers only!")
