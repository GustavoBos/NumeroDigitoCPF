
'''O dígito do CPF é 3'''

#cpf = 660.822.590-33

#iterar numero por numero

#multiplicar cada numero da esquerda pra direita apartir do 10 ate 2, sendo (7*10, 4*9, 6*8, ...)

#apos isso, somar todos os numeros e multiplicar por 10 e depois divir por 11

#if resultado >= 9 = 0 / else = valor da divisao por 11 '''


cpf = 66082259033
numero_str = str(cpf)
total = 0

for i, digito in enumerate(numero_str):
    valor_decrescente = 10 - i
    if valor_decrescente >= 2:
        resultado = int(digito) * valor_decrescente
        total += resultado

total *= 10
total %= 11

if total > 9:
    total = 0
    
print(total)

