datos=[["Kill Bill", "Estrllas 1: 10", "Estrllas 4:12"],
["Pulp Fiction ", "estrellas 3:11","Estrellas 4:2"],
["Psicosis", "Estrella 3:9","Estrellas 4:12", "Estrellas 1:10", "Estellas 2:13"],
["Seven", "Estres 1:10","Etrellas 4:12"],
["La miRAda", "Estrllas 1:10","EstrEllas 4:1", "Esrellas 2:12"],
["Millennium", "Cuenta 1:10","Estrels 4:12", "EstrellAS 2:1","Estrelas 3:18"],
["El cluB", "Esllas 1:10","Estrellas 4:12", "Estrels 3:17"],
["Ciudad de Dios", "Estlas 1:10", "Estrellas 3:2","Esrellas 4:12"],
["EL senor", "Estras 1:2","Esellas 3:11"],
["Buscando a Nemo", "Estllas 2:2", "Estreas 1:10"]]
peliculas = ["Buscando a Nemo", "Ciudad de Dios","El club","El senor","Kill Bill","Lamirada",
"Millennium","Psicosis","Pulp Fiction ","Seven"]

for listas in datos:
    maximo = 0
    b=[listas[0],0.0,0.0,0.0,0.0, '']
    for e in range(1, len(listas)): # 1 2
        c1 = listas[e]
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
