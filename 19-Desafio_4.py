# Desafio
# Você foi contratado para desenvolver um sistema que armazena informações dos pedidos de comida online realizados por um cliente. O sistema 
# deve permitir ao cliente inserir novos pedidos, escolher um cupom de desconto (10% ou 20%) e exibir o valor total de todos os pedidos realizados 
# até o momento, com o desconto aplicado.

# Entrada
# A entrada é composta por:

# Uma linha com um número inteiro n representando a quantidade de pedidos que o usuário deseja inserir;
# n linhas, cada uma contendo uma string com o nome do pedido e um valor em ponto flutuante separados por espaço. O nome do pedido não contém 
# espaços em branco;
# Uma linha contendo o cupom de desconto escolhido (10% ou 20%).
# Saída
# O programa deve exibir uma única linha contendo o valor total de todos os pedidos com o desconto aplicado, no seguinte formato:

# Valor total: XX.YY, onde "XX.YY" é a soma de todos os pedidos com desconto em formato de duas casas decimais após a vírgula.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com
#  esses exemplos e com outros casos possíveis.


# Entrada	            Saída
# 3
# Pizza 29.90
# Hambúrguer 15.50
# Refrigerante 7.00
# 10%	
#                       Valor total: 47.16
# 2
# Salada 12.00
# Suco 10.50
# 20%	                Valor total: 18.00
# 4
# X-Burger 19.99      
# Salada 29.99
# Sushi 61.00
# Pudim 10.00
# 20%	                Valor total: 96.78

def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
    
    desconto = input()

    if desconto == "10%":
        total = round((total * 0.9), 2)
    else:
        total = round((total * 0.8), 2)

    total = "{:.2f}".format(total)
    
    print (f"Valor total: {total}")
 
 
if __name__ == "__main__":
    main()