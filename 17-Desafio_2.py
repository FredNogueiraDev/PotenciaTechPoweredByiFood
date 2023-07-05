valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebida = valorBebida * quantidadeBebida
precoFinal = totalBebida + totalHamburguer
totalTroco = valorPago - precoFinal

precoFinal = format(precoFinal, ".2f")
totalTroco = format(totalTroco, ".2f")

print(f"O preço final do pedido é R$ {precoFinal}. Seu troco é R$ {totalTroco}")


# valorHamburguer = 10.00;
# quantidadeHamburguer = 2;
# valorBebida = 5.00;
# quantidadeBebida = 1;
# valorPago = 30.00;