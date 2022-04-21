
# module that cleans a data set of dictionaries so that it can be used to train a decision tree
# note that in this library the labels are included in the data set
# all fields (well, keys) in the data set must be of the same type
# all fields/keys must be comparable, that is, they must be boolean, integer, or float (except for the label, which is always a string)
# all fields/keys must be unique (raise UncomparableDataSetException if not)
# all items must have the same keys (raise UncomparableDataSetException if not)


from typing import Dict, List


def clean_data_set(data_set: List[Dict]) -> List[Dict]:
    """
    Cleans a data set of dictionaries so that it can be used to train a decision tree.
    Raises UncomparableDataSetException if the data set cannot be successfully cleaned.

    O of time: O(n)
    O of space: O(1)
    """
    if len(data_set) <= 1:
        return data_set

    

    return data_set


# may be legacy code but I'm leaving it here for now
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