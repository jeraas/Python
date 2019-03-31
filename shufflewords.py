from random import randint

string = str(input('Say something to shuffle: \n'))

letters = []
for letter in string:
    letters.append(letter)

# Equivalente a um 'list(string)'

for character in letters:
    for c in range(0, len(string)):
        selected = randint(0, len(string) - 1)
        save = letters[c]
        letters[c] = letters[selected]
        letters[selected] = save

print('Output returns: {}'.format("".join(letters)))

