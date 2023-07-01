
extrato = ""

saldo = 0

LIMITE = 500
LIMITE_SAQUES = 3

opcao = -1
saques_no_dia = 0
operacoes_no_dia = 0

while opcao != 0:
    if operacoes_no_dia == 0:
        opcao = int(input("Olá, seja muito bem vindo! No que posso lhe ajudar? \n [1] Depositar \n [2] Sacar \n [3] Extrato \n [0] Sair \n: "))
        operacoes_no_dia += 1
    else:
        opcao = int(input("Há algo mais em que eu possa lhe ajudar? \n [1] Depositar \n [2] Sacar \n [3] Extrato \n [0] Sair \n: "))
        operacoes_no_dia += 1

    #Operação de depósito
    if opcao == 1:
        valor_de_deposito = float(input("Insira o valor que você deseja depositar: "))

        if float(valor_de_deposito) <= 0:
            print("O valor deve ser maior que 0.")
        else:
            saldo += valor_de_deposito
            extrato += f"Depósito: R$ {valor_de_deposito:.2f}\n "
            
            print(f"Valor de R${valor_de_deposito:.2f} depositado com sucesso. \n")

    #Operação de saque
    elif opcao == 2:
        valor_de_saque = float(input("Insira o valor que você deseja sacar: "))

        if valor_de_saque > 500 or valor_de_saque > saldo:
            if valor_de_saque > 500:
                print("Só é possível realizar saques de até R$500.00 \n")
            else:
                print("Não foi possível realizar a operação, saldo insuficiente. \n")
        else:
            saques_no_dia += 1

            if saques_no_dia > LIMITE_SAQUES:
                print("Só é possível realizar 3 saques por dia. \n Obrigado por utilizar os nossos serviços. \n")
                
            else:
                saldo -= valor_de_saque
                extrato += f"Saque: R$ {valor_de_saque:.2f}\n "
                print(f"Valor de R${valor_de_saque:.2f} sacado com sucesso. \n")
            
    #Operação de extrato
    elif opcao == 3:
        print(f"EXTRATO \n {extrato} \n Saldo em conta: R${saldo} \n")


    #Sair    
    elif opcao == 0:
        print("Obrigado por utilizar o nosso sistema!")
        break
    else: 
        print("Opção inválida, por favor selecione outra opção.")