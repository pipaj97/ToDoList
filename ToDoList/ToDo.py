"""
A simple ToDo list
"""

# TODO:
# - read csv
# - write task
# - add a task
# - finish task and remove
# - print tasks


"""
Function for parsing the input file

Parameters
----------
input file: str

Returns
-------
dict
    ``task`` (str): name of the tasks
    ``status`` (int): status if the task is finished or not

"""

# TODO dict richtig zurückgeben
def read_data(data_file):
    with open(data_file) as f:
        f.readline()
        data = {}
        for line in f:

            (data["status"], data["task"]) = line.split(";")
            # print(f"Your current tasks: \n{input_data}")
        print(data)
        # return data


def add_task(data_file):
    with open(data_file, "a") as f:
        new_task = input("Add a new task: \n")
        new_task_to_append = f"\n[ ] {new_task}"
        f.write(new_task_to_append)


def main():
    test = "../data/template.csv"
    read_data(test)
    # add_task(test)
    # read_data(test)


if __name__ == "__main__":
    main()
