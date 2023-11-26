# Importar librerias básicas
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog
from PyQt5.uic import loadUi;
import numpy as np
from scipy.signal import sawtooth, square

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt,QRegExp, QTimer, QDate, QTime


class Menu(QMainWindow):
    #constructor
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('menu.ui',self)
        self.setup()

    #metodo para configurar las senales-slots y otros de la interfaz
    def setup(self):
        #se programa la senal para el boton
        self.seno_push.clicked.connect(self.graficarseno)
        self.cuadrada_push.clicked.connect(self.graficarcuadrada)
        self.diente_push.clicked.connect(self.graficardiente)
    
    def graficarseno(self):
        ventana_Seno=VentanaSeno(self)
        self.hide()
        ventana_Seno.show()

    def graficarcuadrada(self):
        ventana_cuadrada=Cuadrada(self)
        self.hide()
        ventana_cuadrada.show()

    def graficardiente(self):
        ventana_diente=Diente(self)
        self.hide()
        ventana_diente.show()
    
    def asignarControlador(self,control):
        self.__miControlador = control
    
    def recb_datos1(self,a):
        self.nivel1=self.__miControlador.datos_slide1(a)
        self.recibirvalor1(self.nivel1)

    def recibirvalor1(self,p):
        return p
    
    def recb_datos2(self,a):
        self.nivel2=self.__miControlador.datos_slide2(a)
        self.recibirvalor2(self.nivel2)

    def recibirvalor2(self,p):
        return p
    
    def recb_datos3(self,a):
        self.nivel3=self.__miControlador.datos_slide3(a)
        self.recibirvalor3(self.nivel4)

    def recibirvalor3(self,p):
        return p
    

    def recb_datos4(self,a):
        self.nivel4=self.__miControlador.datos_slide4(a)
        self.recibirvalor4(self.nivel4)

    def recibirvalor4(self,p):
        return p
    
    def recb_datos5(self,a):
        self.nivel5=self.__miControlador.datos_slide5(a)
        self.recibirvalor5(self.nivel5)

    def recibirvalor5(self,p):
        return p
    
    def recb_datos6(self,a):
        self.nivel6=self.__miControlador.datos_slide6(a)
        self.recibirvalor6(self.nivel6)

    def recibirvalor6(self,p):
        return p
    
class VentanaSeno(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('SENO.ui',self)
        self.__VentanaPadre = ppal
        self.setup()
        current_date = QDate.currentDate()
        self.dateEdit.setDate(current_date)
        current_time = QTime.currentTime()
        self.timeEdit.setTime(current_time)

        # Desactivar la edición manual
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.timeEdit.setDisplayFormat("hh:mm:ss")

    def setup(self):
        self.grafica=SSeno()
        self.verticalLayout.addWidget(self.grafica)
        self.pushButton_3.clicked.connect(self.cerrar)
        self.Slider1.valueChanged.connect(self.slider_uno)
        self.Slider2.valueChanged.connect(self.slider_dos)
        self.dateEdit.dateChanged.connect(self.mostrar_fecha_seleccionada)
        self.timeEdit.timeChanged.connect(self.mostrar_hora_seleccionada)
    
    def mostrar_fecha_seleccionada(self, date):
        # Método que se llama cuando cambia la fecha seleccionada
        return date.toString('yyyy-MM-dd')

    def mostrar_hora_seleccionada(self, time):
        # Método que se llama cuando cambia la hora seleccionada
        return time.toString('hh:mm:ss')
    
    def slider_uno(self, event):
        valor1 = self.__VentanaPadre.recibirvalor1(event)
        self.grafica.datos1(valor1)

    def slider_dos(self, event):
        valor2 = self.__VentanaPadre.recibirvalor2(event)
        self.grafica.datos2(valor2) 

    def cerrar(self):
        self.close() 
        self.__VentanaPadre.show()
    
class SSeno(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(facecolor='black')
        super().__init__(self.fig)
        self.ax.set_facecolor('black')
        self.ax.grid()
        self.ax.margins(x=0)
        self.nivel1 = 10
        self.nivel2 = 1
        self.grafica_datoss()

    def datos1(self,c):
        self.nivel1 = c

    def datos2(self,c):
        self.nivel2 = c

    def grafica_datoss(self):
        plt.title("Grafica en PyQt5 con Matplotlib")
        x = np.arange(-np.pi, 8*np.pi, 0.01) 
        line, = self.ax.plot(x,self.nivel1*np.sin(self.nivel2*x), color='r',linewidth=2)
        self.draw()     
        line.set_ydata(np.sin(x)+24)
        QTimer.singleShot(10, self.grafica_datoss)

class Cuadrada(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('CUADRADA.ui',self)
        self.__VentanaPadre = ppal
        self.setup()
        current_date = QDate.currentDate()
        self.dateEdit.setDate(current_date)
        current_time = QTime.currentTime()
        self.timeEdit.setTime(current_time)

        # Desactivar la edición manual
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.timeEdit.setDisplayFormat("hh:mm:ss")

    def setup(self):
        self.graficac=SCuadrada()
        self.verticalLayout.addWidget(self.graficac)
        self.pushButton_3.clicked.connect(self.cerrar)
        self.Slider3.valueChanged.connect(self.slider_tres)
        self.Slider4.valueChanged.connect(self.slider_cuatro)
        self.dateEdit.dateChanged.connect(self.mostrar_fecha_seleccionada)
        self.timeEdit.timeChanged.connect(self.mostrar_hora_seleccionada)
    
    def mostrar_fecha_seleccionada(self, date):
        # Método que se llama cuando cambia la fecha seleccionada
        return date.toString('yyyy-MM-dd')

    def mostrar_hora_seleccionada(self, time):
        # Método que se llama cuando cambia la hora seleccionada
        return time.toString('hh:mm:ss')

    def slider_tres(self, event):
        valor3 = self.__VentanaPadre.recibirvalor3(event)
        self.graficac.datos3(valor3)

    def slider_cuatro(self, event):
        valor4 = self.__VentanaPadre.recibirvalor4(event)
        self.graficac.datos4(valor4)     

    def cerrar(self):
        self.close() 
        self.__VentanaPadre.show()
    
class SCuadrada(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(facecolor='black')
        super().__init__(self.fig)
        self.ax.set_facecolor('black')
        self.ax.grid()
        self.ax.margins(x=0)
        self.nivel3 = 10
        self.nivel4 = 1
        self.grafica_datosc()

    def datos3(self,c):
            self.nivel3 = c

    def datos4(self,c):
        self.nivel4 = c

    def grafica_datosc(self):
        plt.title("Señal Cuadrada en PyQt5 con Matplotlib")
        x = np.arange(-np.pi, (1/2)*np.pi, 0.01)
        y = self.nivel3 * np.sign(np.sin(x * (2 * np.pi *self.nivel4)))
        line, = self.ax.plot(x, y, color='b', linewidth=2)
        self.draw()
        line.set_ydata(np.sign(np.sin(x))+10)
        QTimer.singleShot(10, self.grafica_datosc)
    
    def cerrar(self):
        self.close() 
        self.__VentanaPadre.show()
    
class Diente(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('DIENTE.ui',self)
        self.__VentanaPadre = ppal
        self.setup()
        current_date = QDate.currentDate()
        self.dateEdit.setDate(current_date)
        current_time = QTime.currentTime()
        self.timeEdit.setTime(current_time)

        # Desactivar la edición manual
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.timeEdit.setDisplayFormat("hh:mm:ss")
    
    def setup(self):
        self.graficad=Sierra()
        self.verticalLayout.addWidget(self.graficad)
        self.pushButton_3.clicked.connect(self.cerrar)
        self.Slider5.valueChanged.connect(self.slider_cinco)
        self.Slider6.valueChanged.connect(self.slider_seis)
        self.dateEdit.dateChanged.connect(self.mostrar_fecha_seleccionada)
        self.timeEdit.timeChanged.connect(self.mostrar_hora_seleccionada)

    def mostrar_fecha_seleccionada(self, date):
        # Método que se llama cuando cambia la fecha seleccionada
        return date.toString('yyyy-MM-dd')

    def mostrar_hora_seleccionada(self, time):
        # Método que se llama cuando cambia la hora seleccionada
        return time.toString('hh:mm:ss')
    
    def slider_cinco(self, event):
        valor5 = self.__VentanaPadre.recibirvalor5(event)
        self.graficad.datos5(valor5)

    def slider_seis(self, event):
        valor6 = self.__VentanaPadre.recibirvalor6(event)
        self.graficad.datos6(valor6) 
         
    def cerrar(self):
        self.close() 
        self.__VentanaPadre.show()

class Sierra(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig, self.ax = plt.subplots(facecolor='black')
        super().__init__(self.fig)
        
        self.ax.set_facecolor('black')
        self.ax.grid()
        self.ax.margins(x=0)
        self.nivel5 = 10
        self.nivel6 = 1
        self.grafica_datosd()

    def datos5(self,c):
            self.nivel5 = c

    def datos6(self,c):
        self.nivel6 = c

    def grafica_datosd(self):
        plt.title("Grafica en PyQt5 con Matplotlib - Diente de Sierra")
        x = np.arange(-np.pi, 14*np.pi, 0.01) 
        y= self.nivel5 * sawtooth(self.nivel6 * x)
        line, = self.ax.plot(x, y, color='g', linewidth=2)
        self.draw()     
        line.set_ydata(sawtooth(x))
        QTimer.singleShot(10, self.grafica_datosd)




