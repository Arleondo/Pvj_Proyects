import turtle
ventana=turtle.Screen()
t2=turtle.Turtle()
t2.hideturtle()
t2.speed(1000)
t2.pensize(20)



t2.penup()
t2.goto(-350,-50)
t2.pendown()
t2.goto(-250,-50)
t2.penup()
t2.goto(-300,-50)
t2.pendown()
t2.goto(-300,250)
t2.goto(-200,250)
t2.goto(-200,200)


def buscar_coincidencia(p,l):
    x=0
    lista=[]
    for i in range(len(p)):
        if p[i] == l:
            lista.append(i)
            x=x+1
    if x>0:
        return True, lista
    else:
        return False

palabra='hola'
letra='a'
acer=list(buscar_coincidencia(palabra,letra))
if True in acer:
    for k in acer:
        num=k[0]
    print(palabra[num])

'''
t2.pensize(5)
t2.penup()
t2.goto(-200,140)
t2.pendown()
t2.circle(30)

t2.goto(-200,110)
t2.goto(-230,50)
t2.goto(-200,110)
t2.goto(-170,50)
t2.goto(-200,110)


t2.goto(-200,40)
t2.goto(-230,-10)
t2.penup()
t2.goto(-170,-10)
t2.pendown()
t2.goto(-200,40)
'''


turtle.done()