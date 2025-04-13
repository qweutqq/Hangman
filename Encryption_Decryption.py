
text = input('Просто введи свой текст тут:') #Начальная информация
print('Ты хочешь зашифровать (з) или дешифровать (д)?')
cryption = input()
print('Введи сдвиг:')
shift = int(input())
result = ''
print('Выбери язык шифрования (ru / en):')
language = input()

if language == 'en':
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + (shift if cryption == 'з' else -shift)) % 26 + ord('A'))
            elif char.islower():
                result += chr((ord(char) - ord('a') + (shift if cryption == 'з' else -shift)) % 26 + ord('a'))
        else:
            result += char
            
elif language == 'ru':
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('А') + (shift if cryption == 'з' else -shift)) % 32 + ord('А'))
            elif char.islower():
                result += chr((ord(char) - ord('а') + (shift if cryption == 'з' else -shift)) % 32 + ord('а'))
        else:
            result += char                        
print('Вот зашифрованный текст:', result)
     