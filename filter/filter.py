from scanner.scanner import Scanner

class Filter:
    def __init__(self):
        pass
    
    def get_General_Inf(self):
        scanner=Scanner()
        campos=['Solicitud','Registrada como','Origen','Situación','Atendida como','Centro','INFORMACIÓN GENERAL','INFORMACIÓN DEL SERVICIO']
        scanner.find('Solicitud',campos)