number = 23
guess = int(input ('Введите целое число'))

if guess == number:
    print ('''
        Поздравляю вы угадали!''')
    print("хотя не выйграли никакого приза")
elif guess < number:
    print('Нет. Загаданное число немного больше этого')
else:
    print('Нет. Загаданное число немного меньше этого')

print('Завешено!')
