import sys

import LSystem as ls
from renderer import Renderer


def read_render_input():
    return (
        int(input("Número de reescritas: ")),
        int(input("Ângulo: ")),
        list(input("L-System: ")),
    )


def read_check_input():
    return (
        int(input("Número de reescritas: ")),
        list(input("L-System: ")),
        list(input("String: ")),
    )


def read_rules():
    print("Escreva as regras a seguir no seguinte formato: char->string")
    print("Quando não houver mais regras deixe a linha em branco!")

    rules = {}
    while True:
        line = input("Regra: ")
        if line == "":
            return rules
        strings = line.split("->", 1)
        rules[strings[0]] = strings[1]


def read_multiple_rules():
    print("Escreva as regras a seguir no seguinte formato: char->string")
    print("Quando não houver mais regras deixe a linha em branco!")

    rules = {}
    while True:
        line = input("Regra: ")
        if line == "":
            return rules
        strings = line.split("->", 1)
        rules.setdefault(strings[0], []).append(strings[1])


def main():
    argv = sys.argv
    if len(argv) < 2:
        print("Argumento faltando. Use checar ou renderizar")
        return False

    elif argv[1] == "checar":
        n_iterations, l_system, string = read_check_input()

        if ls.check(l_system, string, read_multiple_rules(), n_iterations):
            print(
                f"Verdadeiro: O L-System esperado é equivalente ao L-System após {n_iterations} reescritas"
            )
        else:
            print(
                f"Falso: O LSystem esperado não é equivalente ao LSystem após {n_iterations} reescritas"
            )

    elif argv[1] == "renderizar":
        n_iterations, angle, l_system = read_render_input()

        if not ls.validate(l_system):
            print("Cadeia de caracteres L-System inválida!")
            return False

        l_system = ls.apply_production_rules(l_system, read_rules(), n_iterations)

        print(f"L-System após {n_iterations} reescritas: {''.join(l_system)}")

        Renderer(angle).render(l_system)

    else:
        print("Argumento inválido!")
        return False

    return True


if __name__ == "__main__":
    main()
