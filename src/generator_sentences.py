
# Markov chain algorithm
from random import choice, randint


def generate_message(data_dict, chat_id):
    gen_msg = []
    value = choice(list(data_dict[chat_id]["markov_chains"].keys()))
    for i in range(randint(3, 20)):
        if value not in data_dict[chat_id]["markov_chains"]:
            break
        new_text = choice(data_dict[chat_id]["markov_chains"][value])
        value = new_text[1]
        gen_msg.append(new_text[0])
        gen_msg.append(new_text[1])
    return (' '.join(gen_msg)).capitalize() + " "


# print(generate_message(get_database(), "1"))
