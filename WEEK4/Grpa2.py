#List mutating operations - This will help you learn the list methods and operations that will modify the list inplace. Note that you should not be creating a new list anywhere in this function.
#Create new lists - This will help you learn how to create new lists that resembles the result of above operations but does not affecting the original list.
#Set operations - This will help you learn things that you can do with sets.

def list_mutating_operations(items: list, item1, item2):
    # sort the items inplace
    items.sort()
    print("sorted:", items)

    # add item1 to the items at the end
    items.append(item1)
    print("append:", items)

    # add item2 at index 3
    items.insert(3, item2)
    print("insert:", items)

    # extend items with the first three elements in items
    items.extend(items[:3])
    print("extend:", items)

    # pop the fifth element
    popped_item = items.pop(4)
    print("pop:", items)

    # remove first occurrence of item2
    if item2 in items:
        items.remove(item2)
    print("remove:", items)

    # make the element at index 4 None
    if len(items) > 4:
        items[4] = None
    print("modify_index:", items)

    # make the even indices None
    items[::2] = [None] * len(items[::2])
    print("modify_slice:", items)

    # delete the third last element
    if len(items) >= 3:
        del items[-3]
    print("delete_index:", items)

    # delete the even indices
    del items[::2]
    print("delete_slice:", items)

    return items, popped_item


def list_non_mutating_operations(items: list, item1, item2):

    print("sorted:", sorted(items))

    # append
    print("append:", items + [item1])

    # insert at index 3
    print("insert:", items[:3] + [item2] + items[3:])

    # extend with first three elements
    print("extend:", items + items[:3])

    # remove fifth element
    print("pop:", items[:4] + items[5:])

    # remove first occurrence of item2
    if item2 in items:
        idx = items.index(item2)
        print("remove:", items[:idx] + items[idx + 1:])
    else:
        print("remove:", items)

    # modify fourth index
    print("modify_index:", items[:4] + [None] + items[5:])

    # modify even indices
    modified = items[:]
    modified[::2] = [None] * len(modified[::2])
    print("modify_slice:", modified)

    # delete even indices
    print("delete_slice:", items[1::2])

    return items


def do_set_operation(set1, set2, set3, item1, item2):

    # add item1 to set1
    set1.add(item1)
    print(sorted(set1))

    # remove item2 from set1
    set1.discard(item2) 
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    set1.difference_update(set3)
    print(sorted(set1))

    # common elements
    print(sorted(set2 & set3))

    # union
    print(sorted(set1 | set2 | set3))

    # set2 but not set3
    print(sorted(set2 - set3))

    # symmetric difference
    print(sorted(set2 ^ set3))

    return set1, sorted(set1), sorted(set2), sorted(set3)