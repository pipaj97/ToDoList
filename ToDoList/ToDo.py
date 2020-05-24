"""
A simple ToDo list
"""
import pandas as pd
from pathlib import Path

class ToDo:
    """
    Driver class for the functionality of the ToDo list.
    """
    def __init__(self):
    
        self.data_file = self.get_path()
        self.df = pd.read_csv(self.data_file, sep=",")
        self.output_data(self.df)


    def get_path(self):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/template.csv").resolve()
        return file_path

    def output_data(self, df):
        """
        Prints the DataFrame in the terminal.

        Parameters
        ----------
        input file: DataFrame

        Returns
        -------
        None
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
        None

        Returns
        -------
        If no user input is given:
            self.output_data(self.df): func
                Function to display the updated DataFrame.
        
        Else:
            csv_mod: CSV
                Updated CSV file.
            self.output_data(df_mod): func
                Function to display the updated DataFrame.
        """
        new_task = input("Add a new task:\n")
        if new_task == "":
            print("Wrong input!")
            return self.output_data(self.df)
        else:
            df_mod = self.df.append({"STATUS": 0, "TASK": new_task}, ignore_index=True)
            csv_mod = df_mod.to_csv(self.data_file, index=False)
            return csv_mod, self.output_data(df_mod)


    def finish_task(self, chosen_task):
        """
        Labels a task as finished.

        Parameters
        ----------
        chosen_task: dict of {str: str}
            The chosen task which will be labelled as finished.

        Returns
        -------
        csv_mod: CSV
            Updated CSV file.
        self.output_data(df_TTF): func
            Function to display the updated DataFrame.
        """
        df_TTF = self.df
        df_TTF.loc[df_TTF["TASK"] == chosen_task, ["STATUS"]] = 1
        csv_mod = df_TTF.to_csv(self.data_file, index=False)
        return csv_mod, self.output_data(df_TTF)


    def unfinish_task(self, chosen_task):
        """
        Labels a task as unfinished.

        Parameters
        ----------
        chosen_task: dict of {str: str}
            The chosen task which will be labelled as unfinished.

        Returns
        -------
        csv_mod: CSV
            Updated CSV file.
        self.output_data(df_TTU): func
            Function to display the updated DataFrame.
        """
        df_TTU = self.df
        df_TTU.loc[df_TTU["TASK"] == chosen_task, ["STATUS"]] = 0
        csv_mod = df_TTU.to_csv(self.data_file, index=False)
        return csv_mod, self.output_data(df_TTU)


    def remove_task(self, chosen_task):
        """
        Removes a task from the ToDo list.

        Parameters
        ----------
        chosen_task: dict of {str: str}
            The chosen task which will be removed.

        Returns
        -------
        csv_mod: CSV
            Updated CSV file.
        self.output_data(new_df_TTR): func
            Function to display the updated DataFrame.
        """
        df_TTR = self.df
        df_TTR = df_TTR.drop(df_TTR[df_TTR["TASK"] == chosen_task].index)
        new_df_TTR = df_TTR.reset_index(drop=True)
        csv_mod = new_df_TTR.to_csv(self.data_file, index=False)
        return csv_mod, self.output_data(new_df_TTR)