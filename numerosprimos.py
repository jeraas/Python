#Achando números primos

def verifyNumber(n):
    d_c = 0
    for c in range(1, n + 1):
        if n % c == 0:
            if c == 1:
                print('{} - Número um.'.format(c))
            elif c == n:
                print('{} - Ele mesmo.'.format(c))
            else:
                print('{} - É dívisivel'.format(c))
                d_c = d_c + 1
                return d_c
        else:
            print(c)
    return d_c

def primoOuNao(d_c):
    if d_c > 0:
        print('Esse número não é primo')
    else:
        print('Esse número é primo')

again = 'yes'
while again[0] == 'y':
    n = int(input('Me de um número para verificar se os números até esse número são primos ou não.'))
    d_c = verifyNumber(n)
    primoOuNao(d_c)
    print('\n')
    print('\n')
    print('Quer testar outro número? [Y/N]')
    resp = str(input(''))
    while resp[0].lower() != 'n' or resp[0].lower() != 'y':
        if resp[0].lower() == 'n':
            again = 'no'
            break
        elif resp[0].lower() == 'y':
            again = 'yes'
            break
            
