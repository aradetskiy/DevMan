from re import findall

def main():
    inp_pass = input('Введите пароль: ')
    if len(inp_pass) > 12:
        print('Длинный')
    else:
        print('Короткий')
    
   
    if findall(r'[0-9]',inp_pass):
        print('есть цифра')
    else:
        print('Нет цифры')


if __name__ == '__main__':
    main()
