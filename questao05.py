'''Desenvolva um algorítimo que receba 3 números inteiros diferentes e os imprima em ordem
decrescente. '''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

numeros = num1, num2, num3

for i in reversed(numeros):
    print(i)