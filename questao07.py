'''
     Desenvolva o algoritmo que receba o valor a ser pago por um produto e a forma de pagamento.
 Utilize os seguintes caracteres para identificar a forma de pagamento: C para cartão, P para PIX
 e D para dinheiro. Após o preenchimento dos campos, imprima o valor a ser pago aplicando os
 seguintes descontos:
 a) 10% para pagamento no cartão.
 b) 20% para pagamento no PIX.
 c) 30% para pagamento em dinheiro'''

valorProduto = int(input("Digite o valor de produto: "))
formaPagamento = str(input("Digite a forma de pagamento: "))


c = 10
p = 20
d = 30

if formaPagamento == "c":
    desconto = valorProduto * c / 100
    print(f'Você recebue um desconto de: {desconto} R$')
elif formaPagamento == "p":
    desconto = valorProduto * p / 100
    print(f'Você recebue um desconto de: {desconto} R$')
elif formaPagamento == "d":
    desconto = valorProduto * d / 100
    print(f'Você recebue um desconto de: {desconto} R$')