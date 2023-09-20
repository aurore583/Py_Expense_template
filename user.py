from shutil import copy2
from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"What is the name of the new user ? - Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    fichier = open("users.csv", "a") #ouvrir un fichier pour append dedans
    fichier.write(f'{infos["name"]}\n') 
    print("User Added !")
    return True


def save_users(): #sauvegarder les users dans un autre fichier pour la redondance des infos
    copy2("./users.csv", "./user_saved.csv")
    return
