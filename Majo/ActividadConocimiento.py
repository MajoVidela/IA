from logic import *

ACaballero=Symbol("A es Caballero")
ALadron=Symbol("A es Ladrón")
BCaballero=Symbol("B es Caballero")
BLadron=Symbol("B es Ladrón")
CCaballero=Symbol("C es Caballero")
CLadrón=Symbol("C es Ladrón")

#Esenario 1
knowledge = And(
    Implication(Not ACaballero, ALadron),
    Or()