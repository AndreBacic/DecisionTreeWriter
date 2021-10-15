from typing import List


class BaseDecisionTree(object):
    """
    A decision tree that classifies objects of type supported_data_type
    """
    def __init__(self, root: 'Branch', supported_data_type: type, name: str = "DecisionTreeModel") -> None:
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
        labels =[]
        for item in objects:
            labels.append(self.classify_one(item))
        return labels
    
    # Same functions used by DecisionTreeWriter for duck typing
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
