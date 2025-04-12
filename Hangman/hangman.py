import random
word_list = ['cave', 'hangman', 'minecraft', 'backpack', 'grass', 'cumshot']

def get_word(word):
    word = random.choice(word_list)
    return word

def display_hangman(tries):
    stages = [  # Final state: head, torso, both arms, and both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both arms, and one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso, and both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, torso, and one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # first state
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
    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\nYou have", tries, "tries to guess the word. Please enter a letter or a word.")

    while not guessed and tries > 0:
        guess = input()
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                word_completion = ''.join([guess if word[i] == guess else word_completion[i] for i in range(len(word))])
                print(word_completion)
            else:
                tries -= 1
                print('\nYou have', tries, 'tries left.')    
                print(display_hangman(tries))
                print(word_completion)
        elif len(guess) > 1 and guess.isalpha():
            if guess == word:
                word_completion = word
                print('Congratulations! You guessed the word!')
                guessed = True
                print(word_completion)
                
            else:
                tries -= 1
                print('\nYou have', tries, 'tries left.')    
                print(display_hangman(tries))
                print(word_completion)
        else:
            print('Please enter correct word or letter.')
        if word_completion == word and tries >= 1:
            print('Congratulations! You guessed the word!')
            print(word.upper())
            break     

    again = input('Wanna play again? (y/n)')
    if again.lower() == 'y':
        word = get_word(word_list)
        play(word)

word = get_word(word_list)
play(word)