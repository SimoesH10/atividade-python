'''Faça um programa que calcula a quantidade de divisores de um número 
(incluindo 1 e o próprio número) que são divisíveis por 3.
'''

num = int(input("Digite um número: "))
resto = 0

if num % 3 == 0:
  resto = 1
  while num % 3 == 0:
    resto += 1
    num //= 3

  print(f"Quantidade de divisores divisíveis por 3: {resto}")
else:
  print(f"O número {num} não possui divisores múltiplos de 3")

