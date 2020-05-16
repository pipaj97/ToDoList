"""
A simple ToDo list
"""
import pandas as pd

# TODO:
# - docstring ändern


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
    df_mod = df.append({"STATUS": 0, "TASK": new_task}, ignore_index=True)
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
    data_out = data.copy()
    print("Your tasks:\n")
    data_out.loc[(data_out["STATUS"] == 0), ["STATUS"]] = "[ ]"
    data_out.loc[(data_out["STATUS"] == 1), ["STATUS"]] = "[X]"
    data_out.index = data_out.index + 1
    print(data_out)
    return None


def finish_task(df):
    df_TTF = df
    task_to_finish = input("Which task should be finished?: \n")
    df_TTF.loc[[int(task_to_finish) - 1], ["STATUS"]] = 1
    csv_mod = df_TTF.to_csv("../data/template.csv", index=False)
    return csv_mod, output_data(df_TTF)


def unfinish_task(df):
    df_TTF = df
    task_to_finish = input("Which task should be unfinished?: \n")
    df_TTF.loc[[int(task_to_finish) - 1], ["STATUS"]] = 0
    csv_mod = df_TTF.to_csv("../data/template.csv", index=False)
    return csv_mod, output_data(df_TTF)


def remove_task(df):
    df_TTF = df
    task_to_remove = input("Which task should be removed?: \n")
    df_TTF = df_TTF.drop(df_TTF.index[int(task_to_remove) - 1])
    df_TTF = df_TTF.reset_index(drop=True)
    csv_mod = df_TTF.to_csv("../data/template.csv", index=False)
    return csv_mod, output_data(df_TTF)


def do_nothing(df):
    return print(
        r"""
    ༼ つ ◕_◕ ༽つ  Don't leave me alone! ༼ つ ◕_◕ ༽つ
    """
    )


def greeting():
    return r"""
 ______        ____            __                    __
/\__  _\      /\  _`\         /\ \       __         /\ \__
\/_/\ \/   ___\ \ \/\ \    ___\ \ \     /\_\    ____\ \ ,_\
   \ \ \  / __`\ \ \ \ \  / __`\ \ \  __\/\ \  /',__\\ \ \/
    \ \ \/\ \L\ \ \ \_\ \/\ \L\ \ \ \L\ \\ \ \/\__, `\\ \ \_
     \ \_\ \____/\ \____/\ \____/\ \____/ \ \_\/\____/ \ \__\
      \/_/\/___/  \/___/  \/___/  \/___/   \/_/\/___/   \/__/

Brought to you by @hugo_weizenkeim and @pipaj97
"""


def parse_cli(operation, data):
    functions = {
        "nothing": do_nothing,
        "add task": add_task,
        "finish task": finish_task,
        "unfinish task": unfinish_task,
        "remove task": remove_task,
    }
    if operation in functions:
        return functions[operation](data)
    else:
        print("Wrong input! Try one these:\n")
        for key, value in functions.items():
            print(key)


def main():
    data_file = "../data/template.csv"
    df = pd.read_csv(data_file, sep=",")
    print(greeting())
    output_data(df)
    operation = (input("What do you want to do?\n")).lower()
    parse_cli(operation, df)


if __name__ == "__main__":
    main()
