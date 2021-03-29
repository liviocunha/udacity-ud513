"""
    Agora nós voltamos nossa atenção para usar a estratégia de “dividir para conquistar” como uma forma de melhorar o
    desempenho dos algoritmos de ordenação. O primeiro algoritmo que iremos estudar é o merge sort, um algoritmo
    recursivo que divide uma lista continuamente pela metade. Se a lista estiver vazia ou tiver um único item,
    ela está ordenada por definição (o caso base). Se a lista tiver mais de um item, dividimos a lista e
    invocamos recursivamente um merge sort em ambas as metades. Assim que as metades estiverem ordenadas,
    a operação fundamental, chamada de intercalação, é realizada.
    Intercalar é o processo de pegar duas listas menores ordenadas e combiná-las de modo a formar uma lista nova,
    única e ordenada.

    https://panda.ime.usp.br/pythonds/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
"""


def merge_sort(test_list):
    # print("Splitting ", test_list)
    if len(test_list) > 1:
        mid = len(test_list)//2
        lefthalf = test_list[:mid]
        righthalf = test_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                test_list[k] = lefthalf[i]
                i = i+1
            else:
                test_list[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            test_list[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            test_list[k] = righthalf[j]
            j = j+1
            k = k+1
    # print("Merging ", test_list)


test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(test_list)
print(test_list)
