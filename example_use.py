from decision_tree_writer import DecisionTreeWriter
from example_data import *


# Create the writer. 
# You must specify which attribute or key is the label of the data items.
# You can also specify the max branching depth of the tree (default [and max] is 998)
# or how many data items there must be to make a new branch (default is 1).
writer = DecisionTreeWriter(label_name="order")

# Trains a new model and saves it to a new .py file
writer.create_tree(data_set = dinosaurs, 
                   look_for_correlations = True, 
                   tree_name = "Dino Classifier")