# Decision Tree Writer

This package allows you to train a binary classification decision tree on a list of labeled dictionaries or class instances, and then writes a new .py file with the code for the new decision tree model.

## Installation
Simply run `py -m pip install decision-tree-writer` from the command line (Windows)
or `python3 -m pip install decision-tree-writer` (Unix/macOS) and you're ready to go!

## Usage
### 0) Gather training data
Models are trained on a list of labeled dictionaries or objects. The algorithm only looks at attributes/keys that have numeric or Boolean values, so all nested objects or strings are simply ignored. If you train it with dictionaries, all of the items must have the same keys (with numeric or Boolean values; each can have different keys with string or object or whatever else values). Similarly, if you give it a list of objects, they must all have the same attributes (with integer, floating-point, or Boolean values). Finally, all of the items in the data set must have a label attribute/key that has the same name for each item, and can have any value (as shown in this example data set):
```python
# Here we're using some of the famous iris data set for an example.
iris_data = [
    { "species": "setosa", "sepal_length": 5.2, "sepal_width": 3.5, 
                            "petal_length": 1.5, "petal_width": 0.2},
    { "species": "setosa", "sepal_length": 5.2, "sepal_width": 4.1, 
                            "petal_length": 1.5, "petal_width": 0.1},
    { "species": "setosa", "sepal_length": 5.4, "sepal_width": 3.7, 
                            "petal_length": 1.5, "petal_width": 0.2},
    { "species": "versicolor", "sepal_length": 6.2, "sepal_width": 2.2, 
                            "petal_length": 4.5, "petal_width": 1.5},
    { "species": "versicolor", "sepal_length": 5.7, "sepal_width": 2.9, 
                            "petal_length": 4.2, "petal_width": 1.3},
    { "species": "versicolor", "sepal_length": 5.6, "sepal_width": 2.9, 
                            "petal_length": 3.6, "petal_width": 1.3},
    { "species": "virginica", "sepal_length": 7.2, "sepal_width": 3.2, 
                            "petal_length": 6.0, "petal_width": 1.8},
    { "species": "virginica", "sepal_length": 6.1, "sepal_width": 2.6, 
                            "petal_length": 5.6, "petal_width": 1.4},
    { "species": "virginica", "sepal_length": 6.8, "sepal_width": 3.0, 
                            "petal_length": 5.5, "petal_width": 2.1}
    ]
```

You could alternatively make an Iris class with the same attributes as the keys of each of these dictionaries:
```python
from dataclasses import dataclass
@dataclass
class Iris:
    species: str
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
# And then instantiate twelve Iris objects with the previous data
```
### 1) Train the model
Use the DecisionTreeWriter class to train a model on a data set and write the code to a new file in a specified file folder (default folder is the same as your code) The label of an item in the training data set is a specified attribute or key (in this example, the key "species"):
```python
from decision_tree_writer import DecisionTreeWriter


# Create the writer. 
# You must specify which attribute or key is the label of the data items.
# You can also specify the max branching depth of the tree (default [and max] is 998)
# or how many data items there must be to make a new branch (default is 1).
writer = DecisionTreeWriter(label_name="species")

# Trains a new model and saves it to a new .py file.
writer.create_tree(data_set = iris_data, 
                   look_for_correlations = True, 
                   tree_name = "Iris Classifier")
```

### 2) Using the new decision tree
In the specified file folder a new python file with one function will appear. It will have the name you gave your decision tree model plus a uuid to ensure it has a unique name. The generated code will look something like this:
```python
from decision_tree_writer.BaseDecisionTree import *

# class-like syntax because it acts like it's instantiating a class.
def Iris_Classifier__0c609d3a_741e_4770_8bce_df246bad054d() -> 'BaseDecisionTree':
    """
    Iris_Classifier__0c609d3a_741e_4770_8bce_df246bad054d 
    has been trained to identify the species of a given object.
    """
    tree = BaseDecisionTree(None, dict,
            'Iris_Classifier__0c609d3a_741e_4770_8bce_df246bad054d')
    tree.root = Branch(lambda x: x['sepal_length'] <= 5.5)
    tree.root.l = Leaf('setosa')
    tree.root.r = Branch(lambda x: x['petal_length'] <= 5.0)
    tree.root.r.l = Leaf('versicolor')
    tree.root.r.r = Leaf('virginica')
    
    return tree
```

**Important note**: if you train your model with class instance data you may have to change the import statement for that class in the new file if the class is in a file in a different directory from where you have the model's file placed.
The code for a model trained with objects would look like: 
```python
from decision_tree_writer.BaseDecisionTree import *

# Please fix this import statement if necessary
from sample_data.flowers import Iris

def Iris_Classifier__0c609d3a_741e_4770_8bce_df246bad054d() -> 'BaseDecisionTree':
    tree = BaseDecisionTree(None, Iris, 
                'Iris_Classifier__0c609d3a_741e_4770_8bce_df246bad054d')
```

Now just use the factory function to create an instance of the model.
The model has two important methods, `classify_one`, which takes a data item of the same type as you trained the model with and returns what it thinks is the correct label for it, and `classify_many`, which does the same as the first but with a list of data and returns a list of labels.

Example:
```python
tree = IrisClassifier__0c609d3a_741e_4770_8bce_df246bad054d()
print(tree.classify_one(
            { "sepal_length": 5.4, "sepal_width": 3.2, 
                "petal_length": 1.6, "petal_width": 0.3})) # output: 'setosa'
```

## Bugs or questions
If you find any problems with this package of have any questions, please create an issue on [this package's GitHub repo](https://github.com/AndreBacic/DecisionTreeWriter/issues)
