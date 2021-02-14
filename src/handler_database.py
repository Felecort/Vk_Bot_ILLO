
import json
data_filename = "D:\\Projects\\PythonProjects\\Vk_Bot_ILLO\\data\\database.json"
log_error_name = "D:\\Projects\\PythonProjects\\Vk_Bot_ILLO\\data\\error.log"
# data_filename = "./data/database.json"    # hosting
# log_error_name = "./data/error.log"       # hosting


def get_database():
    with open(data_filename, "r") as file:
        database = json.load(file)
    return database


def set_database(database):
    with open(data_filename, "w") as file:
        json.dump(database, file, ensure_ascii=False, indent=4)


def add_to_dict(new_text, database, chat_id):

    # new_text = "".join(c for c in new_text if c.isalpha() or c == " " or c.isdigit()).lower().split()
    print(new_text)
    for i in range(len(new_text) - 2):
        if new_text[i] not in database[chat_id]["markov_chains"]:
            database[chat_id]["markov_chains"][new_text[i]] = [[new_text[i + 1], new_text[i + 2]]]
        else:
            database[chat_id]["markov_chains"][new_text[i]].append([new_text[i + 1], new_text[i + 2]])
    return database


# rand = str(list(randint(10, 20) for x in range(15)))
# rand = [1, 2, 3, 4, 5, 6, 7, 4]
# print(rand)
# data = get_database()
# set_database(data)
# data = add_to_dict(rand, data, "1")
# set_database(data)
