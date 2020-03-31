import os
from os.path import splitext
import sys
sys.path.append('..')

from modelos_principales.rutas import Rutas, unir_cadenas, dividir_cadena
from modelos_principales.pdf import ArchivoPDF
from almacenar.ayuda.buscador import Buscador

PERIODOS = ['01','02','03','04','05','06','07','08','09','10','11',
			'12','13','14','15','16','17','18','19','20','21','22','23','24'
			]

class ReciboPDF:
	
	def __init__(self, ruta_base):
		self.ruta_base = ruta_base
		self.rutas     = self.depurar_rutas()
		self.patrones  = ['CONTROL: [0123456789]{8}', 'PERIODO:[0123456789]{2}/[0123456789]{4}']


	def depurar_rutas(self):

		rutas_pdf = list()
		rutas = Rutas()
		rutas = rutas.recuperar_rutas(self.ruta_base, True)
		ruta_base_num = len(self.ruta_base.split('\\'))
	

		for ruta in rutas:

			tipo_archivo = splitext(ruta[-1])[-1]
			if tipo_archivo == '.pdf':
				per = ruta[ruta_base_num].split('_')[0]
				carp_reci = ruta[ruta_base_num+3]

				if per in PERIODOS and carp_reci == 'RECIBOS':		
					ruta_completa = unir_cadenas('\\', ruta)
					rutas_pdf.append(ruta_completa)
		
		return rutas_pdf

	def retornar_datos(self):
		for archivo in self.rutas:

			pdf = ArchivoPDF(archivo)
			contenido = pdf.extraer_contenido()
			self.buscar_patron(self.patrones, contenido, archivo)
	
	
	
	def buscar_patron(self, patrones, paginas, archivo):

		self.extraer_texto   = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]	
		self.archivo = archivo

		texto = list()
		
		
		texto_encontrado = None
		for pagina, contenido_pdf in paginas.items():
		
			for patron in patrones:
			
				
				buscador 		 = Buscador(patron, contenido_pdf)
				posiciones 		 = buscador.buscar()

				if len(posiciones) < 2:
					buscador 		 = Buscador('PERIODO:[0123456789]{1}/[0123456789]{4}', contenido_pdf)
					posiciones 		 = buscador.buscar()
				
					if len(posiciones) < 2:
						continue
					
			
						texto_encontrado = self.extraer_texto(posiciones[0], posiciones[1], contenido_pdf)
			
				
				texto.append(texto_encontrado)
			
			linea = self.armar_texto(texto[0], texto[1], pagina, self.archivo)

			return linea
				
	def armar_texto(self, ctrl_text, per_txt, pagina, ruta):
		linea = dict()
		control = dividir_cadena('|', str(ctrl_text))
		periodo = dividir_cadena('|', str(per_txt))

		llave = control[-1] + '|' + periodo[-1] + '|' + str(pagina)
		
		linea[llave] = ruta
		
		return linea
