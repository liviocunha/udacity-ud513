"""
    Você escreverá uma função de pesquisa binária.
    Utilize uma abordagem iterativa, ou seja, por meio de loops.
    Sua função deve submeter duas entradas:
    uma lista Python para efetuar a pesquisa e o valor pelo qual procura
    Suponha que a lista possui apenas elementos distintos, ou seja, não há valores repetidos,
    estando os elementos rigorosamente em ordem crescente.
    Retorne o indicador do valor, ou -1, caso o valor não esteja representado na lista.
"""


def binary_search(input_array, value):
    for item in test_list:
        if item == value:
            return print("Valor encontrado.")
        else:
            return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
