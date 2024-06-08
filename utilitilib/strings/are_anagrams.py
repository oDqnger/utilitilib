def are_anagrams(str1: str, str2: str) -> bool:
    """Checks if two strings are anagrams of each other, i.e., if they contain the same characters with the same frequency, but not necessarily in the same order.

    Args:
        str1 (str): the first string
        str2 (str): the second string you need to compare the first string to

    Returns:
        bool: True if the two strings are anagrams, False if not.
    """
    if len(str1) == len(str2):
        for x in str1:
            if str2.count(x) > 1 or str2.count(x) == 0:
                return False
            
        return True
                
    return False
