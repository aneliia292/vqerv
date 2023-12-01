import os


def read_end(lines, file):
    with open(file, 'r') as f:
        ls = f.readlines()
    for i in range(len(ls) - lines, len(ls)):
        print(ls[i], end='')


read_end(2, 'article.txt')

def print_reps(directory):
    for path, dirs, files in os.walk(directory):
        for dir in dirs:
            print(os.path.join(path, dir))
        for file in files:
            print(os.path.join(path, file))


os.chdir('../venv')
directory = os.getcwd()
print(directory)