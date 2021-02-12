
import json
data_filename = "D:\\Projects\\PythonProjects\\Vk_Bot_ILLO\\data\\database.json"


def get_database():
    with open(data_filename, "r") as file:
        database = json.load(file)
    return database


def set_database(database):
    with open(data_filename, "w") as file:
        json.dump(database, file, indent=4, ensure_ascii=False)


def add_to_dict(new_text, database, chat_id):
    chat_id = str(chat_id)

    new_text = "".join(c for c in new_text if c.isalpha() or c == " " or c.isdigit()).lower().split()

    print(new_text)
    i = 0
    for i in range(len(new_text) - 1):
        if new_text[i] not in database[chat_id]["markov_chains"]:
            database[chat_id]["markov_chains"][new_text[i]] = [new_text[i + 1]]
        else:
            database[chat_id]["markov_chains"][new_text[i]].append(new_text[i + 1])
    database[chat_id]["markov_chains"][new_text[i + 1]] = [new_text[i + 1]]

    set_database(database)
    # print(database)
    return database


# data = get_database()
# data = add_to_dict("😜 привет 🗿😜 я камень!", data, 1)
# set_database(data)
