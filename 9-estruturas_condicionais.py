saldo = 7000
saque = float(input("Informe o valo do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")
    saldo -= saque
    print(saldo)
else:
    print("Saldo insuficiente!")

#------

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque.")