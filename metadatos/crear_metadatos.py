

import PyPDF2


from metadatos.ayuda.archivo_datos import crear_archivo_txt
from metadatos.ayuda.rutas import Rutas
from metadatos.ayuda.buscador import Buscador



class Archivo_Pdf(Rutas):

	def __init__(self, buscar):
		
		self.ruta   = buscar
		Rutas.__init__(self, self.ruta)
				
	def leer_pdf(self):
		"""Lee archivo pdf y extrae su contenido"""


		self.contenido = list()
		for archivo in self.rutas_pdf:
			
			lectura = PyPDF2.PdfFileReader(archivo,'rb')

			if lectura.isEncrypted:

				lectura.decrypt('')
				pagina = lectura.getPage(0)
				pdftext = pagina.extractText()
				self.contenido.append(pdftext)

			else:
				pagina = lectura.getPage(0)
				pdftext = pagina.extractText()	
				self.contenido.append(pdftext)
	
	
	
	def crear_metadatos(self):
		"""busca datos y los almacena en un txt"""

		self.leer_pdf()
		for contenido in self.contenido:
			
			print(contenido)
			patron = 'CONTROL: [0123456789]{8}'
			buscador = Buscador(patron, contenido)
			posiciones = buscador.buscar()			#llama la funcion que devuelve la poscion del texto
			

	


			
			
		
									

	
		

	