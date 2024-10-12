FILE_PATH = 'todos.txt'

def get_todos(filePath=FILE_PATH) -> list[str]:
    """ Reads todo list from the file. Returns todo list """
    with open(filePath, "r") as file:
        todo_list = file.readlines()
    return [todo_el.strip('\n') for todo_el in todo_list] # remove linebreaks from todos


def write_todos(todo_list: list[str], filePath=FILE_PATH):
    """ Saves todo list passed in todo_list parameter to the file """
    with open(filePath, 'w') as file:
        file.writelines([f"{todo_el}\n" for todo_el in todo_list])

# Printed only when THIS file is run; does not run when it is imported
if __name__ == "__main__":
    print("Hello from functions!")