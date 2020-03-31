from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger




class ArchivoPDF:
	"""CLASE QUE TRABAJA CON ARCHIVOS PDF, SE LE PASA COMO PARAMETRO UNA
		LA RUTA DE UN ARCHIVO PDF Y 
		EL MODO: puede ser 'lectura', 'escritura, 'modificar'"""

	def __init__(self, archivo):
		self.ruta_archivo  = archivo
		self.archivo_leido = self.leer_archivo()
		self.paginas       = self.archivo_leido.numPages
		
		
	def leer_archivo(self):
		"""Retorna el archivo leido pasando la ruta del archivo pdf"""
		self.lectura =PdfFileReader(self.ruta_archivo,'rb')

		return self.lectura

	def extraer_contenido(self):
		"""Retorna el contenido del PDF leido"""
		contenido_pdf = dict()

		for pagina in range(self.paginas):
			if self.archivo_leido.isEncrypted:
				print('Archivo Encriptado no se pudo leer')
				continue
			else:
				pagina_lect = self.archivo_leido.getPage(pagina)
				pdf_texto   = pagina_lect.extractText()
				pag = pagina+1

				contenido_pdf[pag] = pdf_texto
		
		return contenido_pdf

		
		

	def escribir(self):
		pass
	def modificar(self):
		pass

class ArchivoPDFEncrip(ArchivoPDF):
	pass

ruta = 'X:\\CFDI_NOMINA_2019\\01_2019\\ORDINARIA\\PDF\\RECIBOS\\Funcionarios_Cheques_201901.pdf'
pdf = ArchivoPDF(ruta)
pdf.extraer_contenido()
