'''Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos 
no intervalo definido por eles, considerando inclusive os extremos.'''

num1 = int(input("digite um número: "))
num2 = int(input("digite um número: "))

while num2 < num1:

	num1 = int(input("digite um número: "))
	num2 = int(input("digite um número: "))



else:
	for i in range(num1, num2):
			if num1 < 0:
				num1 += 1
			i = num1 + num2
	print(i)
