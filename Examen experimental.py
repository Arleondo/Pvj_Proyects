'''
#QUE GOD 
ejemplo=['A 999','B 43','2']
Lista=[]
nums=['1','2','3','4','5','6','7','8','9','0']
for i in ejemplo:
    for a in range(len(i)):
        for z in nums:
            if i[a]==z:
                Lista.append(int(i[a: ]))
print(Lista)

ejemplo=[1,2,5,6,3,7,98,100,2,7,4]
Lista=[]
for i in ejemplo:
    encontrado=False
    for a in Lista:
        if a==i:
            encontrado=True
    if encontrado==False:
        Lista.append(i)
print(Lista)

ejemplo=[[11,22,33],[1,2,3],[3,1],[4]]
lista=[]
for i in ejemplo:
    lista.append(len(i))
print(lista)

ejemplo1=[[34,9,10],[90,34,1]]
Lista=[]
for i in ejemplo1:
    x = 0
    for a in i:
        if a>x:
            x=a
    Lista.append(x)
print(Lista)

ejemplo1=[40,50,20,8]
minimo=ejemplo1[0]
for i in ejemplo1:
    if i<minimo:
        minimo=i
for min in range(1,minimo+1):
    x=0
    for i in ejemplo1:
        if i%min==0:
            x=x+1
    if x==len(ejemplo1):
        mcd=min
print(mcd)

c='mariano'
print(c[1]+c[3]+c[5])

cad=input('Escribir palabra: ')
def es_palindromo (a):
    for i in range(len(a)//2):
        if a[i]!=a[-(i+1)]:
            return False
    return True

print(es_palindromo(cad))

cad=input()
nums=['1','2','3','4','5','6','7','8','9','0',]
for i in cad:
    for u in nums:
        if i==u:
            break
        else:
            continue
x=int(cad[i: ])

Iden=[['Maria Melo',30,76543443],['Yvan Gomez',54,40986774]]
for i in Iden:
    for u in i:
        if u==i[0]:
            for L in range(len(u)):
                if u[L]==' ':
                    x=str(u[L: ])
        elif u==i[2]:
            y=str(u)
    z=str(x+y+'@ucsp.edu.pe')
    i.append(z)
print(Iden)
'''
def longitud_maxima_minima(La):
  menor=0
  mayor=0
  exit=[]
  for i in range(len(La)):
    if La[i]<La[menor]:
      menor=i
  
  for u in range(len(La)):
    if La[u]>La[mayor]:
      mayor=u

  exit.append(La[menor])
  exit.append(La[mayor])
  print(exit)

nums= [[2, 3, 4, 5], [1, 23], [1, 34, 5, 27], [9, 11], [3, 75, 7]]
longitud_maxima_minima(nums)
