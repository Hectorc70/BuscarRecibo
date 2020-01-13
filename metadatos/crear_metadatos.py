

import PyPDF2


from metadatos.ayuda.archivo_datos import ArchivoTxt
from metadatos.ayuda.rutas import Rutas
from metadatos.ayuda.buscador import Buscador



class Archivo_Pdf(Rutas):

	def __init__(self, buscar):
		
		self.ruta   = buscar
		Rutas.__init__(self, self.ruta)
		self.extraer_texto   = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]	


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
	
	
	
	def extraer_no_control(self):
		"""busca datos y los almacena en un txt"""

		self.leer_pdf()
		for contenido in self.contenido:

			#periodo = self.extraer_periodo(contenido)

			print(contenido)
			patron 			= 'CONTROL: [0123456789]{8}'
			buscador 		= Buscador(patron, contenido)
			posiciones 		= buscador.buscar()			 			
			control = self.extraer_texto(posiciones[0], posiciones[1], contenido) 

			texto = control

			ArchivoTxt(texto)

	def extraer_periodo(self, contenido):

		for conte in contenido:
			
			print(conte)
			patron 			= 'PERIODO:01/2019'
			buscador 		= Buscador(patron, conte)
			posiciones 		= buscador.buscar()			 			
			texto = self.extraer_texto(posiciones[0], posiciones[1], conte) 
			
		return texto
	





			
			
		
									

	
		

	