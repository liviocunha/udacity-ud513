"""
    - Escreva uma função denominada "show_excitement" (demonstre animação), na qual a string
    "I am super excited for this course!" (estou muito animado para este curso!)
    seja retornada exatamente 5 vezes, com cada sentença separada por um espaço simples.
    - Retorne essa string com "return" (retornar).
    - A string poderá aparecer apenas uma vez em seu código.
    - Não realize o procedimento de copiar/colar a string por 5 vezes dentro de uma variável simples!

"""


def show_excitement():
    string = "I am super excited for this course! "
    return string * 5


if __name__ == '__main__':
    exec_function = show_excitement()
    print(exec_function)
