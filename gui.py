import functions
import FreeSimpleGUI as sg



label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window('To-Do App',
                   layout=[[[label], input_box, add_button]], #the objects
                   font=('Helvetica', 12)) #font & size
while True:
    event, values = window.read() #display window
    print(values)
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close() #close window when press exit button