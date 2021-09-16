class Scanner:
    def __init__(self):
        pass

    def find(self, campo, limites):
        """Esta funcion se encarga de buscar un campo en el documento y regresarlo junto con su valor

        Args:
            campo (string): es la informacion que estas buscando
            limites (list): el resto de campos en el documento(para saber cuando detenerse)

        Returns:
            diccionary: contiene el campo y valor buscados
        """
        limites.remove(campo)
        information = {}
        value = ''
        find = False
        with open("data/texto.txt", "r", encoding="utf-8") as file:
            for line in file:
                is_inside = line.strip() in limites  # comprueba si line es uno de los limites
                if is_inside == False:
                    if line.find(campo) != -1:  # comprueba que line es el campo que buscas
                        find = True
                    else:
                        if find == True and line != ' \n':
                            value += line.strip()
                elif line != campo and find != True:  # ignora todos los campos que aparescan antes
                    continue  # del que buscas
                else:
                    information[campo] = value
                    return print(information)
