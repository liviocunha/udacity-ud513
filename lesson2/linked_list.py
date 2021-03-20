"""
    LINKED LIST
    - Adicione três funções à lista vinculada.
    - "get_position" retorna o elemento em uma determinada posição.
    - A função "insert" adicionará um elemento a um lugar específico na lista.
    - "delete" excluirá o primeiro elemento com aquele valor específico.
    - Então, utilize "Test Run" (Executar teste) e "Submit" (Enviar) para executar os casos de teste na parte inferior."
"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Escolha um elemento de uma posição específica.
        Suponha que a primeira posição seja "1".
        Retorne "None" (Nenhum) caso a posição não esteja na lista."""
        pointer = 1
        current = self.head

        if position < 1:
            return None

        while current and pointer <= position:
            if pointer == position:
                return current
            current = current.next
            pointer += 1

        return None

    def insert(self, new_element, position):
        """Acrescente um novo node na posição determinada.
        Suponha que a primeira posição seja "1".
        Inserir na posição 3 significa estar localizado entre o 2º e 3º elementos."""
        pointer = 1
        current = self.head

        if position == 1:
            new_element.next = self.head
            self.head = new_element
        elif position > 1:
            while current and pointer < position:
                if pointer == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                pointer += 1

    def delete(self, value):
        """Exclua o primeiro node que contenha um valor determinado."""
        previous = None
        current = self.head

        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


if __name__ == '__main__':
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    print(ll.head.next.next.value)
    # Should 3

    print(ll.get_position(3).value)
    # Should 3

    ll.insert(e4, 3)
    print(ll.get_position(3).value)
    # Should 4

    ll.delete(1)
    print(ll.get_position(1).value)
    # Should 2

    print(ll.get_position(2).value)
    # Should 4

    print(ll.get_position(3).value)
    # Should 3

