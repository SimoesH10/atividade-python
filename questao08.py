'''
 Em um determinado campeonato, ao cadastrar o atleta devemos informa a organização qual
 categoria ele irá competir de acordo com a sua idade. Desenvolva um algoritmo que receba o
 nome e idade do atleta e em seguida imprima seu nome seguido da categoria na qual ele ira
 competir. Utilize a tabela abaixo no seu algoritmo.

5 até 7            8 até 10
Infantil A         Infantil B

11 até 13           14 até 17 
Juvenil A           Juvenil B

 Maior que 18 
Adult
'''

nome = str(input("Digite se nome: "))
idade = int(input("Digite sua idade: "))

if idade >= 5 and idade  <= 7:
    print(f'o atleta {nome} participa da categoria Infantial A')
elif idade >=8 and idade <= 10:
    print(f'o atleta {nome} participa da categoria Infantial B')
elif idade >= 11 and idade <= 13:
    print(f'o atleta {nome} participa da categoria Juvenil A')
elif idade >= 14 and idade <= 17:
    print(f'o atleta {nome} participa da categoria Infantial B')
elif idade >= 18:
    print(f'o atleta {nome} participa da categoria Adulta')
else:
    print("Idade invalida")