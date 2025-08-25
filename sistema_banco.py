from functions import saque, deposito, extrato

if __name__ == "__main__":

    saldo = 0
    limite_diario = 3
    depositos = []
    saques = []

    usuario = str(input("Informe seu nome: "))

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
                        saldo, limite_diario = saque(saldo, saques, limite_diario, valor)
            
            else:
                print("Limite diário de saque atingido")
                
        elif operacao == 2:

            valor = float(input("\n[DEPÓSITO] Informe o valor: "))

            if valor < 1:
                print("Valor inválido!")
            else:
                saldo = deposito(saldo, depositos, valor)
                

        elif operacao == 3:

            if depositos or saques:
                extrato(depositos, saques)
                print(f"\nSaldo atual: R$ {saldo:.2f}")
                
            else:
                print(" Não foram realizadas movimentações.")

        elif operacao == 0:
            print("SESSÃO ENCERRADA.")
            break

        else:
            print("Operação invalida!")