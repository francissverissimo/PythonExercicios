m = ''' (DESAFIO 026)
    Faça um programa que leia uma frase
    pelo teclado e mostre:
        > Quantas vezes aparece a letra "A";
        > Em que posição ela aparece a primeira vez;
        > Em que posição ela aparece a última vez. '''
print(m, '\n')

frase = str(input('Digite uma frase: '))

frase = frase.upper().strip()

print(f'A letra "A" aparece {frase.count("A")} vezes.')

print(f'A letra "A" aparece primeiro na posição {frase.find("A") + 1}.')

print(f'A letra "A" aparece por último na posição {frase.rfind("A") + 1}.')
