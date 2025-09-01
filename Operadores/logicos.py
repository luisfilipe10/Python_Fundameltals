saldo = 1000
saque = 200
limite = 400

if saque > saldo or saque > limite:
    if saque > saldo and saque > limite:
        print("Saque maior que saldo e limite")
    elif saque > saldo:
        print("Saque maior que o saldo")
    else:
        print("Saque acima do limite")
else:
    print("Saque permitido")
