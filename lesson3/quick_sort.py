"""
    O quick sort utiliza a estratégia de dividir para conquistar para obter as mesmas vantagens do merge sort,
    mas sem usar espaço adicional. Em compensação, é possível que a lista possa não ser dividida ao meio.
    Quando isso ocorre, veremos que seu desempenho é reduzido.

    O quick sort primeiro seleciona um valor, chamado de pivô. Embora existam muitas maneiras de selecionar o pivô,
    iremos utilizar simplesmente o primeiro item na lista. O papel do pivô é ajudar na divisão da lista.
    A posição à qual o pivô pertence de fato na lista ordenada, conhecida como ponto de divisão,
    será usada para quebrar a lista em chamadas subsequentes do quick sort.
"""


def quick_sort(test_list):
    quick_sort_helper(test_list, 0, len(test_list)-1)


def quick_sort_helper(test_list, first, last):
    if first < last:
        split_point = partition(test_list, first, last)
        quick_sort_helper(test_list, first, split_point-1)
        quick_sort_helper(test_list, split_point+1, last)


def partition(test_list, first, last):
    pivot_value = test_list[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and test_list[leftmark] <= pivot_value:
            leftmark += 1
        while test_list[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = test_list[leftmark]
            test_list[leftmark] = test_list[rightmark]
            test_list[rightmark] = temp

    temp = test_list[first]
    test_list[first] = test_list[rightmark]
    test_list[rightmark] = temp

    return rightmark


test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(test_list)
print(test_list)
