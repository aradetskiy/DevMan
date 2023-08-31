import re
def main():
    test_fraze = input('Введите текст для обработки: ')
    test_pattern = '\d'
    result = re.finditer(test_pattern,test_fraze)
    print (result)

if __name__ == '__main__':
    main()