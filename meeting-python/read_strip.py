from codecs import open
from time import sleep


file = open('meeting-python\src\letters_mapping.txt', 'r', 'utf-8')
letters_mapping = file.readlines()
my_dict = {}
for line in letters_mapping:
    line = line.split(',')
    for letter in line:
        if letter != '\r\n':
            key = letter.split(': ')[0]
            value = letter.split(': ')[1]
            print(key,'       ',value)
            my_dict[key] = value
            sleep(1)

   
print(my_dict)