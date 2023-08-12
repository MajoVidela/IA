import PySimpleGUI as sg

fuente_1=('Monotype Corsiva',20)
menu_principal=[
    [sg.Text('MENU PRINCIPAL',font=fuente_1)],
    [sg.Button('SOY UN BOTON',key='BUTTON_1'),sg.Button('El de al lado es un boton',key='BOTON_2')],
    [sg.Output(size=(60,5))]
]

ventana=sg.Window(title='MI PROGRMA',layout=menu_principal)

while True:
    eventos, valores=ventana.read()
    if eventos==sg.WIN_CLOSED:
        break
    if eventos=='BOTON_1':
        sg.popup('ME APRETASTE',title='MI POPUP')
    if eventos=='BOTON_2':
        print('A MI TAMBIEN...')
    