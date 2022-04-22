
# module that cleans a data set of dictionaries so that it can be used to train a decision tree
# note that in this library the labels are included in the data set

# GOAL is to modify the data set so is CLEAN
# A data set is CLEAN if all items: 
#   - have one and only one label (key of type str)
#   - have the same keys
#   - have values of type in [int, float, bool] (except for the label)
#   - have no duplicate keys
#   - have at least two key/value pairs after cleaning (label and at least one other key/value pair)

# if the data set cannot be cleaned, this method raises an UncomparableDataSetItemsException


from typing import Dict, List

        
def clean_data_set(data_set: List[Dict]) -> List[Dict]:
    """
    Cleans a data set of dictionaries so that it can be used to train a decision tree.
    Does not modify the data set in place, but returns a new, modified data set.

    Raises UncomparableDataSetException if the data set cannot be successfully cleaned.

    O of time: O(n)
    O of space: O(1)
    """
    if len(data_set) <= 1:
        return data_set

    # copy input data set so that we don't modify it in place
    data_set = data_set.copy()

    # iterate through the data set and clean each item
    

    return data_set


# may be legacy code but I'm leaving it here for now
# TODO: Fix this so that it doesn't use the first item in the data set to determine the type of the data set
def is_comparable_data_set(data_set: List[Dict]) -> bool:
    """
    Makes sure all items in data_set are of the same type.
    If the items are dictionaries, this method checks if they have the same keys.

    O of time: O(n)
    O of space: O(1)
    """
    if len(data_set) <= 1:
        return True

    needed_type = type(data_set[0])
    for item in data_set[1:]:
        if type(item) != needed_type:
            return False

    if needed_type == dict:
        needed_keys = data_set[0].keys()
        for item in data_set[1:]:
            if item.keys() != needed_keys:
                return False
    
    return True