from src.decision_tree_writer import DecisionTreeWriter
from example_data import irises


# Create the writer. 
# You must specify which attribute or key is the label of the data items.
# You can also specify the max branching depth of the tree (default [and max] is 998)
# or how many data items there must be to make a new branch (default is 1).
writer = DecisionTreeWriter(label_name="species")

# Trains a new model and saves it to a new .py file
writer.create_tree(data_set = irises, 
                   look_for_correlations = True, 
                   tree_name = "Dino Classifier")

# Because there is no specified file folder, the new file is created in this same directory
# and will have the working code for our new model.

# Now that we have the trained model, we can import and use it:
