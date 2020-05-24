import os
import ToDoList

src = os.path.join(os.path.dirname(ToDoList.__file__), 'data/template.csv')

def get():
    with open(src) as f:
        return f.read().strip()