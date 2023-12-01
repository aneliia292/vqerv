import os

path = os.getcwd()
print('Место работы: ', path)

if not os.path.isdir('folder'):
    os.mkdir('folder')

else:
    print('уже есть')

os.chdir('folder')
print('Место работы ', os.getcwd())
os.chdir('..')
print('Место работы ', os.getcwd())

os.makedirs('f1/f2/f3/f4')
text_file = open('text.txt', 'a')
text_file.write('My new file')
os.rename('text.txt', 'new.txt')
os.replace('new.txt', 'folder/new.txt')
os.remove('folder/new.txt')
print('my dirs', os.listdir())
listDirs = os.listdir()
for i in listDirs:
    print(i)

for dirpath, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
        print('katalog', os.path.join(dirpath, dirname))
    for filename in filenames:
        print('File', os.path.join(dirpath, filename))

os.remove('f1/')
os.rmdir('f3')
os.removedirs('f2')

os.mkdir('folder/text.txt')
open('text.txt', 'w').write('fghjklkjhgfdfghjkl')
print(os.stat('text.txt').st_size)

with open('text.txt', 'r') as f:
    f.write('asdasd')
    f.read(6)
