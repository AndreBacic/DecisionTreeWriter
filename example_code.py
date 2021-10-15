
if __name__ == "__main__":
    from decision_tree_writer import DecisionTreeWriter

    # Here we're using some of the famous iris data set for an example.
    # You could alternatively make an Iris class with the same 
    # attributes as the keys of each of these dictionaries.
    iris_data = [
        { "species": "setosa", "sepal_length": 5.2, "sepal_width": 3.5, "petal_length": 1.5, "petal_width": 0.2},
        { "species": "setosa", "sepal_length": 5.2, "sepal_width": 4.1, "petal_length": 1.5, "petal_width": 0.1},
        { "species": "setosa", "sepal_length": 5.4, "sepal_width": 3.7, "petal_length": 1.5, "petal_width": 0.2},
        { "species": "versicolor", "sepal_length": 6.2, "sepal_width": 2.2, "petal_length": 4.5, "petal_width": 1.5},
        { "species": "versicolor", "sepal_length": 5.7, "sepal_width": 2.9, "petal_length": 4.2, "petal_width": 1.3},
        { "species": "versicolor", "sepal_length": 5.6, "sepal_width": 2.9, "petal_length": 3.6, "petal_width": 1.3},
        { "species": "virginica", "sepal_length": 7.2, "sepal_width": 3.2, "petal_length": 6.0, "petal_width": 1.8},
        { "species": "virginica", "sepal_length": 6.1, "sepal_width": 2.6, "petal_length": 5.6, "petal_width": 1.4},
        { "species": "virginica", "sepal_length": 6.8, "sepal_width": 3.0, "petal_length": 5.5, "petal_width": 2.1},
        ]

    # Create the writer. You must specify which attribute or key is the label of the data items.
    # You can also specify the max branching depth of the tree (default [and max] is 998)
    # or how many data items there must be to make a new branch (default is 1)
    writer = DecisionTreeWriter(label_name="species")

    # Trains a new model and saves it to a new .py file
    writer.create_tree(iris_data, True, "Iris Classifier")