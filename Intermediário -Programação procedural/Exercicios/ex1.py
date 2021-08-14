# while True:
#     nome = input('Digite seu nome: ')
#     msg = input('Digite uma saudação: ')
#     def saudacao(msg, user):
#         return f'{msg} {user}'
#
#     var = saudacao(msg or 'Digite uma Saudação.', nome or 'Voce nao digitou um nome.')
#     print(var)

while True:
    nome = input('Digite seu nome: ')
    msg = input('Digite uma saudação: ')
    def saudacao(msg, user):
        print(msg, user)
    saudacao(msg or '"Digite uma Saudação"', nome or '"Voce nao digitou um nome."')