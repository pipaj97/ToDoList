"""
A simple ToDo list
"""
import pandas as pd

# TODO:
# BUGFIX:
# - status ändert sich bei finish task
# - index bei finish task = -1

# - docstring ändern
# - remove task
# - unfish task


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


def read_data(data_file):
    df = pd.read_csv(data_file, sep=",")
    return df


"""
Adds a task to the end of the csv file.

Parameters
----------
input file: str

user input: str

Returns
-------
data file: file

"""


def add_task(df):
    new_task = input("Add a new task:\n")
    df_mod = df.append({"status": 0, "task": new_task}, ignore_index=True)
    csv_mod = df_mod.to_csv("../data/template.csv", index=False)
    return csv_mod, output_data(df_mod)



"""
prints the data in the terminal

Parameters
----------
input file: str

Returns
-------
none

"""


def output_data(data):
    data_out = data
    print("Your tasks:\n")
    data_out.loc[(data_out["status"] == 0), ["status"]] = "[ ]"
    data_out.loc[(data_out["status"] == 1), ["status"]] = "[X]"
    # data_out.index = data_out.index + 1
    print(data_out)
    # return data


def finish_task(df):
    # print(df)
    task_to_finish = input("Which task should be finished?: \n")
    task_to_finish = df.iloc[int(task_to_finish) - 1]
    task_to_finish["status"] = 1
    # print(task_to_finish)
    csv_mod = df.to_csv("../data/template.csv", index=False)
    return csv_mod

    # csv_mod = task_to_finish.to_csv("../data/template.csv", index=False)
    # return




def main():
    test = "../data/template.csv"
    # data = read_data(test)
    data = read_data(test)
    test_data = read_data(test)
    # print(data)
    output_data(data)
    # add_task(test_data)
    finish_task(data)


if __name__ == "__main__":
    main()
