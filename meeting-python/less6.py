from re import findall


def has_digit(password):
    if findall(r'\d', password):
        return True
    else:
        return False


def is_very_long(password):
    if len(password) > 12:
        return True
    else:
        return False


def coint_score(password):
    count = (has_digit(password) + is_very_long(password))*2
    return count


def main():
    inp_pass = input('Введите пароль: ')

    score = coint_score(inp_pass)
    print(f'Рейтинг пароля - {score}')


if __name__ == '__main__':
    main()
