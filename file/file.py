import PyPDF2
class File:
    # cada que un objeto de tipo objeto es creado se solicita la ruta del archivo
    def __init__(self,path,page):
        self.path=path
        self.page=page
        
    def _extract(self):
        """Obtiene el texto de una pagina especificada

        Args:
            page (Number): El numero de la pagina a obtener

        Returns:
            objeto: contiene todo el texto de la pagina
        """        
        pdf=PyPDF2.PdfFileReader(self.path)
        page_one_object=pdf.getPage(self.page)
        page_one_text=page_one_object.extractText()
        return page_one_text
    
    def write_file(self):
        text=self._extract()
        with open("data/texto.txt","w",encoding="utf-8") as file:
            for line in text:
                file.write(line)