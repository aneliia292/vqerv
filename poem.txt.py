import os


def longest_words(file):
    with open(file) as f:
        maximum = 0
        list = []
        ls = f.readlines()
    for i in ls:
        if len(i) > maximum:
            maximum = len(i)
            list.append(i)

        elif maximum == i:
            list.append(i)

        if len(i) == maximum:
            list.append(i)
    print(list)


longest_words('poem.txt')