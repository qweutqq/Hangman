import random
print('Добро пожаловать в числовую угадайку')
right = int(input('Укажите правую границу загаданного числа:'))
number = random.randint(1, right)
attempts = 0


def is_valid(num):
    if 1 <= num <= right:
         return True
    else:
         return False 

while True:
     n = input(f'Введите число от 1 до {right}: ')
     if is_valid(int(n)):
         if int(n) == number:
             attempts += 1
             print()
             print('Вы угадали!')
             print(f'Количество попыток: {attempts}')
             print('Хотите сыграть еще?')
             print('1 - Да')
             print('2 - Нет')
             answer = input('Введите 1 или 2: ')
             if answer == '1':
                 number = random.randint(1, right)
                 attempts = 0
             else:
                break
         elif int(n) > number:
             print('Меньше')
             attempts += 1
         elif int(n) < number:
             attempts += 1
             print('Больше')
     else:
         print(f'А может быть все-таки введем целое число от 1 до {right}?') 
           
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
       