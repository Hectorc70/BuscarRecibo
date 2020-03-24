from ui import *

from metadatos.escritura import EscrituraMetadatos





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):   
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ejecutar()
        

        

    def ejecutar(self):
        self.boton_start_2.clicked.connect(self.ejecutar_creacion_metadatos)


    def ejecutar_creacion_metadatos(self):
        ruta_carpeta = self.carpeta_input.text()

        metadatos = EscrituraMetadatos(ruta_carpeta)
        metadatos.comparacion()

        print("Terminada la escritura de metadatos")



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()