#import pgmpy as pg
#from pgmpy import TabularCPD, KJDKjadkjas
#from pgmpy import *
#pg.TabularCPD()

from pgmpy.factors.discrete import TabularCPD 
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

red_bayes=BayesianNetwork([('Lluvia','Mantenimiento'),
                           ('Lluvia','Tren'),('Mantenimiento','Tren'),
                           ('Tren','Reunion')])

dominio_lluvia=['nula','ligera','fuerte']
lluvia_cpd=TabularCPD(variable='Lluvia',
                  variable_card=3,
                  values=[[0.7],[0.2],[0.1]],
                  state_names={'Lluvia':['nula','ligera','fuerte']}
                  )
print(lluvia_cpd )

dominio_mantenimiento=['no','si']
mantenimiento_cpd=TabularCPD(variable='Mantenimiento',
                         variable_card=len(dominio_mantenimiento),
                         values=[[0.6,0.8,0.9],[0.4,0.2,0.1]],
                         evidence=['Lluvia'],
                         evidence_card=[3],
                         state_names={'Mantenimiento':dominio_mantenimiento,
                                      'Lluvia':['nula','ligera','fuerte']},
                         )
print(mantenimiento_cpd)
dominio_tren = ['A tiempo', 'Demorado']


tren_cpd=TabularCPD(variable='Tren',
                    variable_card=len(dominio_tren),
                    values=[[0.9,0.8,0.7,0.6,0.5,0.4],[0.1,0.2,0.3,0.4,0.5,0.6]],
                    evidence=['Lluvia','Mantenimiento'],
                    evidence_card=[3,2],
                    state_names={'Tren':dominio_tren,
                                 'Mantenimiento':dominio_mantenimiento,'Lluvia':dominio_lluvia
                                 }                    )

print(tren_cpd)
dominio_reunion=['Asistir', 'No asistir']
reunion_cpd=TabularCPD(variable='Reunion',
                       variable_card=len(dominio_reunion),
                       values=[[0.9,0.6],[0.1,0.4]],
                       evidence=['Tren'],
                       evidence_card=[2],
                       state_names={'Reunion':dominio_reunion,
                                    'Tren':dominio_tren}
                                    )
print(reunion_cpd)

red_bayes.add_cpds(lluvia_cpd, mantenimiento_cpd, tren_cpd, reunion_cpd)
inferencia=VariableElimination(red_bayes)
consulta_1=inferencia.query(variables=['Reunion'],evidence={'Lluvia':'nula', 'Mantenimiento':'no'})
consulta_2=inferencia.query(variables=['Lluvia'],evidence={'Mantenimiento':'no'})
consulta_3=inferencia.query(variables=['Mantenimiento'],evidence={'Lluvia':'ligera'})
consulta_4=inferencia.query(variables=['Lluvia','Mantenimiento'],evidence={'Reunion':'No asistir'})
print(consulta_1)
print(consulta_2)
print(consulta_3)
print(consulta_4)