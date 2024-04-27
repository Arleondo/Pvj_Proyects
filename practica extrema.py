
cad='Eellas 4:10'
e=''
c=''
num=[1,2,3,4,5,6,7,8,9,0]

for i in cad:
    if i==':':
        if cad[len(cad)-2]==':':
            c=(int(str(cad[len(cad)-1])))
        else:    
            c=(int(str(cad[len(cad)-2])+str(cad[len(cad)-1])))
        break
    elif i!=':':
        for numero in num:
            if i==str(numero):
                for z in num:
                    if int(i)==z:
                        e=int(i)

print(e,c)


#       0                1               2
a=["Kill Bill","Estrllas 1:410", "Estrllas 4:12",  "Esrllas 2:120"]
b = [a[0], 0.0,0.0,0.0,0.0, ""]
maximo = 0
for e in range(1, len(a)): # 1 2
  c1 = a[e]
  i = 0
  while c1[i]!=":":
    i+=1
  num_es = int(c1[i-1])
  cali = float(c1[i+1:])
  b[num_es] = cali
  if cali>maximo:
    maximo = cali
b[5] = "Max: " + str(maximo)
print(b)
# deseado b=["Kill Bill", 101.0, 0.0, 0.0, 12.0, "Max: 12.0"]