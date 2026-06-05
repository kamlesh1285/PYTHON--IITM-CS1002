# dictionary_operations(fruit_prices: dict, fruits: list)

#Perform a series of operations on the given fruit_prices dictionary based on the fruits list:

#Add fruits[0] with a cost of 3.
#Modify the cost of fruits[1] to 2.
#Increase the cost of fruits[2] by 2.
#Delete fruits[3] from fruit_prices.
#Print the price of fruits[4].
#Print the names of fruits in fruit_prices as a sorted list.
#Print the prices of fruits in fruit_prices as a sorted list.
#increase_prices(fruit_prices: dict) -> None

#Increase the prices of every fruit by 20% and round to two decimal places. Modify the dictionary in place.

#dict_from_string(string: str, key_type, value_type)

#Convert a string with comma-separated key-value pairs into a dictionary, converting the keys and values to the specified types.

#Convert a dictionary back into a string with each key-value pair on a new line, using comprehensions.

def dictionary_operations(fruit_prices: dict, fruits: list):
    # add the fruit fruits[0] to fruit_prices with cost 3
    fruit_prices[fruits[0]] = 3
    order_print(fruit_prices)

    # modify the cost of fruits[1] as 2
    fruit_prices[fruits[1]] = 2
    order_print(fruit_prices)

    # increase the cost of fruits[2] by 2
    fruit_prices[fruits[2]] += 2
    order_print(fruit_prices)

    # delete fruits[3]
    del fruit_prices[fruits[3]]
    order_print(fruit_prices)

    # print price of fruits[4]
    print(fruit_prices[fruits[4]])

    # print sorted fruit names
    print(sorted(fruit_prices.keys()))

    # print sorted prices
    print(sorted(fruit_prices.values()))


def increase_prices(fruit_prices: dict) -> None:
    """
    Increase the prices of every fruit by 20 percent and round to two decimal places.
    """
    for fruit in fruit_prices:
        fruit_prices[fruit] = round(fruit_prices[fruit] * 1.2, 2)


def dict_from_string(string: str, key_type, value_type):
    """
    Create a dictionary from a string containing one key-value pair per line.
    """
    return {
        key_type(line.split(',')[0]): value_type(line.split(',')[1])
        for line in string.strip().split('\n')
        if line
    }


def dict_to_string(D: dict) -> str:
    """
    Convert dictionary to the format:
    key,value
    key,value
    """
    return '\n'.join(f'{k},{v}' for k, v in D.items()) 

