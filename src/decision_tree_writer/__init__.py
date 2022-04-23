from decision_tree_writer.TreeWriter import DecisionTreeWriter
# ✓ (v0.4.1): delete the unused root parameter from BaseDecisionTree for cleaner scaffolded code.
# ✓ (v0.4.2): move data validating and cleaning to a separarte class from DecisionTreeWriter and add better validating and cleaning methods
# TODO: Have max_depth and min_node_size as parameters for DecisionTreeWriter.create_tree() and maybe have look_for_correlations by default be False (v0.4.3)

# TODO: Why would you need multiple tree writers? Wouldn't a static class work for multithreading? If so, make DecisionTreeWriter (and the data validating and cleaning class) static (v1.0.x) 
# TODO: Make code so that a program can use the new model immediately after it's been trained without having to stop and let the devs write the code to use the new model (v1.1.x)
# TODO: Add support for regression trees as well, and perhaps tries and n-ary trees instead of just binary trees (v1.2.x)
