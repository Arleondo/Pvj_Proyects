'''
class punto2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mostrar_punto_en(self):
        print('(',self.x,',',self.y,')')

class Rectangulo:
    def __init__(self,a1,a2,p):
        self.anchura=a1
        self.altura=a2
        self.puntobase=p
    def mostrar_datos(self):
        print('Ancho:', self.anchura)
        print('Alto:', self.altura)
        print('Punto base:', end='')
        self.puntobase.mostrar_punto_en()
    def calcular_centro(self):
            return punto2D(self.puntobase.x + self.anchura/2, self.puntobase.y + self.altura/2 )
    def Punto_A (self):
            return punto2D(self.puntobase.x , self.puntobase.y + self.altura)
    def Punto_B (self):
            return punto2D(self.puntobase.x + self.anchura , self.puntobase.y + self.altura)
    def Punto_C (self):
            return punto2D(self.puntobase.x + self.anchura , self.puntobase.y)
    def Perimetro(self):
            return self.anchura * 2 + self.altura * 2
    def Area(self):
            return self.anchura*self.altura
def main():
    p1=punto2D(6,6)
    r1=Rectangulo(8,2,p1)
    pc1=r1.calcular_centro()
    pc1.mostrar_punto_en()
    print(r1.Perimetro())
    print(r1.Area())
main()


n_c=1
n_f=12
l=[1,2,3,4,5,6,7,8,9,10,11,12]
m=[]
x=0
for i in range(0,len(l),n_c):
        m.append(l[i:i+n_c])
        x=x+1
print(m)


datos= [1,2,3,4,5,6,7,8,9,10,11,12]
filas= 4
col=3
m=[]
k=0
for f in range(filas):
        fil_temp = []
        for c in range(col):
                fil_temp.append(datos[k])
                k += 1
        m.append(fil_temp)
print(m)
'''

class matriz:
  def __init__(self,n_col,n_fil,l):
    self.columnas=n_col
    self.filas=n_fil
    self.m=[]
    x=0
    for i in range(0,len(l),self.columnas):
        self.m.append(l[i:i+self.columnas])
        x=x+1

  def __lt__(self,otro):
        if self.columnas==otro.columnas and self.filas==otro.filas:
                x=0
                for i in range(self.filas):
                        for j in range(self.columnas):
                                if self.m[i][j]<otro.m[i][j]:
                                     x=x+1
                if x>((self.columnas*self.filas)/2)+1:
                        return True
                else:
                        return False
        return 'No se puede comparar Matrises de diferente tamaño'
  def mostrar_matriz(self):
    for i in range(self.filas):
      for j in range(self.columnas):
        print(self.m[i][j], end='\t')
      print()
  def __add__(self,otro):
        if self.columnas==otro.columnas and self.filas==otro.filas:
                l=[]
                x=0
                for k in range(self.columnas*self.filas):
                     l.append(x)
                for i in range(self.filas):
                        for j in range(self.columnas):
                                num=otro.m[i][j]+self.m[i][j]
                                l[x]=num
                                m2=matriz(self.columnas,self.filas,l)
                                x=x+1
                return m2
        return 'Sintax error'

def main():
  m1 = matriz(6,2,[1,2,3,4,5,6,7,8,9,10,11,12])
  m2 = matriz(6,2,[1,1,1,1,1,1,1,1,1,1,1,1])
  sumadematricez=m1+m2
  sumadematricez.mostrar_matriz()
main()
