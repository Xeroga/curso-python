while True:
    def aumento(n1, n2):
        return n1 * n2 / 100 + n1
    try:
        resp = aumento(
            n1=float(input('Digite um valor: ')),
            n2=float(input('Digite a % do aumento: '))
        )
        print(resp)
    except:
        print('Digite apenas números.')
