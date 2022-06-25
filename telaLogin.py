import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

window = sg.Window('Login',layout=layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        usuario_correto = 'Gustavo'
        senha_correta = '123456'
        usuario = value['usuario']
        senha = value['senha']
        if usuario == usuario_correto and senha == senha_correta:
            window['mensagem'].update('Login realizado com sucesso')
        else:
            window['mensagem'].update('Falha ao logar')
