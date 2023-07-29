from logic import *

ACaballero=Symbol("A es Caballero")
ALadron=Symbol("A es Ladrón")
BCaballero=Symbol("B es Caballero")
BLadron=Symbol("B es Ladrón")
CCaballero=Symbol("C es Caballero")
CLadron=Symbol("C es Ladrón")

ListaPersonajes=[ACaballero,ALadron,BCaballero,BLadron,CCaballero,CLadron]
#Esenario 1
knowledge = And(
    Or(ACaballero, ALadron),
    Not(And(ACaballero, ALadron)),
    Implication(ACaballero, And(ACaballero, ALadron)),
    Implication(ALadron, Not(And(ACaballero, ALadron))),
)

for personajes in ListaPersonajes:
        if model_check(knowledge, personajes):
            print(personajes)
print("-------------------")
#Esenario 2
knowledge2 = And(
    Or(ACaballero, ALadron),
    Not(And(ACaballero, ALadron)),
    Or(BCaballero, BLadron),
    Not(And(BCaballero, BLadron)),
    Implication(ACaballero, And(ALadron, BLadron)),
    Implication(ALadron, Not(And(ALadron, BLadron)) )

)
for personajes in ListaPersonajes:
        if model_check(knowledge2, personajes):
            print(personajes)
