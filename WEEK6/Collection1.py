# Rotate a list K times
#Given a list of items and an integer k, rotate the list to the right by k steps.

#Consider that the list contains at least one item. 

def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.


    Arguments:
    lst: list - a list of items
    k: int - the number of steps to rotate the list to the right

    Return:
    list - the rotated list
    '''
    ...
    n = len(lst) 
    
    k = k % n 
    
    return lst[-k:] + lst[:-k] 
    
    

