"""
Operador ternário
"""
logged_user = False

# if logged_user:
#     msg = 'Usuario Logado'
# else:
#     msg = 'Usuario precisa logar'
# print(msg)

msg = 'Usuario Logado.' if logged_user else 'Usuario precisa Logar.'
print(msg)

idade = input('Qual a sua idade: ')
if not idade.isnumeric():
    print('Voce  precisa digitar apenas numeros')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'pode acessar' if e_de_maior else 'Nao pode'
    print(msg)