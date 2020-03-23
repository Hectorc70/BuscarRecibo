from txt import ArchivoTxt
from rutas import dividir_cadena


class ArchivoMetadatos(ArchivoTxt):

	def __init__(self, archivo):
		super().__init__(archivo)

	def leer(self):

		empleado = dict()			
		
		txt = ArchivoTxt(self.ruta_archivo)
		contenido_txt = txt.leer()

		for linea in contenido_txt:									
			linea_div = dividir_cadena('|', linea)			
			control = linea_div[0]	
			linea_div.remove(control)

			datos_periodos = self.separar_periodos(linea_div)

			empleado[control] = datos_periodos
		
		return empleado
			



	def separar_periodos(self, periodos_datos):
		self.periodo = dict()

		for recibo in periodos_datos:
			if recibo == '\n':
				continue

			recibos = dividir_cadena('-', recibo)
			
			pagina = recibos[0]
			periodo = recibos[1]
			ruta = recibos[2]
			
			self.periodo[periodo+pagina] = [ruta]
		
		return self.periodo



		