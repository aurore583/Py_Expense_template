import csv
from PyInquirer import prompt


def choose_spender():
    fichier = open("users.csv") #Ouvre le fichier des user
    user_list = fichier.read() #lis le fichier
    list_spender = user_list.split("\n") #selectionne chaque user sous forme de list
    return list_spender

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender (choose among this list:): ",
        "choices": choose_spender(), 
    },

]

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    fichier = open("expense_report.csv", "a") #ouvrir un fichier pour append dedans
    fichier.write(f'{infos["amount"]}, {infos["label"]}, {infos["spender"]}\n') 
    print("Expense Added !")
    return True




