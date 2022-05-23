from decision_tree_writer.TreeWriter import DecisionTreeWriter
# ✓ (v0.4.1): delete the unused root parameter from BaseDecisionTree for cleaner scaffolded code.
# ✓ (v0.4.2): move data validating and cleaning to a separate class from DecisionTreeWriter and add better validating and cleaning methods
# ✓ (v0.5.1): Have max_depth and min_node_size as parameters for DecisionTreeWriter.create_tree()

# TODO: Refactor DataCleaner (see class todos) (v0.5.2)
# TODO: Refactor TreeWriter fields and properties to be more consistent with what actions change them (ex. passing in max_depth changes it but passing in folder doesn't, and you can't pass in label_name) (v0.5.3)
# TODO: Possibly good idea: Why would you need multiple tree writers? Wouldn't a static class work for multithreading? If so, make DecisionTreeWriter (and the data validating and cleaning class) static (v0.?.1) 
# TODO: Make code so that a program can use the new model immediately after it's been trained without having to stop and let the devs write the code to use the new model (v0.6.1)
# TODO: Add support for regression trees as well, and perhaps tries and n-ary trees instead of just binary trees (v0.7.1)
