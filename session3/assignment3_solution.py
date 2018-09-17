def get_value_milk(item_age, item_details):
    '''return the value of milk with given age and item_details.

    '''
    value = None
    if item_details == 'lonlon' and item_age <= 14:
        value = 150
    elif item_details == 'premium' and item_age <= 7:
        value = 200
    elif item_details == 'premium' and item_age <= 14:
        value = 150
    elif item_age <= 14:
        value = 100
    else:
        value = 0
    return value

def get_value_cheese(item_age):
    '''return the value of cheese of age item_age'''
    value = 100
    if item_age > 30:
        value_3_days = min(item_age-30, 360-30)
        value += value_3_days * 3
    if item_age > 360:
        value_4_days = min(item_age-360, 720-360)
        value += value_4_days * 4
    if item_age > 720:
        value -= (item_age-720) * 10
    return max(value, 0) # never return negative value

def get_value_whisky(item_age, cask_type, quality):
    '''return the value of whisky of given age, cask type and quality.

    Any whisky younger than 360 days has value 0.
    Whisky between 360 (inclusive) and 720 days has value 300 rupees.

    Value appreciation for different casks:
    1% per 30 days for "ex-sherry" cask.
    2% per 30 days for "ex-bourbon" cask.
    3% per 30 days for "ex-amarone" cask.

    The overall value of the whisky is multiplied by item quality,
    which is between 0 and 1 (inclusive).

    '''
    if item_age < 360:
        return 0 # not worth drinking...
    value = 300
    months = int(item_age / 30) # int() rounds down to closest integer
    if cask_type == 'ex-sherry' and months > 24:
        value *= pow(1.01, months-24)
    if cask_type == 'ex-bourbon' and months > 24:
        value *= pow(1.02, months-24)
    if cask_type == 'ex-amarone' and months > 24:
        value *= pow(1.03, months-24)
    return value * quality

def get_value(item_name, item_age, item_details):
    '''return the value of an item based on its name,  age and any further details given.

    args:

    item_name: the name of the item. given as a string.

    item_age: the age of the item measured in days.

    item_details: a string containing further details about the item. is the empty string ("")
    for items with no details.

    '''
    if not isinstance(item_name, str):
        raise TypeError('item_name must be a string')
    item_name = item_name.replace(' ', '').lower()
    item_details = item_details.replace(' ', '').lower()
    value = None
    if item_name == 'emptybottle':
        value = 1000
    if item_name == 'milk':
        value = get_value_milk(item_age, item_details)
    if item_name == 'agedcheese':
        value = get_value_cheese(item_age)
    if item_name == 'whisky':
        cask_type, quality = item_details.split(',')
        quality = float(quality) # convert string to float
        value = get_value_whisky(item_age, cask_type, quality)
    return value # returns None if no case triggers

def get_values(item_list):
    '''
    returns a list of values for each item in item_list. item_list is a list of
    lists with fields "item_name", "item_age", "item_details at index 0, 1, 2,
    respectively."
    '''
    # create an empty list for storing the values in
    values = list()

    # iterate over elements of item_list
    for item in item_list:

        # each element of item_list is a list of length 3
        # you can unpack these 3 values like we did with the string split.
        # item_name, item_age, item_details = item

        # you can also use explicit indices to extract each
        # value. this is the same as the above unpacking.
        item_name = item[0]
        item_age = item[1]
        item_details = item[2]

        # compute the value for this individual item
        value = get_value(item_name, item_age, item_details)

        # append the value to the list of values
        values.append(value)

    return values

def get_values(item_list):
    '''this is a fancier version of the above solution that is based on
    one of my favourite features in Python: list comprehension. both
    solutions yield exactly the same result but this one is more
    compact.

    '''
    # list comprehension is a way to write for loops in a very compact
    # way. it's equivalent to the above loop but much
    # shorter. creating an empty list and appending is handled
    # implicitly so we don't need to write it.
    return [get_value(item[0], item[1], item[2]) for item in item_list]
