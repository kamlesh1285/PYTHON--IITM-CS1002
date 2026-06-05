# A bit of wisdom 📖

#Iterable - Something that can be used in a for loop.
#Collection - Datatypes that hold many values like list, set, tuple and dict.
#All iterables are not collections. Eg. str and range are iterables but not collections.
#All collections are iterables.
#Only ordered collections are indexable and slicable
#Only Mutable collections can be modified
#Hasing is a method used in collections like set to check whether an element is present or not quickly, and in dict to retrive the value for the given key quickly. There are only certain datatypes that can be hashed. For example


empty_list = []
empty_set = set()
empty_tuple = ()

singleton_list = [1]
singleton_set = {1}
singleton_tuple = (1,)

a_falsy_list = []
a_falsy_set = set()
a_truthy_tuple = (0,)

int_iterable_min = min(int_iterable)
int_iterable_max = max(int_iterable)
int_iterable_sum = sum(int_iterable)
int_iterable_len = len(int_iterable)
int_iterable_sorted = sorted(int_iterable)
int_iterable_sorted_desc = sorted(int_iterable, reverse=True)

if hasattr(int_iterable, "__reversed__") and hasattr(int_iterable, "__getitem__"):
    int_iterable_reversed = list(reversed(int_iterable))
else:
    int_iterable_reversed = list(reversed(sorted(int_iterable)))

if hasattr(some_collection, "__getitem__") and hasattr(some_collection, "__len__"):
    third_last_element = some_collection[-3]
else:
    third_last_element = None

if hasattr(some_collection, "__getitem__"):
    odd_index_elements = some_collection[1::2]
else:
    odd_index_elements = None

is_some_value_in_some_collection = some_value in some_collection

if hasattr(some_collection, "__getitem__"):
    is_some_value_in_even_indices = some_value in some_collection[::2]
else:
    is_some_value_in_even_indices = None

all_iterables = list(some_iterable) + list(another_iterable) + list(yet_another_iterable)

if hasattr(string_iterable, "__getitem__"):
    all_concat = "-".join(string_iterable)
else:
    all_concat = "-".join(sorted(string_iterable))