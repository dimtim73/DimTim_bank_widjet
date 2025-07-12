import re

def clear_names(file_name):
    """ функция возвращает очищенный список имен"""
    new_names_list = list()

    with open("src/names.txt", "r", encoding='utf-8') as names_file:
        names_list = names_file.read().split()

        for name_item in names_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)



    return new_names_list


def has_cyrillic(name_list):
    cyr_names =[]
    for cleared_name in cleared_names:
        if  bool(re.search('[а-яА-Я]', cleared_name)):
            cyr_names.append(cleared_name)

    cyr_names.sort()

    return cyr_names

def has_english(name_list):
    eng_names =[]
    for cleared_name in cleared_names:
        if  bool(re.search('[a-zA-Z]', cleared_name)):
            eng_names.append(cleared_name)

    eng_names.sort()

    return eng_names






cleared_names = clear_names('names.txt')

cyr_names_list = has_cyrillic(cleared_names)

with open("src/rus_names.txt", "w", encoding='utf-8') as names_file:
    names_file.write(str(cyr_names_list))


eng_names_list = has_english(cleared_names)


with open("src/eng_names.txt", "w", encoding='utf-8') as names_file:
    names_file.write(str(eng_names_list))

for name in cyr_names_list:
    print(name)

print()

for name in eng_names_list:
    print(name)
