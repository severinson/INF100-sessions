# Dictionaries store key-value mappings (like Hashes in Ruby)
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values with []
filled_dict["one"] #=> 1

# Get all keys as a list with "keys()"
filled_dict.keys() #=> ["three", "two", "one"]

# Get all values as a list with "values()"
filled_dict.values() #=> [3, 2, 1]

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict #=> True
1 in filled_dict #=> False

# Looking up a non-existing key is a KeyError
filled_dict["four"] # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one") #=> 1
filled_dict.get("four") #=> None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4) #=> 1
filled_dict.get("four", 4) #=> 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5) #filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6) #filled_dict["five"] is still 5
