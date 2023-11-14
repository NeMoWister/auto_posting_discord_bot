import random
import os
import config


def start_posting():
    choice = random.choices(config.my_list, weights=[item[2] for item in config.my_list], k=1)[0]
    print(choice)
    files = os.listdir(choice[1])
    out = []
    while len(out) != 10:
        file = choice[1] + '/' + random.choice(files)
        if file not in out and os.path.isfile(file):
            out.append(file)
    print(out)
    return [choice[0], out]


