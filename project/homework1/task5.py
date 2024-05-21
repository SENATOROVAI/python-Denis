while True:
    a = input('ввод "1" - сложение (+)\nввод "2" - вычитание (-)\nввод "3" - умножение (*)\nввод "4" - деление (/)\n')
    if a == "1":
        try:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            print(a + b)
        except ValueError:
            print('ОШИБКА! Допустим ввод только целых чисел!')
    elif a == "2":
        try:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            print(a - b)
        except ValueError:
            print('ОШИБКА! Допустим ввод только целых чисел!')
    elif a == "3":
        try:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            print(a * b)
        except ValueError:
            print('ОШИБКА! Допустим ввод только целых чисел!')
    elif a == "4":
        try:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            print(a / b)
        except ValueError:
            print('ОШИБКА! Допустим ввод только целых чисел!')
        except ZeroDivisionError:
            print('ОШИБКА! Нельзя делить на ноль')
    else:
        print("Недопустимое действие! Попробуйте еще раз")
