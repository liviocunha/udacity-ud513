"""
    - Você pode utilizar esta classe para representar o nível de elegância de alguém ou algo.
    - "Classy" (elegante) é intercambiável com "fancy" (chique).
    - Caso adicione itens chiques, isso aumentará a sua "classiness" (elegância).
    - Crie uma função em "Classy" (Elegante) que leve uma string como retorno e a adicione à lista de "items" (itens).
    - Outro método deve calcular o valor de "classiness" (elegância) baseado nos itens.
    - Os itens a seguir possuem pontos de elegância a eles associados:
        - "tophat" (cartola) = 2
        - "bowtie" (gravata borboleta) = 4
        - "monocle" (monóculo) = 5
    - Todos os demais possuem 0 pontos.
"""


class Classy(object):
    def __init__(self):
        self.items = []
        self.items_fancy = {"tophat": 2, "bowtie": 4, "monocle": 5}

    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        classiness = 0
        for item in self.items:
            try:
                classiness = self.items_fancy[item] + classiness
            except KeyError:
                classiness += 0
        return classiness


if __name__ == '__main__':
    me = Classy()

    print(me.getClassiness())
    # Should be 0

    me.addItem("tophat")

    print(me.getClassiness())
    # Should be 2
    me.addItem("bowtie")
    me.addItem("jacket")
    me.addItem("monocle")

    print(me.getClassiness())
    # Should be 11
    me.addItem("bowtie")

    print(me.getClassiness())
    # Should be 15

    me.addItem("cap")
    print(me.getClassiness())
    # Should be 15
