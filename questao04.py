'''Escreva um programa que calcule os N termos da série S abaixo:

S = (1/3) + (2/6) + (3/9) + (4/12) + …

O seu programa deve imprimir na saída padrão tanto os termos da série quanto o valor da soma com precisão de 2 casas decimais.'''

N = int(input("Entrada:\n"))


fracoes = [f"{k}/{3*k}" for k in range(1, N+1)]
expressao = " + ".join(fracoes)


soma = N / 3

print("\nSaída:\n")
print(expressao)
print(f"{soma:.2f}")
