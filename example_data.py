from dataclasses import dataclass
@dataclass
class Dinosaur:
    order: str
    species: str
    length: float
    height: float
    is_herbivore: bool
    is_bipedal: bool
    age: int

dinosaurs = [
    Dinosaur()
]