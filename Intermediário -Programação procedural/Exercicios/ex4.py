# '''
# Meu
# Fizz Buzz
# '''
# while True:
#     try:
#         def fb(n):
#             if n % 3 == 0 and n % 5 == 0:
#                 return 'Fizz Buzz'
#             elif n % 3 == 0:
#                 return 'Fizz'
#             elif n % 5 == 0:
#                 return 'Buzz'
#             else:
#                 return n
#         v = fb(
#             n=int(input('Digite um numero: '))
#         )
#         print(v)
#     except:
#         print('Digite apenas números')

'''
resposta
Fizz Buzz
'''
while True:
    try:
        def fb(n):
            if n % 3 == 0 and n % 5 == 0:
                return 'Fizz Buzz'
            if n % 3 == 0:
                return 'Fizz'
            if n % 5 == 0:
                return 'Buzz'
            return n
        v = fb(
            n=int(input('Digite um numero: '))
        )
        print(v)
    except:
        print('Digite apenas números')
