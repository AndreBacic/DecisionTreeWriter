from decision_tree_writer.TreeWriter import DecisionTreeWriter
# TODO: move data validating and cleaning to a separarte class from DecisionTreeWriter and add better validating and cleaning methods (v0.3.2)
# TODO: Why would you need multiple tree writers? Wouldn't a static class work for multithreading? If so, make DecisionTreeWriter (and the data validating and cleaning class) static (v1.x.x) 
# TODO: Make code so that a program can use the new model immediately after it's been trained without having to stop and let the devs write the code to use the new model (v2.x.x)
