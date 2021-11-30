from decision_tree_writer.BaseDecisionTree import *
from typing import Dict, List, Tuple
import uuid

class DecisionTreeWriter:
    """
    Makes a decision tree based on a data set 
    and then saves it to a new .py file as a class extending BaseDecisionTree
    """
    def __init__(self, label_name = "LABEL", max_depth: int = 998, min_node_size: int = 1) -> None:
        self.max_depth = max_depth
        self.min_node_size = min_node_size
        self.label_name = label_name

        self.supported_field_types = [int, float, bool]

        self.__field_access_prefix = "."
        self.__field_access_postfix = ""

        self.math_funcs = [self.MATH_EQUALS, self.MATH_SUM, self.MATH_DIFFERENCE, self.MATH_PRODUCT, self.MATH_QUOTIENT]


    def create_tree(self, data_set: List[Dict or object], # TODO: Validate that all of the items in data_set have the same keys/attributes
                         look_for_correlations: bool = True, 
                         tree_name: str = "DecisionTreeModel",
                         file_folder: str = None) -> None:
        """
        self trains a decision tree to classify items of the type of items in data_set by its key/field self.label_name,
        and then writes the code for the new decision tree model to file_folder/tree_name__newUuid.py.

        All of the items in data_set must be of the same type, or the decision tree model produced may not function properly.

        look_for_correlations is whether or not the tree should be trained to look for simple relationships between all 
        possible pairs of the data items' fields. Setting this value to True can create a much better tree but can also take
        much longer to run. (if F is the number of a data item's fields, time and space complexity grow by O(F^2), as opposed to O(F))
        
        O of time: O(len(data_set)^2 * log2(len(data_set))) = O(n^2 * log2(n)) <- (best and probably average cases, worst is O(n^3))
        O of space: O(n)
        """

        tree_name = tree_name.replace(" ","_")
        
        guid = str(uuid.uuid4()).replace('-', '_')
        file_name = f"{tree_name}__{guid}"

        # TODO: make file writer import the object's class instead of guessing.
        is_dict, data_type = ("dictionary ", "dict") if type(data_set) == dict else ("", str(data_set[0].__class__.__name__))
        import_statement = ["", 
             "# Please fix this import statement if necessary",
            f"from {data_set[0].__class__.__module__} import {data_type}", 
             ""] if type(data_set) == dict else [""]

        file = ["from decision_tree_writer.BaseDecisionTree import *"]
        file += import_statement 
        file += [
                "# class-like syntax because it acts like it's instantiating a class.",
               f"def {file_name}() -> 'BaseDecisionTree':",
                '    """',
               f"    {file_name} has been trained to identify the {self.label_name} of a given {is_dict}object.",
                '    """',
               f"    tree = BaseDecisionTree(None, {data_type}, '{file_name}')"]

        # 1) Format data_set
        expanded_data_set = []

        if type(data_set[0]) != dict:
            expanded_data_set = list(map(lambda x: x.__dict__, data_set))
            self.__field_access_prefix = "."
            self.__field_access_postfix = ""
        else:
            expanded_data_set = list(data_set)
            self.__field_access_prefix = "['"
            self.__field_access_postfix = "']"

        if look_for_correlations:
            expanded_data_set = self.__find_correlations(expanded_data_set)

        # 2) recursively build branches or leaves based on best fit
        file += self.__build_branch(expanded_data_set, 1, ".root")

        file += ["    ", "    return tree"]

        
        self.__write_tree_file(file_name, file, file_folder)


    def __build_branch(self, data_set: List[Dict], depth: int, branch_chain: str) -> List[str]:
        """
        Recursively writes and returns a list of lines of code that define this branch of a decision tree.
        The list could be as small as the code for adding a Leaf, which just holds a label (a final decision)
        or it could define up to thousands of decision Branches, terminating in even more Leaves.
        
        O of time: O(n^2 * log(n)) <- (best and probably average cases, worst is O(n^3))
        O of space: O(n * log(n)) <- (best and probably average cases, worst is O(n^2))
        """
        # 1) check that all labels are different
        labels_are_same, primary_label = self.__check_labels(data_set)
        if labels_are_same or depth >= self.max_depth or len(data_set) <= self.min_node_size:
            return [f"    tree{branch_chain} = Leaf('{primary_label}')"]

        # 2) Find best field to split on and what value of it to split by
        file_additions = []

        max_gain = 0
        for field in data_set[0].keys():
            if field == self.label_name or not type(data_set[0][field]) in self.supported_field_types:
                continue
            data_set.sort(key = lambda x: x.get(field))
            fields = list(map(lambda x: x[field], data_set))
            labels = list(map(lambda x: x[self.label_name], data_set))
            gain, split_point = self.__calculate_max_gini_gain(labels, fields)
            if gain > max_gain:
                max_gain = gain
                value_to_split_by = split_point
                field_to_split_by = field

        # 3) Perform the decision split
        left_data_set, right_data_set = self.__split_data(data_set, field_to_split_by, value_to_split_by)

        # 4) Create new Branch
        if field_to_split_by[:10] == "tree.MATH_": # Correlated fields       # field_to_split_by is already formatted code
            file_additions.append(f"    tree{branch_chain} = Branch(lambda x: {field_to_split_by} <= {value_to_split_by})")
        else:
            file_additions.append(f"    tree{branch_chain} = Branch(lambda x: x{self.__field_access_prefix}{field_to_split_by}{self.__field_access_postfix} <= {value_to_split_by})")

        # 5) Recursively build new branches
        depth+=1
        file_additions += self.__build_branch(left_data_set, depth, f"{branch_chain}.l")
        file_additions += self.__build_branch(right_data_set, depth, f"{branch_chain}.r")

        return file_additions

    
    def __write_tree_file(self, file_name: str, lines: List[str], file_folder: str = None) -> None:
        """
        Writes all lines in lines to a new file named file_name.py in file_folder.
        """
        if file_folder: file_folder += "/"
        else: file_folder = ""
        
        file = None
        try:
            file = open(f"{file_folder}{file_name}.py", "w")
        except FileNotFoundError:
            file_folder = file_folder[:-1]
            raise FileNotFoundError(f"Error: file folder '{file_folder}' was not found." + 
                    " If you called an instance of DecisionTreeWriter's create_tree method, please ensure that parameter file_folder is an existing folder.")
            
        for line in lines:
            file.write(line+"\n")
        file.close()


    def __find_correlations(self, data_set: List[Dict]) -> List[Dict]:
        """
        Mutates and returns data_set after adding to it several new key-value pairs for each possible pair combinations of its fields,
        adding one pair of each combination for each basic math operation.
        
        O of time: O(len(data_set) * how_many_fields_are_in_an_item_in_data_set) = O(nF) = O(n)
        O of space: O(how_many_fields_are_in_an_item_in_data_set^2) = O(1)
        """
        # 1 Get all fields we can work with
        fields = list(filter(lambda x: type(data_set[0][x]) in self.supported_field_types, data_set[0].keys()))
        
        # 2 get all pairs
        pairs = []
        for i, field in enumerate(fields):
            for other_field in fields[i+1:]:
                pairs.append((field, other_field))

        # 3 Add a field for the sum, diff, product, and quotient of each field.
        for item in data_set:
            for pair in pairs:
                for func in self.math_funcs:
                    # item key is the code to be written later
                    item[f"tree.{func.__name__}(x{self.__field_access_prefix}{pair[0]}{self.__field_access_postfix}, x{self.__field_access_prefix}{pair[1]}{self.__field_access_postfix})"] = func(item[pair[0]], item[pair[1]])      
        
        return data_set


    def __check_labels(self, data_set: List[Dict]) -> Tuple[bool, str]:
        """
        Checks if all of the labels of the items in data_set are the same.
        
        Returns if they are all the same, and what the most frequent label is.
        
        O of time: O(len(data_set)) = O(n)
        O of space: Worst case O(n), best is O(1) and average is probably O(log(n)), but that depends on data_set.
        """
        counted_labels = dict()
        primary_label = None
        primary_label_count = 0
        for i in data_set:
            if counted_labels.get(i[self.label_name]):
                counted_labels[i[self.label_name]] += 1
            else:
                counted_labels[i[self.label_name]] = 1
            
            if counted_labels[i[self.label_name]] > primary_label_count:
                primary_label_count = counted_labels[i[self.label_name]]
                primary_label = i[self.label_name]
        
        return len(counted_labels.keys()) == 1, primary_label        


    def __split_data(self, data_set: List[Dict], field_to_split_by: str, value_to_split_by) -> Tuple[List[Dict], List[Dict]]:
        """
        Splits data_set into two new lists, separating all items into the first list where field_to_split_by <= value_to_split_by, and the rest into the second.

        O of time: O(len(data_set)) = O(n)
        O of space: O(n)
        """
        left = []
        right = []
        for item in data_set:
            if item[field_to_split_by] <= value_to_split_by:
                left.append(item)
            else:
                right.append(item)

        return left, right


    def __calculate_max_gini_gain(self, labels: List[str], fields: List) -> Tuple[float, float]:
        """
        Determines at what value in between some items of fields a data list should be split
        to minimize the gini impurity of the labels of the data list.

        fields must be sorted in ascending order and the labels sorted to match each field of the same index.

        Returns the maximum gini gain obtainable by spliting the data list by the given field, and what value of
        that field to split by.

        O of time: O(len(labels)*len(fields)), and since those lengths are equal that's O(n^2)
        O of space: O(n) <- ( O(len(labels)) )
        """
        if not (fields and labels) or len(fields) != len(labels): return 0

        max_gain = 0
        H = self.calculate_gini_impurity(labels)
        l = len(labels)
        l1 = []
        l2 = list(labels)
        value_to_split_by = None
        for i, val in enumerate(fields):
            l1.append(l2.pop(0))
            if len(l2) == 0: break

            if val == fields[i+1]: continue

            H1 = self.calculate_gini_impurity(l1) * len(l1) / l
            H2 = self.calculate_gini_impurity(l2) * len(l2) / l
            gain = round(H - H1 - H2, 7)
            if gain > max_gain or (gain == max_gain and i < l/2): # second case motivates the alg to split in the middle
                max_gain = gain
                value_to_split_by = (val + fields[i+1])/2
        
        return max_gain, value_to_split_by


    def calculate_gini_impurity(self, input: List) -> float:
        """
        Returns the Gini impurity of input (0 means all of the items are the same, > 0.5 is pretty mixed)

        O of time: O(n)
        O of space: O(how_many_different_labels_are_in_input), which is at worst O(n) and at best O(1), and in practice probably O(log(n))
        """
        # return 1 - Sum from i=1 to n of (Probability(Xi)**2)
        if not input: return 0.0

        probs = dict()
        p = 1 / len(input)
        for i in input:
            if probs.get(i):
                probs[i] += p
                continue
            probs[i] = p
        
        s = 1.0
        for i in probs.values():
            s -= i*i # returns the negative of the sum, so just minus each time.
        
        s = round(s, 7) # resolves some weird rounding errors
        return s

    def __get_max_depth(self):
        return self.__max_depth
    def __set_max_depth(self, val: int):
        if val > 998: val = 998
        elif val < 1: val = 1
        self.__max_depth = val
    max_depth = property(__get_max_depth, __set_max_depth)

    def __get_min_node_size(self):
        return self.__min_node_size
    def __set_min_node_size(self, val: int):
        if val < 1: val = 1
        self.__min_node_size = val
    max_depth = property(__get_min_node_size, __set_min_node_size)


    # Same functions used by BaseDecisionTree for duck typing
    def MATH_EQUALS(self, n1, n2) -> float:
        return float(n1 == n2)
    def MATH_SUM(self, n1, n2) -> float:
        return n1+n2
    def MATH_DIFFERENCE(self, n1, n2) -> float:
        return n1-n2
    def MATH_PRODUCT(self, n1, n2) -> float:
        return n1*n2
    def MATH_QUOTIENT(self, n1, n2) -> float:
        """Divides n1 by n2 but returns n1 * 2**128 if n2 is zero."""
        if n2 == 0:
            return n1*340282366920938463463374607431768211456 # 2**128
        return n1+n2
