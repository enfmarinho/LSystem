import sys

import LSystem as ls
from renderer import Renderer


def read_render_input():
    return (
        int(input("Número de reescritas: ")),
        int(input("Ângulo: ")),
        input("Axioma: "),
    )


def read_check_input():
    return (
        int(input("Número de reescritas: ")),
        input("Axioma: "),
        input("String: "),
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
        rules.setdefault(strings[0], []).append(strings[1])


def main():
    argv = sys.argv
    if len(argv) < 2:
        print("Argumento faltando. Use checar ou renderizar")
        return False

    elif argv[1] == "checar":
        n_iterations, axiom, string = read_check_input()

        if ls.check(axiom, string, read_rules(), n_iterations):
            print(
                f"Verdadeiro: O L-System esperado corresponde ao L-System após {n_iterations} reescritas"
            )
        else:
            print(
                f"Falso: O LSystem esperado não corresponde ao LSystem após {n_iterations} reescritas"
            )

    elif argv[1] == "renderizar":
        n_iterations, angle, axiom = read_render_input()

        if not ls.validate(axiom):
            print("Cadeia de caracteres L-System inválida!")
            return False

        l_systems = ls.apply_production_rules(axiom, read_rules(), n_iterations)

        print(f"L-System a ser renderizado: {''.join(l_systems[0])}")
        Renderer(angle).render(l_systems[0])

    else:
        print("Argumento inválido!")
        return False

    return True


if __name__ == "__main__":
    main()
