FILEPATH = "todos.txt" #python console will be added to dir()

def get_todo(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, "w") as file_local2:
        file_local2.writelines(todos_arg)
    
print(help(get_todo)) #checking the func get to-do