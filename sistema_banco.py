import sys
from functions import saque, deposito, extrato

if __name__ == "__main__":
  
    clientes = {
        12350528420:{"nome": "Carlos Henrique", "data_nascimento": "01/01/2000"},
        12350528421:{"nome": "Davi Gabriel", "data_nascimento": "02/01/2000"}
    }
    contas = {
        1:{"agencia": "0001", "usuario": 12350528420, "saldo": 130},
        2:{"agencia": "0001", "usuario": 12350528421, "saldo": 540},
    }
    
    limite_diario = 3
    depositos = []
    saques = []
    
    cpf = input("Informe seu cpf sem pontos ou traço: ")
    num_conta = input("Informe o número da conta: ")
    
    if cpf.isdigit() and num_conta.isdigit():
        usuario = int(cpf)
        conta = int(num_conta)
    else:
        print("Dados inválido, digite corretamente.")
        sys.exit()                                                                                                           
    
    if (usuario in clientes) and (conta in contas):

        saldo = contas[conta]["saldo"]
        operacao = 4
        while operacao != 0:


            operacao = int(input(f'''
            _________________________________________                     
            BANCO DIO   
            Olá, {clientes[usuario]['nome']}!
            Saldo: {saldo}
            
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
                
    else:
        print("Usuário inexistente")