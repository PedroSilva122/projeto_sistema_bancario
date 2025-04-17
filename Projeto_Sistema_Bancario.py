operacao = """ 
=========Menu=========
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
======================
"""

deposito = 0
saque = 0
QNTD_SAQUE = 3
LIMITE_SAQUE = 500
saques_realizados = 0
transacoes = []

while True:
    opcao = int(input((operacao)))

    if opcao == 1:
        valor = float(input("Digite o valor do seu depósito: R$"))
        deposito = valor
        transacoes.append(deposito)
    elif opcao == 2:
        if saques_realizados < QNTD_SAQUE:
            valor = float(input("Digite o valor do saque: R$"))
            saque = valor
            if saque > deposito:
                print(f"Saque maior do que o depósito atual\nR${deposito:.2f}")
                continue
            elif saque > LIMITE_SAQUE:
                print("Saque acima do valor máximo de R$500")
                continue
            else:
                deposito -= saque
                print(f"Saque realizado\nDepósito atual: R${deposito:.2f}")
                transacoes.append(saque)
            saques_realizados += 1
        else:
            print("Saques diários já foram concluidos")
    elif opcao == 3:
        print("\nExtrato")
        for transacao in transacoes:
            print(f"Transação: R${transacao:.2f}")
        print(f"Saldo atual: R${deposito:.2f}")
    elif opcao == 0:
        print("Saindo da transação")
        break
    else:
        print("Insira uma opção válida")