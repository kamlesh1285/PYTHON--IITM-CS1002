# Find percentage increased
#Write a function to calculate the percentage increase from the original value to the new value.

#Assume original is less than or equal to new.

def percentage_increased(original, new):
    '''Calculate the percentage increase from the original value to the new value.

    Assume original is less than or equal to new.

    Args:
        original (float): The original value.
        new (float): The new value.

    Returns:
        float: The percentage increase.

    Examples:
    >>> percentage_increased(50, 75)
    50.0
    >>> percentage_increased(80, 100)
    25.0
    '''
    ...
    x = ((new-original)/original * 100)
    return x 

