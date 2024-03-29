FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a text file and returns list of to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do list items in the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


"""
This will be executed only when this function is executed and not when it is imported
"""
if __name__ == "__main__":
    print("Hello")
