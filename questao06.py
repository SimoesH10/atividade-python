# Recebendo os 6 números
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))
num6 = int(input("Digite um número: "))


iguais = 0

if num1 == num2:
    iguais += 1
if num1 == num3:
    iguais += 1
if num1 == num4:
    iguais += 1
if num1 == num5:
    iguais += 1
if num1 == num6:
    iguais += 1

if num2 == num3:
    iguais += 1
if num2 == num4:
    iguais += 1
if num2 == num5:
    iguais += 1
if num2 == num6:
    iguais += 1

if num3 == num4:
    iguais += 1
if num3 == num5:
    iguais += 1
if num3 == num6:
    iguais += 1

if num4 == num5:
    iguais += 1
if num4 == num6:
    iguais += 1

if num5 == num6:
    iguais += 1

print("Quantidade de pares de números iguais:", iguais)
