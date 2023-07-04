import textwrap

#Menu de login do usuário
def menu_login():
    menu_login = """\n
    ---------- MENU ----------
    
    [1]\tNovo usuário
    [2]\tListar contas
    [3]\tNova conta 
    [4]\tEfetuar Login 
    [5]\tSair  
    
    => """
    return input(textwrap.dedent(menu_login))

#Nova conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\nUsuário não encontrado.")
        criar_usuario(usuarios)

#Listar contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

#Novo usuário
def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nOperação falhou! Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! Seja muito bem vindo ao nosso banco! ===")

#Efetuar login
def login(usuarios):
    cpf = input("Informe o seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        logado = True
        return logado
    else:
        print("\nOperação falhou! Não foi encontrado um usuário com esse CPF! ")
        criar_usuario(usuarios)

#Filtrar usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#USUÁRIO LOGADO NO SISTEMA

#Menu de operações
def menu_logado():
    menu_logado = """\n
    ---------- MENU ----------

    [1]\tDepositar 
    [2]\tSacar 
    [3]\tExtrato 
    [4]\tSair  
    
    => """
    return input(textwrap.dedent(menu_logado))

#Depositar
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"Valor de R${valor:.2f} depositado com sucesso. \n")
    else:
        print("Operação falhou! O valor informado é inválido. \n")

    return saldo, extrato

#Sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print("Operação falhou! Saldo insuficiente. \n")

    elif valor > limite:
        print(f"Operação falhou! Só é possível realizar saques de até R${limite} \n")

    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido. \n")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Valor de R${valor:.2f} sacado com sucesso. \n")

    else:
        print("Operação falhou! O valor informado é inválido. \n")

    return saldo, extrato

#Extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

#
def main():
    AGENCIA = "0001"

    usuarios = []
    contas = []
    logado = False

    while True:
        opcao = menu_login()

        if opcao == "1":
            criar_usuario(usuarios)

        elif opcao == "2":
            listar_contas(contas)

        elif opcao == "3":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "4":
            login(usuarios)

            while True:
                LIMITE_SAQUES = 3

                saldo = 0
                limite = 500
                extrato = ""
                numero_saques = 0
                
                opcao = menu_logado()

                if opcao == "1":
                    valor = float(input("Informe o valor do depósito: "))

                    saldo, extrato = depositar(saldo, valor, extrato)

                elif opcao == "2":
                    valor = float(input("Informe o valor do saque: "))

                    saldo, extrato = sacar(
                        saldo=saldo,
                        valor=valor,
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saques=LIMITE_SAQUES,
                    )

                elif opcao == "3":
                    exibir_extrato(saldo, extrato=extrato)

                elif opcao == "4":
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")

        elif opcao == "5":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()