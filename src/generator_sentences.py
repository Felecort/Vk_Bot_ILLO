# Markov chain algorithm
# from pprint import pprint
from random import choice, randint
from pprint import pprint
from time import time
import re

with open("D:/Projects/PythonProjects/Vk_Bot_ILLO/data/test.txt", "r") as file:
    text_source = file.read()
    file.close()

text = re.sub(r"[,.?\n!():—-]", '', text_source).lower().split(" ")
print(text)

test_dict = {}
for i in range(len(text) - 1):
    if text[i] not in test_dict:
        test_dict[text[i]] = [text[i + 1]]
    else:
        test_dict[text[i]].append(text[i + 1])

pprint(test_dict)
out = []
value = choice(list(test_dict.keys()))
for i in range(randint(7, 20)):
    if value not in test_dict:
        break
    value = choice(test_dict[value])
    out.append(value)
# pprint(test_dict)


out = ' '.join(out) + ' '
out = out.capitalize()
print()
print(out)
