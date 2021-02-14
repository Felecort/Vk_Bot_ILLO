# Markov chain algorithm
from random import choice, randint


def generate_message(data_dict, chat_id):
    gen_msg = []
    value = choice(list(data_dict[chat_id]["markov_chains"].keys()))
    for j in range(randint(3, 10)):
        if [value] == data_dict[chat_id]["markov_chains"][value]:
            if len(gen_msg) < 2:
                gen_msg.append(value)
            break
        value = choice(data_dict[chat_id]["markov_chains"][value])
        gen_msg.append(value)
    gen_msg = (' '.join(gen_msg)).capitalize() + " "
    return gen_msg


# print(generate_message(data))
