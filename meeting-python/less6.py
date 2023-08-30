def main():
    inp_pass = input('Введите пароль: ')
    if len(inp_pass) > 12:
        print('Длинный')
    else:
        print('Короткий')
    if inp_pass.isalpha():
        print('Нет цифр')
    else:
        print('Есть цифры')


if __name__ == '__main__':
    main()
