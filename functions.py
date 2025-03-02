FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_args)
