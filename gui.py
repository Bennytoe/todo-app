import functions
import FreeSimpleGUI
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = sg.Window('To-Do App', layout=[[[label], input_box, add_button]]) #obectite po gore
window.read() #display window
print("Hello World")
window.close() #close window when press exit button