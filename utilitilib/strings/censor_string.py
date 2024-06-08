def censor_string(string: str, censor_char: str="*", custom_swear_words: list= [], addition_swear_words: list=[], censor_char_amount: int=0) -> str:
    """Censors all the swear words in a string

    Args:
        string (str): the string that needs to be censored
        censor_char (str): the character that replaces the swear word in the string
        custom_swear_words (list): a list of your own words that you would like to censor (replaces the default list of swear words)
        addition_swear_words (list): a list of words that get added to the already existing default swear words

    Returns:
        str: the fully censored string
    """
    swear_words = ([
        "fuck",
        "shit",
        "bitch",
        "ass",
        "cunt",
        "dick",
        "arse",
        "bastard",
        "tits",
        "penis",
        "cock",
        "bullshit",
        "pussy",
        "motherfucker",
        "sex",
        "fucking"
        "shitty",
        "nigger",
        "nigga",
        "niggers",
        "niggas"
    ] if len(custom_swear_words) == 0 else custom_swear_words) + addition_swear_words
    
    new_string = string.lower()
    
    for x in swear_words:
        new_string = new_string.replace(x, "".join([censor_char for y in x] if censor_char_amount <= 0 else [censor_char for y in range(0, censor_char_amount)]))

    return new_string
