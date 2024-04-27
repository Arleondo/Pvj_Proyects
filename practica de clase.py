class persona:
    def __init__(self,n,e):
        self.Nombre=n
        self.Edad=e
    def __str__(self):
        return self.Nombre+' de edad: '+str(self.Edad)
    def __gt__(self,otro):
        if self.Edad>otro.Edad :
            return True
        else:
            return False

class estudiante(persona):
    def __init__(self,n,e,g,no):
        super().__init__(n,e)
        self.nota=no
        self.grado=g
    def __str__(self):
        return super().__str__()+' de grado: '+str(self.grado)+' con nota: '+str(self.nota)+'.'

class docente(persona):
    def __init__(self,n,e,c,h):
        super().__init__(n,e)
        self.cargo=c
        self.horas=h
    def __str__(self):
        return super().__str__()+' de cargo: '+self.cargo+' la cual tiene '+str(self.horas)+ ' horas trabajadas.'
    

class Administrador(persona):
    def __init__(self,n,e,a):
        super().__init__(n,e)
        self.area=a
    def __str__(self):
        return super().__str__()+' del area: '+self.area

def main():
    p1= estudiante("Arnol",18,'3ro',19)
    p2= docente('Graciela',36,'Profesora de Programacion',48)
    p3= Administrador('Jose',42,'Ciencias de la Computacion')
    resul= p2>p1
    print(resul)
    print('El estudiante '+p1.__str__()+'\n'+'Es estudiante de '+p2.__str__()+'\n'+'Lo cual significa que el/la'+p3.__str__()+'es su superior')
main()
