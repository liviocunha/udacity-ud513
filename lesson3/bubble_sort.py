"""
    O bubble sort realiza múltiplas passagem por uma lista.
    Ele compara itens adjacentes e troca aqueles que estão fora de ordem.
    Cada passagem pela lista coloca o próximo maior valor na sua posição correta.
    Em essência, cada item se desloca como uma “bolha” para a posição à qual pertence.

    https://panda.ime.usp.br/pythonds/static/pythonds_pt/05-OrdenacaoBusca/OBubbleSort.html
"""


def bubble_sort(test_list):
    for pass_num in range(len(test_list)-1, 0, -1):
        for i in range(pass_num):
            if test_list[i] > test_list[i+1]:
                temp = test_list[i]
                test_list[i] = test_list[i+1]
                test_list[i+1] = temp
    return test_list


test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubble_sort(test_list)
print(test_list)
