'''Seu programa deve calcular o custo total mensal com base nessas 
informações e imprimir o resultado. Além disso, ele deve verificar se o custo total 
mensal ultrapassa um limite máximo de R$ 10.000. Se o custo total mensal for maior que esse limite
, o programa deve exibir uma mensagem indicando que o custo está acima do limite.

Servidores: O custo mensal por servidor é de R$ 500.

Banco de Dados: O custo mensal por unidade de capacidade do banco de dados é de R$ 100.

Armazenamento de Dados: O custo mensal por gigabyte de armazenamento de dados é de R$ 0,10.

Transferência de Dados: O custo mensal por gigabyte de transferência de dados de entrada e saída é de R$ 0,05.'''


n = int(input("Digite o número de servidores: "))
m = int(input("Digite o número de unidades de capacidade do banco de dados: "))
o = float(input("Digite a quantidade de armazenamento de dados (em GB): "))
p = float(input("Digite a quantidade de transferência de dados (em GB): "))

custoServidores = n * 500
custoBancoDados = m * 100
custoArmazenamento = o * 0.10
custoTransferencia = p * 0.05 
"""A sepração de casas decimais é feita por '.' e não por ','  """

custoTotal = custoServidores + custoBancoDados + custoArmazenamento + custoTransferencia

print(custoTotal)

if custoTotal > 10000:
    print("Atenção: o custo total está acima do limite de R$ 10.000.")
