import PySimpleGUI as Sg

Sg.theme("DarkAmber")

layout = [
    [Sg.Text("Texto na linha 1")],
    [Sg.Text("Entre com um texto na linha 2"), Sg.InputText()],
    [Sg.Button("Ok"), Sg.Button("Cancel")],
]
window = Sg.Window("Bem-Vindo ao PySimpleGUI", layout)

while True:
    event, values = window.read()
    if event == Sg.WIN_CLOSED or event == "Cancel":
        break
    print("Você entrou com:", values[0])

window.close()
