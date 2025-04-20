menu = """

[d] Depositar
[s] Sacar
[e] extrato
[q] Sair

=>"""

saldo = 0
limite = 10000
extrato = ""
número_saques = 0
LIMITE_SAQUES = 10

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o seu valor:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = número_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! você não tem saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação falhou! número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            número_saques += 1

        else:
            print("Operação falhou! O valor informdo e inválido. ")

    elif opcao == "e":
       print("\n==============EXTRATO==============")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2F}")
       print("=========================================")

    elif opcao == "q":  
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
          