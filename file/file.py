import PyPDF2


class File:
    """Obtiene el texto de una pagina especificada

        Args:
            page (Number): El numero de la pagina a obtener

        Returns:
            objeto: contiene todo el texto de la pagina
        """

    def __init__(self, path):
        self.path = path

    def _extract(self):
        pdf = PyPDF2.PdfFileReader(self.path)
        page_number = pdf.getNumPages()
        page_content = ''
        for page in range(0, page_number):
            page_one_object = pdf.getPage(page)
            page_one_text = page_one_object.extractText()
            page_content += page_one_text
        return page_content

    def write_file(self):
        text = self._extract()
        with open("data/texto.txt", "w", encoding="utf-8") as file:
            for line in text:
                file.write(line)
