""" Criar um sistema bancário com as operações: sacar, depositar e ver extrato """

# - Não depositar valores negativos;
# - Não precisa verificar número de agência e conta bancária;
# - Os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato;
# - Somente 3 saques diários;
# - Limite de R$ 500 por saque;
# - Os saques devem ser armazenados em uma variável e exibidos na operação de extrato;
# - O extrato deve listar todos os depósitos e saques da conta e o saldo atual;
# - Se o extrato estiver em branco, exibir a mensagem "Não foram realizadas movimentações"
# - Formatar a saída dos valores em Real (R$)

import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
numero_saques = 0
registros_de_depositos = []
registros_de_saques = []
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        print("### Depósito ###\n")
        deposito = float(input("Digite o valor a ser depositado: "))

        if deposito <= 0:

            print("Digite um valor válido.")

        else:

            saldo += deposito
            data_hora_deposito = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
            registro_deposito = (deposito, data_hora_deposito)
            registros_de_depositos.append(registro_deposito)
            print(f"Depósito efetuado com sucesso!\nSeu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "s":

        print("### Saque ###\n")
        saque = float(input("Digite o valor para saque: "))

        if saque <= saldo and saque <= limite and numero_saques != LIMITE_SAQUES:

            saldo -= saque
            data_hora_saque = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
            registro_saque = (saque, data_hora_saque)
            registros_de_saques.append(registro_saque)
            print(f"Saque efetuado com sucesso!\nSeu saldo atual é: R$ {saldo:.2f}")
            numero_saques += 1

        elif saque > saldo or saque > limite:

            print(f"Seu saldo é insuficiente para realizar essa operação ou limite de saque de R$ 500.00 foi atingido. Seu saldo atual é: R$ {saldo:.2f}")
        
        else:

            print("A operação não pode ser realizada. O limite de saques diário foi atingido.")

    elif opcao == "e":

        print("### Extrato ###\n")

        if not registros_de_depositos and not registros_de_saques:

            print("Não foram realizadas movimentações.")
        
        else:

            for deposito, data_hora in registros_de_depositos:
                print(f"Depósito de R$ {deposito:.2f} em {data_hora}")

            print("")

            for saque, data_saque in registros_de_saques:
                print(f"Saque de R$ {saque:.2f} em {data_saque}")

            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Por favor, selecione novamente a operação desejada.")
