def saque(saldo, saques, limite_diario, valor):
    saldo -= valor
    saques.append(valor)
    limite_diario -= 1
    print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")
    return saldo, limite_diario

def deposito(saldo, depositos, valor):
    saldo += valor
    depositos.append(valor)
    print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")
    return saldo

def extrato(depositos, saques):
            
    print(f"\nEXTRATO TOTAL:")
    print("____________________")
    
    print("\nDEPÓSITOS:")
    for deposito in depositos:
        print(f" + R$ {deposito:.2f}")
    
    print("\nSAQUE:")    
    for saque in saques:
        print(f" - R$ {saque:.2f}")