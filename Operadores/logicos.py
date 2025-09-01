# Operadores lógicos: and, or, not
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

# Negação

not True  # False
not False  # True

not 1400 < 300

true and true # True
false and false # False
true and false # False  
false and true # False

true or true # True
false or false # False
true or false # True
false or true # True

not true # False
not false # True
not (true and false) # True
not (true or false) # False
not (false or false)

