import random
a= random.randint(1,2)
toe=[['','',''],['','',''],['','','']]
con=1
while con<=9:
    if a==2:
        for z in toe:
            for u in z:
                print('|', u,'|',end='\t')
            print()
        fi=int(input('Poner fila: '))
        col=int(input('Poner columna: '))
        if fi>3 or col>3 or fi<1 or col<1:
            print('Coordenadas invalidas')
        else:
            toe[fi-1][col-1]='X'
        a=-1
    elif a==1:
        for z in toe:
            for u in z:
                print('|', u,'|',end='\t')
            print()
        fi2=int(input('Poner fila: '))
        col2=int(input('Poner columna: '))
        if col2>3 or fi2>3 or col2<1 or fi2<1:
            print('Coordenadas invalidas')
        else:    
            toe[fi2-1][col2-1]='O'

        a=+1
    con+=1