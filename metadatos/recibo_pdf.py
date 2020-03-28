from tkinter.filedialog import askdirectory, asksaveasfilename

from PyPDF2 import PdfFileReader, PdfFileWriter

from metadatos.ayuda.lectura_metadatos import ArchivoMetadatos
from metadatos.ayuda.txt import ArchivoTxt
from metadatos.ayuda.rutas import dividir_cadena, unir_cadenas


PERIODOS = ['1','2','3','4','5','6','7','8','9','10','11',
			'12','13','14','15','16','17','18','19','20','21','22','23','24'
			]


class ReciboPDF:

    def __init__(self, control,ruta_destino, periodos, annos):
        """Recupera Recibos en pdf de empleados"""
        self.control      = control
        self.ruta_destino = ruta_destino
        self.periodo_ini  = periodos[0]
        self.periodo_fin  = periodos[1]
        self.annos        = annos
    
       

    def armar_clave_input(self):
        periodos_iniciales = self.armar_periodos(self.annos[0], self.periodo_ini, 25)
        periodos_finales = self.armar_periodos(self.annos[1], 1, int(self.periodo_fin))                                         
       
        empleados  = self.datos_empleado()
        for anno in self.annos:
            for periodo in range(int(self.periodo_ini), int(self.periodo_fin)+1):
            
                clave = self.control + '|' + str(periodo)+ '|' + anno + '|'

        

            

        
    def datos_empleado(self):
        archivo_mtd = ArchivoMetadatos('C:\\RECIBOS_METADATOS\\metadatos.txt')
        empleados = archivo_mtd.leer()

        datos_empleado_format = dict()

        for empleado, ruta in empleados.items():
            empleado_datos = dividir_cadena('|', empleado)

            control   = int(empleado_datos[0].split(' ')[-1])
            periodo_a = empleado_datos[1].split(':')[-1]
            periodo   = int(periodo_a.split('/')[0])
            anno      = periodo_a.split('/')[-1]
            pagina    = empleado_datos[2]
            
            clave = str(control) + '|' + str(periodo) + '|' + anno
            datos_empleado_format[clave] = ruta + '|' + pagina

        return datos_empleado_format
            

            









    def extraer_hoja(self):

        ruta_pdf = self.datos_pdf[0]
        pagina   = self.datos_pdf[1]

        pdf_original =PdfFileReader(ruta_pdf,'rb')
        pdf_nuevo = PdfFileWriter()
        pdf_nuevo.addPage(pdf_original.getPage(pagina))
        
        self.guardar_archivo(self.ruta_destino, pdf_nuevo)



    def guardar_archivo(self, nombre, pdf):
        nombre_archivo = ""
        #ruta_pdf_nuevo = ruta + 'new'

        pdf.write(ruta)


    def armar_periodos(self, anno, periodo_i, periodo_f):        
        periodos_año = dict()
        periodos = list()
        
        #PERIODOS INICIALES
        for per in range(int(periodo_i), periodo_f):
            
            if per == 23:
                periodos.append(str(per)+'-AGUI')
            
            periodos.append(per)


        periodos_año[anno]= periodos

        return periodos_año