

import PyPDF2
import re

from metadatos.ayuda.archivo_datos import crear_archivo_txt
from metadatos.ayuda.rutas import Rutas



class Archivo_Pdf(Rutas):

	def __init__(self, buscar):
		
		self.ruta   = buscar

		Rutas.__init__(self, self.ruta)

	def leer_pdf(self):

		for archivo in self.rutas_pdf:

			lectura = PyPDF2.PdfFileReader(archivo,'rb')

			if lectura.isEncrypted:

				lectura.decrypt('')
				pagina = lectura.getPage(0)
				pdftext = pagina.extractText()
				print(pdftext)

			else:
				pagina = lectura.getPage(0)
				pdftext = pagina.extractText()
				print(pdftext)
				crear_archivo_txt(pdftext)							#llena un txt de los datos del pdf

	def buscar_datos(self):


