def remove_all(arr: list, item: any) -> list:
    """Removes all specified elements from a list

    Args:
        arr (list): the array that needs the object to be removed from
        item (any): the item/object that needs to get removed from the array.

    Returns:
        list: the new list (all elements removed from it)
    """
    new_list = []
    
    
    for i in arr:
        if i != item:
            new_list.append(i)
            
    return new_list
