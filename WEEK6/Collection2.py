# Swap Alternate Elements in a Tuple
#Write a function to swap every alternate of adjacent elements in the tuple.

#Assume the length of the tuple is even. 

def swap_alternate_elements(t):
    '''Swap every alternate of adjacent elements in the tuple.

    Args:
        t (tuple): A tuple of even length.

    Returns:
        tuple: A new tuple with alternate elements swapped.

    Examples:
    >>> swap_alternate_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    >>> swap_alternate_elements(('a', 'b', 'c', 'd'))
    ('b', 'a', 'd', 'c')
    '''
    ...
    res = [] 
    
    for i in range(0, len(t), 2):
        res.append(t[i+1]) 
        res.append(t[i]) 
        
    return tuple(res)
    


