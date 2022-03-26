from typing import List
from decision_tree_writer.CorrelatedDataComparer import CorrelatedDataComparer


class BaseDecisionTree(CorrelatedDataComparer):
    """
    A decision tree that classifies objects of type supported_data_type
    """
    def __init__(self, supported_data_type: type, name: str = "DecisionTreeModel", root: 'Branch' = None) -> None:
        self.root = root
        self.supported_data_type = supported_data_type
        self.name = name
    
    def classify_one(self, obj) -> str:
        """
        Returns what self thinks is the correct label for obj based on the data self has been trained by.
        """
        if not isinstance(obj, self.supported_data_type): return None

        return self.root.classify(obj)

    def classify_many(self, objects: List['object']) -> List[str]:
        """
        Returns a list of (hopefully) correct labels for each item in objects.
        """
        labels = []
        for item in objects:
            labels.append(self.classify_one(item))
        return labels


class Branch():
    """
    Given a decision_func that takes an object and returns a bool, 
    a Branch will choose its left node (self.l) if the function returns true, 
    and its right node (self.r) otherwise.

    Valid types for self.l and self.r are Branch or Leaf.
    """
    def __init__(self, decision_func: 'function') -> None:
        self.l: 'Branch' or 'Leaf' = None
        self.r: 'Branch' or 'Leaf' = None
        self.decision_func = decision_func

    def classify(self, obj) -> str:
        if self.decision_func(obj):
            return self.l.classify(obj)
        return self.r.classify(obj)


class Leaf():
    """
    A final decision node of a decision tree that holds a string value that is the classification.
    """
    def __init__(self, value: str) -> None:
        self.value = value

    def classify(self, obj) -> str:
        return self.value
