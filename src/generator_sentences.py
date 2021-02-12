
# Markov chain algorithm
from random import choice, randint


def generate_message(data_dict):
    gen_msg = []
    value = choice(list(data_dict.keys()))
    print(value)
    for j in range(randint(5, 20)):
        if [value] == data_dict[value] and len(gen_msg) < 2:
            gen_msg.append(value)
            break
        value = choice(data_dict[value])
        gen_msg.append(value)
    gen_msg = (' '.join(gen_msg)).capitalize() + " "
    return gen_msg
