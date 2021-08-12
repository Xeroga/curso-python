# Loop infinito
while True:
    print(50*'=')
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                         # Elimina os 2 ultimos digitos do CPF
    qnt = int(len(cpf))                              # conta a quantidade de caracteres
    reverso = 10                                # contador reverso
    total = 0
    # verificação
    if not cpf:                                 # Verifica se esta vazia
        print('Campo não pode estar vazio.')
        continue
    elif not cpf.isnumeric():                   # verifica se é numeros positivo
        print('Digite apenas numeros...')
        continue
    elif not qnt == 11:                         # verifica se tem 11 numeros
        print('CPF esta faltando')
        continue

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

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * qnt  # len(cpf)
    # Descobre que sequencias avaliam como verdadeiro
    msg = 'CPF Válido' if cpf == novo_cpf and not sequencia else 'CPF Inválido'
    print(msg)
