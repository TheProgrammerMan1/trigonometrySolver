import math

def trigonometria():
    valores = [
        {'sen30': 0.5}, {'sen45': 0.7071}, {'sen60': 0.8660}, {'cos30': 0.8660}, {'cos45': 0.7071},
        {'cos60': 0.5}, {'tan30': 0.5774}, {'tan45': 1}, {'tan60': 1.7321}
    ]

    a = int(input('Digite o valor de a: '))
    co = int(input('Digite o valor de co: '))
    ca = int(input('Digite o valor de ca: '))

    pergunta = input('\nDigite o que voce quer encontrar \n cateto oposto (co) \n cateto adjascente(ca) \n hipotenusa (a) \n \n ')

        # CATETO OPOSTO

    if pergunta == 'co':
        if a > 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                co = valores[0]['sen30'] * a
                print(f'O valor do cateto oposto é {co:.2f}')
            elif pergunta1 == '45':
                co = valores[1]['sen45'] * a
                print(f'O valor do cateto oposto é {co:.2f}')
            elif pergunta1 == '60':
                co = valores[2]['sen60'] * a
                print(f'O valor do cateto oposto é {co:.2f}')

        # TANGENTE PARA CATETO OPOSTO

        elif a == 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                co = valores[6]['tan30'] * ca
                print(f'O valor do cateto oposto é {co:.2f}')
            elif pergunta1 == '45':
                co = valores[7]['tan45'] * ca
                print(f'O valor do cateto oposto é {co:.2f}')
            elif pergunta1 == '60':
                co = valores[8]['tan60'] * ca
                print(f'O valor do cateto oposto é {co:.2f}')

    
        # CATETO ADJASCENTE

    elif pergunta == 'ca':
        if a > 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                ca = valores[3]['cos30'] * a
                print(f'O valor do cateto adjascente é {ca:.2f}')
            elif pergunta1 == '45':
                ca = valores[4]['cos45'] * a
                print(f'O valor do cateto adjascente é {ca:.2f}')
            elif pergunta1 == '60':
                ca == valores[5]['cos60'] * a
                print(f'O valor do cateto adjascente é {ca:.2f}')

        # TANGENTE PARA CATETO ADJASCENTE

        elif a == 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                ca = co / valores[6]['tan30']
                print(f'O valor do cateto oposto é {ca:.2f}')
            elif pergunta1 == '45':
                ca = co / valores[7]['tan45']
                print(f'O valor do cateto oposto é {ca:.2f}')
            elif pergunta1 == '60':
                ca = co / valores[8]['tan60']
                print(f'O valor do cateto oposto é {ca:.2f}')
            
        # HIPOTENUSA

    elif pergunta == 'a':
        if ca == 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                a = co / valores[0]['sen30']
                print(f'O valor da hipotenusa é {a:.2f}')
            elif pergunta1 == '45':
                a = co / valores[1]['sen45']
                print(f'O valor da hipotenusa é {a:.2f}')
            elif pergunta1 == '60':
                a = co / valores[2]['sen60']
                print(f'O valor da hipotenusa é {a:.2f}')
        if co == 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                a = ca / valores[3]['cos30']
                print(f'O valor de a é {a:.2f}')
            elif pergunta1 == '45':
                a = ca / valores[4]['cos45']
                print(f'O valor de a é {a:.2f}')
            elif pergunta1 == '60':
                a = ca / valores[5]['cos60']
                print(f'O valor de a é {a:.2f}')
    
    pergunta0 = input('Mais uma vez y/n? ')
    if pergunta0 == 'y':
        trigonometria()
    else:
        return


trigonometria()
