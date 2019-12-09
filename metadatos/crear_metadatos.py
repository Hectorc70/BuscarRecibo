import PyPDF2

from ayuda.archivo_datos import crear_archivo_txt



class Archivo_Pdf:

	def __init__(self):
		self.nombre = "201916.pdf"
		self.ruta   = None

	def leer_pdf(self):

		lectura = PyPDF2.PdfFileReader(self.nombre,'rb')

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

	def buscar

a= Archivo_Pdf()
a.leer_pdf()