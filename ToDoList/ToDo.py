"""
A simple ToDo list
"""
import pandas as pd

class ToDo:
    """
    Driver class for the functionality of the ToDo list.
    """
    def __init__(self):
        self.data_file = "/home/julian/PythonProjects/MyProjects/ToDoList/data/template.csv"
        self.df = pd.read_csv(self.data_file, sep=",")
        print(self.greeting())
        self.output_data(self.df)

    def greeting(self):
        return r"""
 ______        ____            __                    __
/\__  _\      /\  _`\         /\ \       __         /\ \__
\/_/\ \/   ___\ \ \/\ \    ___\ \ \     /\_\    ____\ \ ,_\
   \ \ \  / __`\ \ \ \ \  / __`\ \ \  __\/\ \  /',__\\ \ \/
    \ \ \/\ \L\ \ \ \_\ \/\ \L\ \ \ \L\ \\ \ \/\__, `\\ \ \_
     \ \_\ \____/\ \____/\ \____/\ \____/ \ \_\/\____/ \ \__\
      \/_/\/___/  \/___/  \/___/  \/___/   \/_/\/___/   \/__/

    Brought to you by @pipaj97 and @hugo_weizenkeim
    """


    def output_data(self, df):
        """
        Prints the data in the terminal.

        Parameters
        ----------
        input file: str

        Returns
        -------
        none
        """
        data_out = df.copy()
        if data_out.empty:
            print("There are no tasks.\n")
        else:
            print("Your tasks:\n")
            data_out.loc[(data_out["STATUS"] == 0), ["STATUS"]] = "[ ]"
            data_out.loc[(data_out["STATUS"] == 1), ["STATUS"]] = "[X]"
            data_out.index = data_out.index + 1
            print(data_out)
        return None


    def add_task(self):
        """
        Adds a task to the end of the csv file.

        Parameters
        ----------
        input file: DataFrame

        user input: str

        Returns
        -------
        data file: DataFrame
        """
        new_task = input("Add a new task:\n")
        if new_task == "":
            print("Wrong input!")
            return self.output_data(self.df)
        else:
            df_mod = self.df.append({"STATUS": 0, "TASK": new_task}, ignore_index=True)
            csv_mod = df_mod.to_csv("/home/julian/PythonProjects/MyProjects/ToDoList/data/template.csv", index=False)
            return csv_mod, self.output_data(df_mod)


    def finish_task(self, chosen_task):
        """
        Labels a task as finished.

        Parameters
        ----------
        input file: DataFrame

        user input: str

        Returns
        -------
        data file: DataFrame
        """
        df_TTF = self.df
        task_to_finish = chosen_task
        df_TTF.loc[df_TTF["TASK"] == chosen_task, ["STATUS"]] = 1
        csv_mod = df_TTF.to_csv("/home/julian/PythonProjects/MyProjects/ToDoList/data/template.csv", index=False)
        return csv_mod, self.output_data(df_TTF)


    def unfinish_task(self, chosen_task):
        """
        Relabels a finished task as unfinished.

        Parameters
        ----------
        input file: DataFrame

        user input: str

        Returns
        -------
        data file: DataFrame
        """
        df_TTU = self.df
        task_to_finish = chosen_task
        df_TTU.loc[df_TTU["TASK"] == chosen_task, ["STATUS"]] = 0
        csv_mod = df_TTU.to_csv("/home/julian/PythonProjects/MyProjects/ToDoList/data/template.csv", index=False)
        return csv_mod, self.output_data(df_TTU)


    def remove_task(self, chosen_task):
        """
        Removes a task from the ToDo list.

        Parameters
        ----------
        input file: DataFrame

        user input: str

        Returns
        -------
        data file: DataFrame
        """
        df_TTR = self.df
        task_to_remove = chosen_task
        df_TTR = df_TTR.drop(df_TTR[df_TTR["TASK"] == chosen_task].index)
        new_df_TTR = df_TTR.reset_index(drop=True)
        csv_mod = new_df_TTR.to_csv("/home/julian/PythonProjects/MyProjects/ToDoList/data/template.csv", index=False)
        return csv_mod, self.output_data(new_df_TTR)


    def exit(self):
        """
        Enables not to change the ToDo list.

        Parameters
        ----------
        input file: DataFrame

        Returns
        -------
        data file: str
        """
        return print(
        r"""
༼ つ ◕_◕ ༽つ  Don't leave me alone! ༼ つ ◕_◕ ༽つ
        """
        )
