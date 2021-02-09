
# Markov chain algorithm
from pprint import pprint
from random import choice
from random import randint
from time import time


start = time()
with open("../data/data.txt", "r") as file:
    text = file.read()
    file.close()
text = text.lower()
text = text.replace("\n", "")
text = text.replace(".", "")
text = text.split(" ")

test_dict = {}
for i in range(len(text) - 1):
    if text[i] not in test_dict:
        test_dict[text[i]] = [text[i+1]]
    else:
        test_dict[text[i]].append(text[i + 1])
print(time() - start)

out = []
value = "в"
for i in range(randint(5, 30)):
    value = choice(test_dict[value])
    out.append(value)


out = ' '.join(out)
out = out.capitalize()
print(out)
print(test_dict.__sizeof__())
