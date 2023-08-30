from re import findall


def has_digit(password):
    if findall(r'[0-9]',password):
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
    print(is_very_long(inp_pass))
    print(has_digit(inp_pass))

    
    


if __name__ == '__main__':
    main()
