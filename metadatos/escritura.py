<<<<<<< HEAD
from metadatos.ayuda.pdf import ArchivoPdfLectura
from metadatos.ayuda.lectura_metadatos import ArchivoMetadatos
from metadatos.ayuda.txt import ArchivoTxt
=======
from ayuda.pdf import ArchivoPdfLectura
from ayuda.lectura_metadatos import ArchivoMetadatos
from ayuda.txt import ArchivoTxt
>>>>>>> master

class EscrituraMetadatos:

	def __init__(self, directorio_de_recibos):

		
		pdf = ArchivoPdfLectura(directorio_de_recibos)
		self.datos_recibos = pdf.leer_pdf()

		txt = ArchivoMetadatos('C:\\RECIBOS_METADATOS\\metadatos.txt')
		self.datos_txt = txt.leer()

	def comparacion(self):
		"""Metodo Principal para la escritura de los nuevos metadatos,
	 		comparando primero si ya existe en el txt"""

		periodos_recibos = self.convertir_datos_recibos(self.datos_recibos)
			   
		for periodo, ruta in periodos_recibos.items():
			if periodo in self.datos_txt.keys():
				continue
		
			else:
				datos = periodo + '|' + ruta				
				self.escribir_metadatos(datos)

			
	def convertir_datos_recibos(self, datos):
		"""Convierte los datos obtenidos de los pdf
		a diccionarios retorna CONTROL|PERIDO|PAGINA:RUTA"""

		periodos_a_agregar = dict()
		for archivo in datos:
			for llave, datos in archivo.items():
				pagina  = str(datos[0])
				periodo = datos[1]
				ruta    = datos[2]
				llave_per = llave + '|' + periodo + '|' + pagina
				periodos_a_agregar[llave_per]= ruta

		return periodos_a_agregar

	def escribir_metadatos(self, datos):
		"""LLama a la calse ArchivoTXT para escribir en un 
			archivo txt los metadatos pasando
			 como parametro en 'Datos'"""


		archivo_metadatos = ArchivoTxt('C:\\RECIBOS_METADATOS\\metadatos.txt')
		archivo_metadatos.escribir(datos)

