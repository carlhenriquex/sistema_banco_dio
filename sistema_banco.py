usuario = str(input("Informe seu nome: "))

saldo = 0
limite_diario = 3
depositos = []
saques = []

operacao = 4
while operacao != 0:


    operacao = int(input(f'''
    _________________________________________                     
    BANCO DIO   
    Olá, {usuario}!
    Selecione a operação que deseja realizar:
    [1] Saque
    [2] Depósito
    [3] Extrato
    [0] Sair
    '''
    ))

    if operacao == 1:

        if limite_diario > 0:

            valor = float(input("\n[SAQUE] Informe quanto deseja sacar: "))

            if valor > saldo:
                print("Saldo insuficiente.")

            else:
                if (valor < 1) or (valor > 500):
                    print("O valor excede o limite permitido por saque. Informe um valor entre R$1 e R$500")
                else:
                    print("Sacando..\n")
                    saldo -= valor
                    saques.append(valor)
                    limite_diario -= 1
                    print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")
        
        else:
            print("Limite diário de saque atingido")
            
    elif operacao == 2:

        valor = float(input("\n[DEPÓSITO] Informe o valor: "))

        if valor < 1:
            print("Valor inválido!")
        else:
            saldo += valor
            depositos.append(valor)
            print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")

    elif operacao == 3:
        print(f"\nEXTRATO TOTAL:")
        print("____________________")

        print("\nDEPÓSITOS:")
        if depositos:
            for deposito in depositos:
                print(f" + R$ {deposito:.2f}")
        else:
            print(" Não foram realizados depósitos.")
        
        print("\nSAQUES:")
        if saques:
            for saque in saques:
                print(f" - R$ {saque:.2f}")
        else:
            print(" Não foram realizados saques.")
        
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif operacao == 0:
        print("SESSÃO ENCERRADA.")
        break

    else:
        print("Operação invalida!")