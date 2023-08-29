def main():
    inp_pass = input('Введите пароль: ')
    if len(inp_pass) > 12:
        print('Длинный')
        if inp_pass.isdigit():
            print('Цифра')
        else:
            print('Буква')
    else:
        print('Короткий')
        if inp_pass.isdigit():
            print('Цифра')
        else:
            print('Буква')
    


if __name__ == '__main__':
    main()