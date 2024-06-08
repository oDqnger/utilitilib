def chunk_list(lst: list, size: int) -> list:
    """Chunks a list into smaller lists of a specified size

    Args:
        lst (list): original list to be chunked
        size (int): size of each chunk
        
    Returns:
        list: a list containing all the chunks
    """
    new_list = []
    temp_list = []
    temp_num = 0
    
    for x in lst:
        temp_list.append(x)
        temp_num += 1
        
        if (temp_num == size):
            temp_num = 0
            new_list.append(temp_list)
            temp_list = []
            
    if (len(temp_list) != 0):
        new_list.append(temp_list)
    
    return new_list
