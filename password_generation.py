import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
puncuations = '!#$%&*+-=?@^_.' 
exceptions = 'il1Lo0O'
chars = ''
password = ''

password_quantity = int(input('Укажите количество паролей для генерации:'))
password_lenth = int(input('Укажите длину одного пароля:'))
digitsOn = input('Включать ли цифры 0123456789? (y/n)')
ABCOn = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if digitsOn == 'y':
    chars += digits
if abcOn == 'y':
    chars += uppercase_letters
if abcOn == 'y':
    chars += lowercase_letters
if chOn == 'y':
    chars += puncuations
if excOn == 'y':
    chars = ''.join([c for c in chars if c not in exceptions])    

def generate_password(chars, password_lenth):
    return ''.join(random.choice(chars) for _ in range(password_lenth))
    
for _ in range(password_quantity):
    print(generate_password(chars, password_lenth))    