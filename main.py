import LSystem as ls
from renderer import Renderer


def read_input():
    return (
        int(input("Número de iterações: ")),
        int(input("Ângulo: ")),
        float(input("Incremento da largura: ")),
        input("L-System: "),
    )


def main():
    n_iterations, angle, width_increment, l_system = read_input()

    if not ls.validate(l_system):
        print("Cadeia de caracteres L-System inválida!")
        return False

    l_system = ls.apply_production_rules(l_system, n_iterations)

    Renderer(angle, width_increment).render(l_system)

    return True


if __name__ == "__main__":
    main()
