from decision_tree_writer import DecisionTreeWriter
from example_data import irises


# Create the writer. 
# You must specify which attribute or key is the label of the data items.
# You can also specify the max branching depth of the tree (default [and max] is 998)
# or how many data items there must be to make a new branch (default is 1).
writer = DecisionTreeWriter(label_name="species")

# Trains a new model and saves it to a new .py file.
writer.create_tree(data_set = irises, 
                   look_for_correlations = True, 
                   tree_name = "Iris Classifier")

# Because there is no specified file folder, the new file is created in this same directory
# and will have the working code for our new model.

# Now that we have the trained model, we can import and use it:
from Iris_Classifier__de3224c8_b2ce_4d58_b932_fefd793abee6 import *
trained_model = Iris_Classifier__de3224c8_b2ce_4d58_b932_fefd793abee6()

unlabeled_iris = Iris("?", 7.5, 3.1, 5.8, 1.7)
label = trained_model.classify_one(unlabeled_iris) # classifying an object doesn't change it's state in any way, so unlabeled_iris.species is still "?"
print(label) # virginica

# to actually label irises, their state must be changed to the labels the model gives:
more_irises = [
    Iris('?', 5.5, 3.9, 1.6, 0.3),
    Iris('??', 6.5, 2.3, 4.4, 1.6),
    Iris('???', 5.3, 3.6, 1.4, 0.2)
]
for i, label in enumerate(trained_model.classify_many(more_irises)):
    more_irises[i].species = label

# now the irises are properly labeled
for iris in more_irises:
    print(iris.species,end=", ") # setosa, versicolor, setosa, 