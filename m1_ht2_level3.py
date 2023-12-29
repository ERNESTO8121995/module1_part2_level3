password = input('Введите пароль: ')
index = 0
while index != 1:
    count_lower = 0 #счетчик наличия строчных букв
    count_upper = 0 #счетчик наличия заглавных букв
    for i in range(len(password)):
        if password[i].islower() == 1:
            count_lower += 1
        elif password[i].isupper() == 1:
            count_upper += 1
    if len(password) >= 8 and count_lower >= 1 and count_upper >= 1:
        print('Допустимый пароль.')
        index += 1
    else:
        password = input('Вы ввели недопустимый пароль.\nДопустимым считается пароль состоящий более чем из 8 символов и включает как прописные так и заглавные буквы.\nВведите новый пароль: ')