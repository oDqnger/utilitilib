import datetime

def days_between_dates(date1: datetime.date, date2: datetime.date) -> int:
    
    """Returns the amount of days between two dates
    Args:
        date1 (): 
        date2 (): 

    Returns:
        int: the amount of days between the two dates.
    """
    return (date2 - date1).days

