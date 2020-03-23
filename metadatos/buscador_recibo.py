from tkinter.filedialog import askdirectory


from ayuda.rutas import Rutas

class ArchivoMDatos:
    def __init__(self, control, ruta ):

        self.control    = control
        self.ruta       = ruta

        rutas           = Rutas()
        self.rutas_archivos  = rutas.recuperar_rutas(self.ruta)

    def leer_archivo(self):
        datos_de_busqueda = list()

        for archivo in self.rutas_archivos:

            archivo_metadatos = open(archivo, "r")
            lineas            = archivo_metadatos.readlines()            

            for empleado in lineas:
                control = empleado.split("|")[0].split(" ")[-1]
                
                if control == self.control:
                    linea_empleado = empleado.split('--')
               
                periodo = linea_empleado.split("|")[1].split(":")[-1].split("/")[0]
                pagina   = linea_empleado.split("|")[2]
                ruta     = linea_empleado.split("|")[4]

                           
                   return ruta, pagina                     

                    
                

           

