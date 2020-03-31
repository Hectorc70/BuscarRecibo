<<<<<<< HEAD
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QThread

from metadatos.escritura import EscrituraMetadatos
from metadatos.recibo_pdf import ReciboPDF
from ui import *


class EscribirMdatos(QThread):
	def __init__(self, ruta):
		super().__init__()
		self.ruta = ruta


	def run(self):		
		metadatos = EscrituraMetadatos(self.ruta )
		metadatos.comparacion()

class BuscarRecibo(QThread):
	def __init__(self, control, ruta_destino, periodos, annos):
		super().__init__()
		self.control = control
		self.ruta_destino = ruta_destino
		self.periodos = periodos
		self.annos = annos


	def run(self):		
		recibos = ReciboPDF(self.control, self.ruta_destino,
							self.periodos, self.annos
							)
		recibos.buscar_control()
=======
from ui import *

from metadatos.escritura import EscrituraMetadatos
>>>>>>> master



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):   
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.ejecutar()
		

		

	def ejecutar(self):
		self.boton_start_mt.clicked.connect(self.ejecutar_creacion_metadatos)
		self.boton_start.clicked.connect(self.ejecutar_busqueda_recibos)


	def ejecutar_creacion_metadatos(self):
		ruta_carpeta = self.carpeta_input.text()

		self.escribir_mt = EscribirMdatos(ruta_carpeta)		
		self.escribir_mt.finished.connect(self.eliminar_hilo_ecribir)
		self.escribir_mt.start()
		
	
	def ejecutar_busqueda_recibos(self):		
		periodo_ini = int(self.periodo_inicial.text())
		periodo_fin = int(self.periodo_final.text())
		anno_ini    = (self.sb_a_ini.value())
		anno_fin    = self.sb_a_fin.value()

		control     = self.control_input.text()
		periodos    = [str(periodo_ini), str(periodo_fin)]
		annos       = [anno_ini, anno_fin]
		ruta_salida = self.ruta_destino_input.text()

<<<<<<< HEAD
		recibos = ReciboPDF(control, ruta_salida,
							periodos, annos
							)
		recibos.comparacion()
=======
        metadatos = EscrituraMetadatos(ruta_carpeta)
        metadatos.comparacion()
>>>>>>> master


		
	def eliminar_hilo_ecribir(self):
		print("---EJECUCION TERMINADA----")
		del self.escribir_mt
	def eliminar_hilo_buscar(self):
		print("---EJECUCION TERMINADA----")
		del self.buscar_reci

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()