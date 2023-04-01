import function
import PySimpleGUI as sg

label = sg.Text("Type in a todo: ")
input_box = sg.InputText(tooltip="Enter todo:", key="todo")
add_button = sg.Button("Add")


window = sg.Window("Pro's Todo App",
                   layout=[[label, input_box, add_button]],
                   font=('Monaco', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()
