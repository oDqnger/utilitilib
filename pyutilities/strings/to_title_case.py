def to_title_case(sentence: str) -> str:
    """Converts the first letter of each word in a sentence to uppercase, while converting all other letters to lowercase.

    Args:
        sentence (str): the string/sentence you want to change

    Returns:
        str: the string/sentence with the first letter of each word uppercased and all letters lowercased
    """
    try: 
        sentence = map(lambda item: item[0].upper()+item[1::].lower(),sentence.split(" "))
        return " ".join(sentence)
    except IndexError:
        return ""
