import random

senhas = ['abcd', 'foda', 'efgh', 'como', 'tope', 'joke']
senha = random.choice(senhas)

letters = 'acdefghijklmnopqrstuvwxyz'.split()
word = ['']

while True:
    if len(word[0]) != 4:
        letterChoiced = random.choice(letters)
        word.append(letterChoiced)
    else:
        result = ''
        for letter in word[0]:
            result = result + letter
        if result == senha:
            print('Key found:', result)
        else:
            print('Error:', result)
        
        
