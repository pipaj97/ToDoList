# -*- coding: utf-8 -*-
"""
simple cli for the ToDo list
"""

from PyInquirer import style_from_dict, prompt
from examples import custom_style_2, custom_style_1
from ToDo import ToDo
import pandas as pd

# TODO:
# manchmal bricht es einfach ab?
# docstrings hinzufügen und in TODO.py ändern
# windows support
# setup.py
# datafile in __init__ ändern


def ask_operation(liste):
    if liste.df.empty:
        operation_prompt = {
        'type': 'list',
        'name': 'operation',
        'message': 'What do you want to do?',
        'choices': ['add task', 'exit']
    }
    else:
        operation_prompt = {
        'type': 'list',
        'name': 'operation',
        'message': 'What do you want to do?',
        'choices': ['add task', 'finish task', 'unfinish task', 'remove task', 'exit']
        }
    answers = prompt(operation_prompt, style=custom_style_2)
    return answers['operation']

def ask_task(series):
    tasks = [
    {
        'type': 'list', # raw list geht nur bis 9 --> zu list gewechselt
        'name': 'tasks',
        'message': 'Choose a task!',
        'choices': series
    }
    ]
    tasks = prompt(tasks, style=custom_style_2)
    return tasks["tasks"]

def ask_permission():
    questions = {
        'type': 'confirm',
        'message': 'Do you really want to remove that task?',
        'name': 'continue',
        'default': True
    }
    answers = prompt(questions, style=custom_style_1)
    return answers




def parse_answer(liste):
    operation = ask_operation(liste)
    switch_case = {
        'add task' : c_add_task,
        'finish task' : c_finish_task,
        'unfinish task' : c_unfinished_task,
        'remove task' : c_remove_task,
        'exit' : c_exit
    }

    func = switch_case.get(operation)
    func(liste)


def c_exit(liste):
    return liste.exit()

def c_add_task(liste):
    liste.add_task()
    liste.df = pd.read_csv(liste.data_file, sep=",")
    return parse_answer(liste)

def c_finish_task(liste):
    relevant_tasks = liste.df.loc[(liste.df["STATUS"] == 0)]
    series = relevant_tasks["TASK"].tolist()
    if len(series) == 0:
        print("No unfinished tasks available!\n")
        return parse_answer(liste)
    else:
        chosen_task = ask_task(series)
        liste.finish_task(chosen_task)
        return parse_answer(liste)

def c_unfinished_task(liste):
    relevant_tasks = liste.df.loc[(liste.df["STATUS"] == 1)]
    series = relevant_tasks["TASK"].tolist()
    if len(series) == 0:
        print("No finished tasks available!\n")
        return parse_answer(liste)
    else:
        chosen_task = ask_task(series)
        liste.unfinish_task(chosen_task)
        return parse_answer(liste)

def c_remove_task(liste):
    series = liste.df["TASK"].tolist()
    chosen_task = ask_task(series)
    row = liste.df.loc[(liste.df["TASK"] == chosen_task)]
    status = row["STATUS"].values
    if (status[0] == 0):
        permission = ask_permission()
        if permission["continue"] == True:
            liste.remove_task(chosen_task)
            liste.df = pd.read_csv(liste.data_file, sep=",")
            return parse_answer(liste)
        else:
            liste.output_data(liste.df)
            return parse_answer(liste)
    else:
        liste.remove_task(chosen_task)
        liste.df = pd.read_csv(liste.data_file, sep=",")
        return parse_answer(liste)


def main():
    liste = ToDo()
    parse_answer(liste)


if __name__ == '__main__':
    main()