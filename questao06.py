'''Desenvolva um algorítimo que receba 6 números inteiros em imprima quantos são iguais.'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))
num6 = int(input("Digite um número: "))


iguais = 1

while True:
    if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5 or num1 == num6:
        iguais += 1
        break
print(iguais)