"""
FOR / ELSE
continue
break
"""

nomes = ['joao', 'maria',]

for nome in nomes:
    #  nome.lower().startswith('j')  converte para minusculo
    if nome.startswith('j'):  # verifica se a primeira letra começa com j
        print(nome,'Começa com J')
    else:
        print(nome,'Nao começa com J')