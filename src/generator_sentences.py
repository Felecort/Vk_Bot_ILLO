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

test_dict = {}
i = 0
for i in range(len(text) - 1):
    # print(text[i])
    if text[i] not in test_dict:
        test_dict[text[i]] = [text[i + 1]]
    else:
        test_dict[text[i]].append(text[i + 1])
test_dict[text[i + 1]] = [text[i + 1]]

out = []
value = choice(list(test_dict.keys()))
for i in range(randint(50, 70)):
    if [value] == test_dict[value]:
        break
    value = choice(test_dict[value])
    out.append(value)


out = ' '.join(out) + ' '
out = out.capitalize()
print(out)
