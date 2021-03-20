"""
    Big O
    - Observe cada um e tome nota da eficiência de tempo. Sempre que possível, use aproximações!
    manatees = [{"name": "Fulano", "age": 20}, {"name": "Beltrano", "age": 30}]

    insira manatees: lista de "manatees", em que cada um é representado por um dicionário
    um só manatee possui propriedades como "name", "age", etc.
    n = o número de elementos em "manatees"
    m = número de propriedades por "manatee" (o número de chaves num dicionário de manatee)

    http://bigocheatsheet.com/

"""
import time  # Library to analyze the execution time of the algorithm


def example1(manatees):
    result = ""
    for manatee in manatees:
        print(manatee['name'])
        result = f"{manatee['name']}\n{result}"
    return result


def example2(manatees):
    print(manatees[0]['name'])
    print(manatees[0]['age'])
    return f"{manatees[0]['name']}\n{manatees[0]['age']}"


def example3(manatees):
    result = ''
    for manatee in manatees:
        for manatee_property in manatee:
            print(f"{manatee_property} : {manatee[manatee_property]}")
            result = f"{manatee_property} : {manatee[manatee_property]}\n"
    return result


def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print(oldest_manatee)
    return oldest_manatee


if __name__ == '__main__':
    manatees = [{"name": "Fulano", "age": 10}, {"name": "Beltrano", "age": 20}]

    # Eficiência de tempo: O(n)
    print("Example 1:")
    time_1_ex1 = time.time()
    example1(manatees)
    time_2_ex1 = time.time()
    print()

    # Eficiência de tempo: O(1)
    print("Example 2:")
    time_1_ex2 = time.time()
    example2(manatees)
    time_2_ex2 = time.time()
    print()

    # Eficiência de tempo: O(nm)
    print("Example 3:")
    time_1_ex3 = time.time()
    example3(manatees)
    time_2_ex3 = time.time()
    print()

    # Eficiência de tempo: O(nn) ou O(n^2) - que é lido como "n squared"
    print("Example 4:")
    time_1_ex4 = time.time()
    example4(manatees)
    time_2_ex4 = time.time()
    print()

    print()
    print("Results:")
    print(f"Example 1 O(n) -> Runtime: {time_2_ex1 - time_1_ex1} seconds.")
    print(f"Example 2 O(1) -> Runtime: {time_2_ex2 - time_1_ex2} seconds.")
    print(f"Example 3 O(nm) -> Runtime: {time_2_ex3 - time_1_ex3} seconds.")
    print(f"Example 4 O(nn) or O(n^2) -> Runtime: {time_2_ex4 - time_1_ex4} seconds.")
