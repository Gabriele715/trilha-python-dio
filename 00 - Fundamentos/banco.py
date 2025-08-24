import datetime

# Variáveis globais
saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

def menu():
    print("\n--- SISTEMA BANCÁRIO ---")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")

def depositar():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato += f"{datetime.datetime.now()} - Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! Valor inválido.")

def sacar():
    global saldo, extrato, numero_saques
    if numero_saques >= LIMITE_SAQUES_DIARIO:
        print("Limite diário de saques atingido.")
        return

    valor = float(input("Informe o valor do saque: R$ "))
    if valor <= 0:
        print("Operação falhou! Valor inválido.")
    elif valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite_saque:
        print(f"Operação falhou! Limite por saque é R$ {limite_saque}.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"{datetime.datetime.now()} - Saque:    R$ {valor:.2f}\n"
        print("Saque realizado com sucesso.")

def mostrar_extrato():
    print("\n--- EXTRATO ---")
    if extrato:
        print(extrato)
    else:
        print("Nenhuma movimentação registrada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")

# Loop principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        mostrar_extrato()
    elif opcao == "0":
        print("Saindo... Obrigado por usar nosso sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")

