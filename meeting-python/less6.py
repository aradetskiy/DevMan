from re import findall

def has_symbol(password):
    if not password.isalnum():
        return True
    else:
        return False
    
def has_digit(password):
    if findall(r'\d', password):
        return True
    else:
        return False


def has_letters(password):
    if findall(r'[a-zA-ZА-Яа-яёЁ]', password):
        return True
    else:
        return False


def has_upper_letters(password):
    if findall(r'[A-ZА-ЯЁ]', password):
        return True
    else:
        return False


def has_lower_letters(password):
    if findall(r'[a-zа-яё]', password):
        return True
    else:
        return False


def is_very_long(password):
    if len(password) > 12:
        return True
    else:
        return False



def main():
    inp_pass = input('Введите пароль: ')

    check_functions = [is_very_long,has_lower_letters,has_upper_letters,has_letters,has_digit,has_symbol]
    rate_pass = 0
    for funct in check_functions:
        rate_pass += funct(inp_pass)*2
    
    print(f'Рейтинг пароля - {rate_pass}')


if __name__ == '__main__':
    main()
