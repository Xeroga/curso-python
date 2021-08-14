
    # n1 = input('Digite um numero :')
    # n2 = input('Digite outro numero :')
    # n3 = input('Digite mais numero :')

    # if not n1 or not n2 or not n3:
    #     print('Campo esta vazio')
    #     continue
    # elif not n1.isnumeric() or not n2.isnumeric() or not n3.isdigit():
    #     print('Digite apenas numeros inteiros')
    #     continue

    # n1 = int(n1)
    # n2 = int(n2)
    # n3 = int(n3)
while True:
    def soma(n1, n2, n3):
        print(n1 + n2 + n3)
    try:
        soma(
        n1 = float(input('Digite um numero :')),
        n2 = float(input('Digite outro numero :')),
        n3 = float(input('Digite mais numero :')),
        )
    except:
        print('Apenas numeros')