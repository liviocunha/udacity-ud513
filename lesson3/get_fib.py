"""
    Implemente uma função de maneira recursiva para obter o valor desejado na sequência Fibonacci.
    Seu código deve possuir a mesma entrada/saída do código iterativo contido nas instruções.
"""


def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)


print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
