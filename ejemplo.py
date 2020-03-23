
from ui import *
from copiar.comandos import Consola


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ejecutar()
        

    def ejecutar(self):       
        
        self.boton_start.clicked.connect(self.opciones_ventana)     

        
           
        
        
        
        

    def opciones_ventana(self):
        ruta_1 = self.ruta_origen.text()
        ruta_2 = self.ruta_destino.text()
        parametros = self.parametros()

        consola = Consola()
        consola.comando(ruta_1, ruta_2, parametros) 

        
        
    def parametros(self):

        parametros = list()

       
        if self.copiar.isChecked():
            pass
        if self.copiar_subdirectorios.isChecked():
            parametros.append("/E")
        
        if self.crear_log.isChecked():
            parametros.append("/LOG:")
        
        if self.mover.isChecked(): 
            parametros.append("/MOVE")
           
        
        hilos_trabajo = '/MT:' + str(self.numero_hilos.value())
        info_detall = '/V'

        parametros.append(hilos_trabajo)
        parametros.append(info_detall)
        
        return parametros

   




        
        

        
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()