from logic import *

ACaballero=Symbol("A es Caballero")
ALadron=Symbol("A es Ladrón")
BCaballero=Symbol("B es Caballero")
BLadron=Symbol("B es Ladrón")
CCaballero=Symbol("C es Caballero")
CLadron=Symbol("C es Ladrón")

ListaPersonajes=[ACaballero,ALadron,BCaballero,BLadron,CCaballero,CLadron]

def solucion(_esenario, _ListaPersonajes):
   for personajes in _ListaPersonajes:
        if model_check(_esenario, personajes):
            #ListaPersonajes_verdaderos.append(ListaPersonajes)
            print(personajes)   
#Esenario 1
#A dice: “Soy un caballero y un ladrón”
print("Esenario 1")

knowledge = And(
    Or(ACaballero, ALadron),
    Not(And(ACaballero, ALadron)),
    Implication(ACaballero, And(ACaballero, ALadron)),
    Implication(ALadron, Not(And(ACaballero, ALadron))),
)
solucion(knowledge, ListaPersonajes)
print("-------------------")

print("Esenario 2")

#Esenario 2
#A:Somos ambos ladrones
#B no dice nada
knowledge2 = And(
    Or(ACaballero, ALadron),
    Not(And(ACaballero, ALadron)),
    Or(BCaballero, BLadron),
    Not(And(BCaballero, BLadron)),
    Implication(ACaballero, And(ALadron, BLadron)),
    Implication(ALadron, Not(And(ALadron, BLadron)) )

)
solucion(knowledge2, ListaPersonajes)
print("-------------------")

print("Esenario 3")

#Esenario 3
#A dice: “Somos del mismo tipo”
#B dice: “Somos de distintos tipos”   
knowledge3 = And(
    Or(ACaballero, ALadron),
    Not(And(ACaballero, ALadron)),
    Or(BCaballero, BLadron),
    Not(And(BCaballero, BLadron)),
    Implication(ACaballero, Or(And(ACaballero, BCaballero),And(ALadron, BLadron))),
    Implication(ALadron, Not(Or(And(ACaballero, BCaballero),And(ALadron, BLadron)))),

    Implication(BCaballero, Or(And(ACaballero, BLadron),And(ALadron,BCaballero))),
    Implication(BLadron, Not(Or(And(ACaballero, BLadron),And(ALadron,BCaballero)))),
)
solucion(knowledge3, ListaPersonajes)
print("-------------------")

print("Esenario 4")

#Esenario 4
#A dice: “Soy un caballero” o “Soy un ladrón” (pero no sabemos cuál frase dijo)
#B dice: “A dijo ‘Soy un ladrón’”
#B luego dice: “C es un ladrón”
#C dice “A es un caballero”
knowledge4 = And(
    Or(ACaballero, ALadron),
    Not(And(ACaballero, ALadron)),
    Or(BCaballero, BLadron),
    Not(And(BCaballero, BLadron)),
    Or(CCaballero, CLadron),
    Not(And(CCaballero, CLadron)),

    Implication(ACaballero, Or(ACaballero, ALadron)),
    Implication(ALadron, Not(Or(ACaballero, ALadron))),

    Implication(BCaballero, And(ALadron, CLadron)),
    Implication(BLadron, Not(And(ALadron, CLadron))),

    Implication(CCaballero, ACaballero),
    Implication(CLadron, Not(ACaballero)),
)
solucion(knowledge4, ListaPersonajes)