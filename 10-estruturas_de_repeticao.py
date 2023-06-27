for numero in range(0,11):
    print (numero, end= " ")
else:
    print(" ") #Quebra de linha

for numero in range(0,51,5):
    print (numero, end=" ")
else:
    print(" ") #Quebra de linha

opcao = -1

while opcao != 0:
    opcao = int(input(" [1] Sacar \n [2] Extrato \n [0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else: 
    print("Obrigado por utilizar o nosso sistema!")