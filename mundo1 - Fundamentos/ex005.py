m = ''' (DESAFIO 005)
    Faça um programa que leia um número inteiro e
    mostre na tela o seu sucessor e seu antecessor: '''
print(m, '\n')

n = int(input('Digite um número: '))

a = n - 1
s = n + 1

print(f'Analisando o valor {n}, seu antecessor é {a} e seu sucessor é {s}')
