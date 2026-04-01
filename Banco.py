def depositar(saldo, extrato):
    valor = float(input("Por favor informe o valor de depósito desejado: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado não é válido.")
    return saldo, extrato


def sacar(saldo, extrato, numero_de_saques, limite, LIMITE_SAQUES):
    valor = float(input("Por favor informe o valor de saque desejado: "))
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedido = numero_de_saques >= LIMITE_SAQUES

    if saldo_excedido:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif limite_excedido:
        print("Operação falhou! O valor de saque excedeu o limite permitido.")
    elif saques_excedido:
        print("Operação falhou! Número de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_de_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_de_saques


def mostrar_extrato(saldo, extrato):
    print("\n**************** Extrato ****************")
    print("Sem registro de movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("*****************************************")


def main():
    menu = """
0 - Depositar
1 - Sacar
2 - Consultar Saldo
3 - Sair
"""

    saldo = 0
    limite = 750
    extrato = ""
    numero_de_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "0":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "1":
            saldo, extrato, numero_de_saques = sacar(saldo, extrato, numero_de_saques, limite, LIMITE_SAQUES)
        elif opcao == "2":
            mostrar_extrato(saldo, extrato)
        elif opcao == "3":
            print("Encerrando o sistema bancário. Obrigado por utilizar!")
            break
        else:
            print("Opção inválida, por favor selecione a opção desejada!")


# Executa o programa
main()
