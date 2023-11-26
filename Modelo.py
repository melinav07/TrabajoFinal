class sistema(object):
    def __init__(self):
       self.nivel1=10
       self.nivel2=10
       self.nivel3=10
       self.nivel4=10
       self.nivel5=10
       self.nivel6=10

    def ampliarSenal(self,valor1):
        self.nivel1 = valor1*0.1
        return self.nivel1

    def frecuenciaSenal(self, valor2):
        if  0 <= self.nivel2:
            self.nivel2 = valor2*0.05
        return self.nivel2
    
    def ampliarSenal1(self,valor3):
        self.nivel3 = valor3*0.1
        return self.nivel3

    def frecuenciaSenal1(self, valor4):
        self.nivel4 = valor4*0.05
        return self.nivel4
    
    def ampliarSenal2(self,valor5):
        self.nivel5 = valor5*0.1
        return self.nivel5

    def frecuenciaSenal2(self, valor6):
        self.nivel6 = valor6*0.05
        return self.nivel6