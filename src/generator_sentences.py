
# Markov chain algorithm
from random import choice, randint
import re


def add_dict(new_text, data_dict):
    new_text = re.sub(r"[.,?\n!():—-]", '', new_text).lower().split(" ")
    i = 0
    for i in range(len(new_text) - 1):
        if new_text[i] not in data_dict:
            data_dict[new_text[i]] = [new_text[i + 1]]
        else:
            data_dict[new_text[i]].append(new_text[i + 1])
    data_dict[new_text[i + 1]] = [new_text[i + 1]]
    return data_dict


def generate_message(data_dict):
    gen_msg = []
    value = choice(list(data_dict.keys()))
    for j in range(randint(5, 20)):
        if [value] == data_dict[value]:
            break
        value = choice(data_dict[value])
        gen_msg.append(value)
    gen_msg = (' '.join(gen_msg)).capitalize()
    return gen_msg
