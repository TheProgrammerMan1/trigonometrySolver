def trigonometria(a, co, ca):
    sen30 = 0.5
    sen45 = 0.7071
    sen60 = 0.8660
    cos30 = 0.8660
    cos45 = 0.7071
    cos60 = 0.5
    tan30 = 0.5774
    tan45 = 1
    tan60 = 1.7321

    pergunta = input('digite o que voce quer encontrar \n cateto oposto (co) \n cateto adjascente(ca) \n hipotenusa (a) \n \n ')

    # CATETO OPOSTO

    if pergunta == 'co':
        if a > 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                co = sen30 * a
                print(f'O valor do cateto oposto é {co:.2f}')
            elif pergunta1 == '45':
                co = sen45 * a
                print(f'O valor do cateto oposto é {co:.2f}')
            elif pergunta1 == '60':
                co = sen60 * a
                print(f'O valor do cateto oposto é {co:.2f}')

        # TANGENTE PARA CATETO OPOSTO

        elif a == 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                co = tan30 * ca
                print(f'O valor do cateto oposto é {co:.2f}')
            elif pergunta1 == '45':
                co = tan45 * ca
                print(f'O valor do cateto oposto é {co:.2f}')
            elif pergunta1 == '60':
                co = tan60 * ca
                print(f'O valor do cateto oposto é {co:.2f}')

    
    # CATETO ADJASCENTE

    elif pergunta == 'ca':
        if a > 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                ca = cos30 * a
                print(f'O valor do cateto adjascente é {ca:.2f}')
            elif pergunta1 == '45':
                ca = cos45 * a
                print(f'O valor do cateto adjascente é {ca:.2f}')
            elif pergunta1 == '60':
                ca == cos60 * a
                print(f'O valor do cateto adjascente é {ca:.2f}')

        # TANGENTE PARA CATETO ADJASCENTE

        elif a == 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                ca = co / tan30
                print(f'O valor do cateto oposto é {ca:.2f}')
            elif pergunta1 == '45':
                ca = co / tan45
                print(f'O valor do cateto oposto é {ca:.2f}')
            elif pergunta1 == '60':
                ca = co / tan60
                print(f'O valor do cateto oposto é {ca:.2f}')
            
    # HIPOTENUSA

    elif pergunta == 'a':
        if ca == 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                a = co / sen30
                print(f'O valor da hipotenusa é {a:.2f}')
            elif pergunta1 == '45':
                a = co / sen45
                print(f'O valor da hipotenusa é {a:.2f}')
            elif pergunta1 == '60':
                a = co / sen60
                print(f'O valor da hipotenusa é {a:.2f}')
        if co == 0:
            pergunta1 = input('angulo formado? ')
            if pergunta1 == '30':
                a = ca / cos30
                print(f'O valor de a é {a:.2f}')
            elif pergunta1 == '45':
                a = ca / cos45
                print(f'O valor de a é {a:.2f}')
            elif pergunta1 == '60':
                a = ca / cos60
                print(f'O valor de a é {a:.2f}')


trigonometria()
