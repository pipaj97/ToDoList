"""
A simple ToDo list
"""

# TODO:
# - read txt
# - write txt
# - add a task
# - finish task and remove


def read_data(data_file):
    with open(data_file) as f:
        data = f.read()
        print(f"Your current tasks: \n{data}")
    return data

def add_task(data_file):
    with open(data_file, 'a') as f:
        new_task = input("Add a new task: \n")
        new_task_to_append = f"\n- [ ] {new_task}"
        f.write(new_task_to_append)

def main():
    test = "../data/template.txt"
    read_data(test)
    add_task(test)
    read_data(test)

if __name__ == "__main__":
    main()