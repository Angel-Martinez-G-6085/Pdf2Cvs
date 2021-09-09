from scanner.scanner import Scanner

class Filter:
    def __init__(self):
        self.scanner=Scanner()
    
    def get_General_Inf(self):
        campos=['Solicitud','Registrada como','Origen','Situación','Atendida como','Centro','INFORMACIÓN GENERAL','INFORMACIÓN DEL SERVICIO']
        self.scanner.find('Solicitud',campos)
    
    
    def getBitacora(self):
        campos=['BITACORA DE MOVIMIENTOS','TRABAJOS REALIZADOS']
        self.scanner.find('BITACORA DE MOVIMIENTOS',campos)