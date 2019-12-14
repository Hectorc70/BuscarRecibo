import os
import os.path



class Rutas():

    def __init__(self, ruta):
        self.ruta_obtener_carpeta = ruta
        self.recuperar_rutas()



    def recuperar_rutas(self):
        """Recupera las Rutas de recibos"""      
        
        self.rutas_pdf = list()
      
       
        

        for ruta, carpetas, recibos in os.walk(self.ruta_obtener_carpeta):                      
          
            
            for archivo in recibos:
            

                extencion_archivo = os.path.splitext(archivo)

                if  extencion_archivo[-1] == '.pdf':

                    ruta_completa = ruta.replace('/','\\')+ "\\" + archivo
                    self.rutas_pdf.append(ruta_completa)

                    

                else:
                    print("Selecciona una carpeta con RECIBOS")
                    self.recuperar_rutas()
                    

    
    
    
