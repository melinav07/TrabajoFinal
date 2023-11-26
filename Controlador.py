from PyQt5.QtWidgets import QApplication
import sys
from Vista import *
from Modelo import sistema

class Coordinador(object):
    def __init__(self,vista,sistema):
        self.__mi_vista=vista
        self.__mi_sistema=sistema

    def datos_slide1(self, valor1):
        dato1=self.__mi_sistema.ampliarSenal(valor1)
        return dato1
    
    def datos_slide2(self, valor2):
        dato2=self.__mi_sistema.frecuenciaSenal(valor2)
        return dato2
    
    def datos_slide3(self, valor3):
        dato3=self.__mi_sistema.ampliarSenal1(valor3)
        return dato3
    
    def datos_slide4(self, valor4):
        dato4=self.__mi_sistema.frecuenciaSenal1(valor4)
        return dato4
    
    def datos_slide5(self, valor5):
        dato5=self.__mi_sistema.ampliarSenal2(valor5)
        return dato5
    
    def datos_slide6(self, valor6):
        dato6=self.__mi_sistema.frecuenciaSenal2(valor6)
        return dato6

class Principal(object):
    def __init__(self):        
        self.__app=QApplication(sys.argv)
        self.__mi_vista=Menu()
        self.__mi_sistema=sistema()
        self.__mi_controlador=Coordinador(self.__mi_vista,self.__mi_sistema)
        self.__mi_vista.asignarControlador(self.__mi_controlador)

    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())  

p=Principal()
p.main()