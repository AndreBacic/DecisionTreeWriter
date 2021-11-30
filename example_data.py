from dataclasses import dataclass
@dataclass
class Iris:
    species: str
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

irises = [
    Iris('setosa', 5.2, 3.5, 1.5, 0.2),
    Iris('setosa', 5.2, 4.1, 1.5, 0.1),
    Iris('setosa', 5.4, 3.7, 1.5, 0.2),
    Iris('versicolor', 6.2, 2.2, 4.5, 1.5),
    Iris('versicolor', 5.7, 2.9, 4.2, 1.3),
    Iris('versicolor', 5.6, 2.9, 3.6, 1.3),
    Iris('virginica', 7.2, 3.2, 6.0, 1.8),
    Iris('virginica', 6.1, 2.6, 5.6, 1.4),
    Iris('virginica', 6.8, 3.0, 5.5, 2.1)
]

