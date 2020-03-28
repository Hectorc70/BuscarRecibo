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

        self.armar_per  = ArmarPeriodos()
    
    def comparacion(self):
        datos_input = self.armar_clave_input()
        metadatos   = self.datos_empleado()

        for periodo_input in datos_input.keys():
            if periodo_input in metadatos.keys():
                datos = metadatos[periodo_input]
                datos_div = dividir_cadena('|', datos)               
                ruta = datos_div[0].strip('\n')

                pagina = datos_div[1]


                self.extraer_hoja(ruta, pagina )
            else:
                pass
        

    
    def extraer_hoja(self, ruta, pagina):

        

        pdf_original =PdfFileReader(ruta,'rb')
        pdf_nuevo = PdfFileWriter()
        pdf_nuevo.addPage(pdf_original.getPage(int(pagina)))
        
        self.guardar_archivo(self.ruta_destino, pdf_nuevo)


    def guardar_archivo(self, ruta, pdf):  
        nombre_archivo = ruta + '\\'+ "prueba.pdf"
        with open(nombre_archivo,'wb') as fp: 
            pdf.write(fp)

        


    def armar_clave_input(self):

        periodos_intermedios = None        
        todos_los_periodos = list()
        

        if self.annos[0] != self.annos[1] and self.annos[0]+1 != self.annos[1]:
            periodos_intermedios = self.recuperar_periodos_intermedios()
        
        elif self.annos[0] == self.annos[1]:

            periodos= self.armar_per.armar_periodos(self.annos[0], self.periodo_ini,
                                                    int(self.periodo_fin)+1
                                                    )
            todos_los_periodos.append(periodos)        
        else:                                           
            periodos_iniciales = self.armar_per.armar_periodos(self.annos[0], 
                                                                self.periodo_ini,25
                                                                )
            periodos_finales   = self.armar_per.armar_periodos(self.annos[1], 1, 
                                                                int(self.periodo_fin)+1
                                                                )
            todos_los_periodos.append(periodos_iniciales)
            todos_los_periodos.append(periodos_finales)
        
        
        if periodos_intermedios != None: 
            
            for periodos in periodos_intermedios:

                todos_los_periodos.append(periodos)
           
            

            
        
        datos_empleado_input = dict()
        for anno in todos_los_periodos:
            for anno_clave, periodos in anno.items():
                for periodo in periodos:
                    control = int(self.control)
                    clave = str(control) + '|' + str(periodo)+ '|' + str(anno_clave)

                    datos_empleado_input[clave] = ' '
        
        return datos_empleado_input
        

    def recuperar_periodos_intermedios(self):
        """Retorna los periodos de los años intermedios"""

        annoos_intermedios = self.armar_per.armar_years(self.annos)
        periodos_intermedios = list()

        for anno_inter in annoos_intermedios:
            intermedios = self.armar_per.armar_periodos(anno_inter, 1,25)

            periodos_intermedios.append(intermedios)

        return periodos_intermedios         

        
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
    
    






class ArmarPeriodos():

    def __init__(self):
        pass

    def armar_years(self, datos):
        """Retorna los años intermedios
            entre el año de inicio y el año final"""


        annos_intermedios = list()

        inicio = datos[0]
        fin    = datos[1]

        intermedio = inicio

        while intermedio != fin:
            intermedio = intermedio+1
            if intermedio == fin:
                break

            annos_intermedios.append(intermedio)

        
        
        
        
        return annos_intermedios

    def armar_periodos(self, anno, periodo_i, periodo_f):        
        periodos_anno = dict()
        periodos = list()
        
        
        for per in range(int(periodo_i), int(periodo_f)):
            
            if per == 23:
                periodos.append(str(per)+'-AGUI')
            
            periodos.append(per)


        periodos_anno[anno]= periodos

        return periodos_anno

    
        


