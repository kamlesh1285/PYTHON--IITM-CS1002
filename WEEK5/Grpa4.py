#Implement the given functions according to the docstrings. 

# mapping

def is_greater_than_5(numbers: list) -> list:
    '''
    Given a list of numbers, return a list of bools corresponding
    to whether the number is greater than 5.
    '''
    return [num > 5 for num in numbers]


# filtering

def filter_less_than_5(numbers: list) -> list:
    '''
    Given a list of numbers, return a list of numbers that are less than 5.
    '''
    return [num for num in numbers if num < 5]


# aggregation with filtering

def sum_of_two_digit_numbers(numbers: list):
    '''
    Given a list of numbers find the sum of all two-digit numbers.
    '''
    return sum(num for num in numbers if 10 <= num <= 99)


# aggregation with mapping

def is_all_has_a(words: list) -> bool:
    '''
    Given a list of words check if all words have the letter 'a'
    (case insensitive) in them.
    '''
    return all('a' in word.lower() for word in words)


# enumerate

def print_with_numbering(items):
    '''
    Print a list in multiple lines with numbering.
    Example:
    apple
    orange
    banana

    Output:
    1. apple
    2. orange
    3. banana
    '''
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")


# zip

def parallel_print(countries, capitals):
    '''
    Print countries and capitals separated by " - ".
    '''
    for country, capital in zip(countries, capitals):
        print(f"{country} - {capital}")


# key-value list to dict

def make_dict(keys, values):
    '''
    Create a dictionary from keys and values.
    '''
    return dict(zip(keys, values))


# enumerate with filtering and mapping

def indices_of_big_words(words) -> list:
    '''
    Given a list of words, find the indices of words
    whose length is greater than 5.
    '''
    return [i for i, word in enumerate(words) if len(word) > 5]


# zip with mapping and aggregation

def decode_rle(chars: str, repeats: list) -> str:
    '''
    Create a string with the i-th character repeated
    repeats[i] times.

    Example:
    chars = "abc"
    repeats = [2, 3, 1]

    Output:
    "aabbbc"
    '''
    return ''.join(char * repeat for char, repeat in zip(chars, repeats)) 