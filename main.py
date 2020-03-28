from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QThread

from metadatos.escritura import EscrituraMetadatos
from ui import *


class EscribirMdatos(QThread):
	def __init__(self, ruta):
		super().__init__()
		self.ruta = ruta


	def run(self):		
		metadatos = EscrituraMetadatos(self.ruta )
		metadatos.comparacion()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):   
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.ejecutar()
		

		

	def ejecutar(self):
		self.boton_start_2.clicked.connect(self.ejecutar_creacion_metadatos)


	def ejecutar_creacion_metadatos(self):
		ruta_carpeta = self.carpeta_input.text()

		self.escribir_mt = EscribirMdatos(ruta_carpeta)		
		self.escribir_mt.finished.connect(self.eliminar_hilo)
		self.escribir_mt.start()
		

		
	def eliminar_hilo(self):
		print("Terminada la escritura de metadatos")
		del self.escribir_mt

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()