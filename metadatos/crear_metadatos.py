

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
		"""busca el Numero de control y lo
		   extrae del pdf"""

		self.leer_pdf()
		datos_pdf_extract = list()
		
		for contenido in self.contenido:

			periodo = self.extraer_periodo(contenido)
			print(contenido)
			patron 			= 'CONTROL: [0123456789]{8}'
			buscador 		= Buscador(patron, contenido)
			posiciones 		= buscador.buscar()			 			
			texto = self.extraer_texto(posiciones[0], posiciones[1], contenido) 

			datos_pdf_extract = texto + "|"+ periodo

			ArchivoTxt(datos_pdf_extract)

	def extraer_periodo(self, contenido):
			
		print(contenido)
		patron 			= 'PERIODO:[0123456789]{2}/[0123456789]{4}'
		buscador 		= Buscador(patron, contenido)
		posiciones 		= buscador.buscar()			 			
		texto = self.extraer_texto(posiciones[0], posiciones[1], contenido) 
			
		return texto
	





			
			
		
									

	
		

	