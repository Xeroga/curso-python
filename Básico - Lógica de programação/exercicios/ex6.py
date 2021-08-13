hr = input('Que horas sao: ')
#  converter str >> int
try:
    hr = float(hr)
    #  iniciar
    if hr >= 0 and hr < 12:
        print('Bom Dia')
    elif hr >= 12 and hr <= 17:
        print('Boa Tarde')
    elif hr > 17 and hr <= 23.59:
        print('Boa Noite')
    else:
        print(f'"{hr}" Nao e um Horario')
except:
    print(f'"{hr}" Nao e um Horario')