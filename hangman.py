import random
word_list = ['cave', 'hangman', 'minecraft', 'backpack', 'grass', 'cumshot']

def get_word(word):
    word = random.choice(word_list)
    return word

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Добро пожаловать в игру виселицу!")
    print(display_hangman(tries))
    print(word_completion)
    print("\nУ вас есть", tries, "попыток. Пожалуйста, введите букву или слово:")

    while not guessed and tries > 0:
        guess = input()
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                word_completion = ''.join([guess if word[i] == guess else word_completion[i] for i in range(len(word))])
                print(word_completion)
            else:
                tries -= 1
                print('\nУ вас осталось', tries, 'попыток')    
                print(display_hangman(tries))
                print(word_completion)
        elif len(guess) > 1 and guess.isalpha():
            if guess == word:
                word_completion = word
                print('Поздравляю, вы угадали слово!')
                guessed = True
                print(word_completion)
                
            else:
                tries -= 1
                print('\nУ вас осталось', tries, 'попыток')    
                print(display_hangman(tries))
                print(word_completion)
        else:
            print('Был введен некорректный символ или слово!')
        if word_completion == word and tries >= 1:
            print('Поздравляю, вы угадали слово!')
            print(word.upper())
            break     

    again = input('Хотите сыграть еще раз? (д - да, н - нет)')
    if again.lower() == 'д':
        word = get_word(word_list)
        play(word)

word = get_word(word_list)
play(word)