from random import randint
numero = str(randint(100000000, 999999999)) # Gera um numero aleatório de 1 a 9

novo_cpf = numero                           # Elimina os 2 ultimos digitos do CPF
qnt = int(len(numero))                      # conta a quantidade de caracteres
reverso = 10                                # contador reverso
total = 0

# Loop do CPF
for index in range(19):
    if index > 8:                           # Primeiro índice vai 0 a 9
        index -= 9                          # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso # Valor total da multiplicação

    reverso -= 1                            # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                           # Se o digito for > 9 o valor é 0
            d = 0
        total = 0                           # Zera o total
        novo_cpf += str(d)                  # Concatena o digito gerado no novo CPF

print(novo_cpf)