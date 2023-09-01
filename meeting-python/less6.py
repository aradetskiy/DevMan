from re import findall
from msvcrt import getwch



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


def input_pass():
    print('Введите пароль: ', end='',flush=True)
    password = []
    while 1:
        current_char = getwch()
        if current_char != '\r':
            if current_char == '\x08':  # разобраться с отображением затирания  символов пароля
                if password:
                    #print('\u001b[1D')
                    
                    password = password[:-1] 
            else:
                password.append(str(current_char))
                print('*', end='',flush= True)
        else:
            print('',end='\n')
            break
    password = ''.join(password)
    return password


def main():

    inp_pass = input_pass()
    check_functions = [is_very_long, has_lower_letters,
                       has_upper_letters, has_letters, has_digit, has_symbol]
    rate_pass = 0
    for funct in check_functions:
        rate_pass += funct(inp_pass)*2

    print(f'Рейтинг пароля - {rate_pass}')


if __name__ == '__main__':
    main()
