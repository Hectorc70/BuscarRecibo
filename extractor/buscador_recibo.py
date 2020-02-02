

class Recibo:

    def __init__(self, control, periodos, t_empleado):

        self.control    = control
        self.periodos   = periodos
        self.t_empleado = t_empleado


    def abrir_metadatos(self):

        if self.t_empleado == '1': 
            archivo_metadatos = open("metadatos_1.txt", "r")
            lineas            = archivo_metadatos.readlines()
            return lineas
        elif self.t_empleado == '2':
            archivo_metadatos = open("metadatos_2.txt", "r")
            lineas            = archivo_metadatos.readlines()
            return lineas
        
        elif self.t_empleado == '4':
            archivo_metadatos = open("metadatos_3.txt", "r")
            lineas            = archivo_metadatos.readlines()
            return lineas

    def leer_archivo(self):

        datos = self.abrir_metadatos()

        for empleado in datos:
            control = empleado.split("|")[0].split(" ")[-1]
            periodo = empleado.split("|")[1].split(":")[-1].split("/")[-1]
            ruta    = empleado.split("|")[]
