import LSystem as ls
from renderer import Renderer


def read_input():
    return (
        int(input("Número de iterações: ")),
        int(input("Ângulo: ")),
        float(input("Incremento da largura: ")),
        input("L-System: "),
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


def main():
    n_iterations, angle, width_increment, l_system = read_input()

    if not ls.validate(l_system):
        print("Cadeia de caracteres L-System inválida!")
        return False

    l_system = ls.apply_production_rules(l_system, read_rules(), n_iterations)

    print(f"L-System após {n_iterations} reescritas: {l_system}")

    Renderer(angle, width_increment).render(l_system)

    return True


if __name__ == "__main__":
    main()
