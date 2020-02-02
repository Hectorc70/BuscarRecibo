

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


		self.contenido_pag = dict()
		self.ruta_templeado = dict()
		for archivo in self.rutas_pdf:

			tipo_empleado = self.tipo_de_empleado(archivo)		
			self.lectura = PyPDF2.PdfFileReader(archivo,'rb')
			paginas = self.lectura.numPages
			
			for pagina in range(paginas):
				if self.lectura.isEncrypted:
					self.lectura_encriptada(self.lectura, pagina)				

				else:
					pagina_lect = self.lectura.getPage(pagina)
					pdftext = pagina_lect.extractText()	
					pag = pagina+1
					self.contenido_pag[pdftext] = [tipo_empleado, pag, archivo]	#Almacena el contenido y la pagina
				
				
	
	def extraer_no_control(self):
		"""busca el Numero de control y lo
		   extrae del pdf"""

		self.leer_pdf()
		datos_pdf_extract = list()
		
		for contenido, datos in self.contenido_pag.items():													
			tipo_empleado = str(datos[0])
			pagina 		  = str(datos[1])
			ruta		  = str(datos[2])

			periodo = self.extraer_periodo(contenido)
			print(contenido)
			patron 			= 'CONTROL: [0123456789]{8}'
			buscador 		= Buscador(patron, contenido)
			posiciones 		= buscador.buscar()			 			
			texto			= self.extraer_texto(posiciones[0], posiciones[1], contenido) 

			datos_pdf_extract = texto + "|"+ periodo + "|" + pagina + "|" + tipo_empleado + "|" + ruta + "--"
			nombre_archivo    = "metadatos_" + tipo_empleado + ".txt"
			ArchivoTxt(datos_pdf_extract, nombre_archivo)

	def extraer_periodo(self, contenido):
			
		print(contenido)
		patron 			= 'PERIODO:[0123456789]{2}/[0123456789]{4}'
		buscador 		= Buscador(patron, contenido)
		posiciones 		= buscador.buscar()			 			
		texto = self.extraer_texto(posiciones[0], posiciones[1], contenido) 
			
		return texto
	


	def tipo_de_empleado(self, ruta):
		nombre_archivo = str(ruta.split("\\")[-1]).upper()

		if (nombre_archivo.split("_")[0] == 'CONFIANZA' or 
			nombre_archivo.split("_")[1] == 'CONFIANZA'
			):

			tipo_empleado = '1'
			return tipo_empleado
		elif (nombre_archivo.split("_")[0] == 'BASE' or 
				nombre_archivo.split("_")[1] == 'BASE'
			):

			tipo_empleado = '2'
			return tipo_empleado
		
		elif (nombre_archivo.split("_")[0] == 'BASE4' or 
				nombre_archivo.split("_")[1] == 'BASE4'
			):

			tipo_empleado = '4'
			return tipo_empleado
		

	




			
			
		
									
	def lectura_encriptada(self, archivo, pag):

		archivo.decrypt('')
		pagina = archivo.getPage(pag)
		pdftext = pagina.extractText()
		self.contenido.append(pdftext)

		

	