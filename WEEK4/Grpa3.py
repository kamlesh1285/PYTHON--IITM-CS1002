# Implement the following functions:

#find_min: Find the minimum value in a list of integers.
#Input: A list of integers.
#Output: An integer, the minimum value in the list.
#odd_increment_even_decrement_no_modify: Increment all the odd numbers in a list by 1 and decrement all the even numbers by 1, without modifying the original list.
#Input: A list of integers.
#Output: A new list of integers with the modified values.
#odd_square_even_double_modify: Square all the odd numbers and double all the even numbers in a list, modifying the list in place.
#Input: A list of integers.
#Output: None (the input list is modified in place).
#more_than_two_unique_vowels: Given a string of comma-separated words, return a set containing words that have more than two unique vowels.
#Input: A string of comma-separated words.
#Output: A set of words with more than two unique vowels.
#sum_of_list_of_lists: Given a list of lists of integers, find the sum of all the integers in all the lists.
#Input: A list of lists of integers.
#Output: An integer, the sum of all the integers in the nested lists.
#flatten: Flatten a list of lists into a single list.
#Input: A list of lists.
#Output: A single flattened list.
#all_common: Find the common characters that are present in all strings in a list of strings and return them as a string in ascending order.
#Input: A list of strings.
#Output: A string containing common characters in ascending order.
#vocabulary: Given a list of sentences (with only alphabets and spaces), find the vocabulary (list of unique words) and return it as a set. Convert all words to lowercase before adding to the vocabulary.
#Input: A list of sentences.
#Output: A set of unique words in lowercase. 

def find_min(items: list):
    return min(items)


def odd_increment_even_decrement_no_modify(items) -> list:
    return [x + 1 if x % 2 else x - 1 for x in items]


def odd_square_even_double_modify(items: list) -> list:
    for i in range(len(items)):
        if items[i] % 2:
            items[i] = items[i] ** 2
        else:
            items[i] *= 2
    return items


def more_than_two_unique_vowels(sentence):
    words = sentence.split(',')
    vowels = set('aeiouAEIOU')
    return [
        word.strip()
        for word in words
        if len(set(ch for ch in word if ch in vowels)) > 2
    ]


def sum_of_list_of_lists(lol):
    return sum(sum(sublist) for sublist in lol)


def flatten(lol):
    return [item for sublist in lol for item in sublist]


def all_common(strings):
    if not strings:
        return ''

    common = set(strings[0])

    for s in strings[1:]:
        common &= set(s)

    return ''.join(sorted(common))


def vocabulary(sentences):
    vocab = set()

    for sentence in sentences:
        words = sentence.lower().split()
        vocab.update(words)

    return vocab 
