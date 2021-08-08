"""
IF, ELSE e ELIF
"""

sd = int(input('Type the password: '))
#  verificar
if sd == 1234:  # se
    print('Welcome!')
elif sd == 0000:  # se nao se
    print('Reset Password')
else:  # se nao
    print('Incorrect password')
