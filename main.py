"""



from extractor.buscador_recibo import Recibo


def ejecutar(ruta):
    pdf = Archivo_Pdf(ruta)
    pdf.extraer_no_control()

def extraer_recibo():
    reci = Recibo("300596", "01", "2")
    reci.leer_archivo()
extraer_recibo()
#ejecutar(askdirectory())



"""

from ui import *

from metadatos.crear_metadatos import Archivo_Pdf





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):   
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ejecutar()
        

        

    def ejecutar(self):
        self.boton_start_2.clicked.connect(self.ejecutar_creacion_metadatos)


    def ejecutar_creacion_metadatos(self):
        ruta_carpeta = self.carpeta_input.text()

        pdf = Archivo_Pdf(ruta_carpeta)
        pdf.extraer_no_control()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()