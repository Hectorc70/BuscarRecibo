from tkinter.filedialog import askdirectory
from os.path import splitext

from PyPDF2 import PdfFileReader


from rutas import Rutas, unir_cadenas, comprobar_rutas
from buscador import Buscador
from txt import ArchivoTxt


PATRONES = ['CONTROL: [0123456789]{8}', 'PERIODO:[0123456789]{2}/[0123456789]{4}']

def depurar_rutas(ruta_archivo_pdf):
	rutas_pdf = list()

	rutas = Rutas()
	rutas = rutas.recuperar_rutas(ruta_archivo_pdf, True)
	
	for ruta in rutas:
		tipo_archivo = splitext(ruta[-1])[-1]

		if tipo_archivo == '.pdf':
			ruta_completa = unir_cadenas('\\', ruta)
			rutas_pdf.append(ruta_completa)
	
	return rutas_pdf


class ArchivoPdfLectura():

	def __init__(self, rutas):	
		
		self.rutas_pdf = depurar_rutas(rutas)
		
	
	def escribir_pdf(self):
		

	def leer_pdf(self, metadatos=True):
		"""Lee archivo pdf"""	
		
		datos_hoja = list()

		for archivo in self.rutas_pdf:				
			self.lectura =PdfFileReader(archivo,'rb')
			paginas = self.lectura.numPages
			datos =  self.extraer_contenido(paginas, self.lectura, archivo, PATRONES)

			datos_hoja.append(datos)
		
		if metadatos:
			return datos_hoja
		
		else: 
			pass
			
	
	def extraer_contenido(self, paginas, pdf_leido, ruta_archivo, patrones):
		"""Retorna el contenido por hoja del Archivo PDF,
			el numero de pagina, la ruta del archivo"""

		
		datos_pag = dict()

			
		for pagina in range(paginas):
			if pdf_leido.isEncrypted:
				self.lectura_encriptada(pdf_leido, pagina)				

			else:
				pagina_lect = pdf_leido.getPage(pagina)
				pdf_texto = pagina_lect.extractText()	
				pag = pagina+1

				buscar = self.buscar_texto(patrones, pdf_texto)
				
				datos_pag[buscar[0]] = 	[pag, buscar[1], ruta_archivo]
		
		return datos_pag


	def buscar_texto(self, patrones, contenido_pdf):
		"""retorna la palabra pasada por parametro"""
		
		self.extraer_texto   = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]	

		texto = list()
	
		for patron in patrones:

			buscador 		 = Buscador(patron, contenido_pdf)
			posiciones 		 = buscador.buscar()			 			
			texto_encontrado = self.extraer_texto(posiciones[0], posiciones[1], contenido_pdf)

			texto.append(texto_encontrado)
		
		return texto

	def escribir_datos()
		ruta_txt = 'C\\RECIBOS_METADOS\\metadatos.txt'
		comprobar_ruta = comprobar_rutas(ruta_txt)
		

		if comprobar_ruta:
			continue
		else:
			pedir
		
		txt = ArchivoTxt(ruta_txt)
		

		
		contenido_txt = txt.leer()

		for linea in contenido_txt:
			recibos_empleado = linea.split('|')
			control 		 = linea.split('|')[0]


	

	
	def comprobar_empleado(self):
		datos_pdf = self.leer_pdf()

		for dato_pdf in datos_pdf:



	
	

	


	





			
			
		
									
	def lectura_encriptada(self, archivo, pag):

		archivo.decrypt('')
		pagina = archivo.getPage(pag)
		pdftext = pagina.extractText()
		self.contenido.append(pdftext)



pdf = ArchivoPdfLectura(askdirectory())
pdf.leer_pdf()