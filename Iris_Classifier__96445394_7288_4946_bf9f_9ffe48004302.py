from decision_tree_writer.BaseDecisionTree import *

# Please fix this import statement if necessary
from example_data import Iris

# class-like syntax because it acts like it's instantiating a class.
def Iris_Classifier__96445394_7288_4946_bf9f_9ffe48004302() -> 'BaseDecisionTree':
    """
    Iris_Classifier__96445394_7288_4946_bf9f_9ffe48004302 has been trained to identify the species of a given Iris.
    """
    tree = BaseDecisionTree(None, Iris, 'Iris_Classifier__96445394_7288_4946_bf9f_9ffe48004302')
    tree.root = Branch(lambda x: x.sepal_length <= 5.5)
    tree.root.l = Leaf('setosa')
    tree.root.r = Branch(lambda x: x.petal_length <= 5.0)
    tree.root.r.l = Leaf('versicolor')
    tree.root.r.r = Leaf('virginica')
    
    return tree
