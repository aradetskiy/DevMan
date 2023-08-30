def main():
    inp_pass = input('Введите пароль: ')
    if len(inp_pass) > 12:
        print('Длинный')
        for pass_letter in inp_pass:
            if pass_letter.isdigit():
                print(f'{pass_letter} - Цифра')
            else:
                print(f'{pass_letter} - Буквава')
    else:
        print('Короткий')
       
    


if __name__ == '__main__':
    main()