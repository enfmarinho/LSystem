from alphabet import ALPHABET


# Check if l_system string contains only valid characters, i.e. characters in the alphabet
def validate(l_system):
    for char in l_system:
        if char not in ALPHABET:
            return False

    return True


def check(axiom, string, rules, n_iterations):
    stack = []
    for variable in reversed(axiom):
        stack.append((variable, 0))

    return check_aux(list(reversed(string)), rules, n_iterations, stack)


def check_aux(string, rules, n_iterations, stack):
    if not stack or not string:
        return not stack and not string

    variable, height = stack.pop()

    if variable in rules and height < n_iterations:
        for rule in rules[variable]:
            string_cp = string.copy()
            stack_cp = stack.copy()

            for variable in reversed(rule):
                stack_cp.append((variable, height + 1))

            if check_aux(
                string_cp,
                rules,
                n_iterations,
                stack_cp,
            ):
                return True
    elif variable == string.pop():
        return check_aux(string, rules, n_iterations, stack)

    return False


# l_system is a list of chars instead of string because strings are
# immutable, which would cause a lot of memory copies when dealing with
def apply_production_rules(l_system, rules, n_iterations):
    if n_iterations == 0:
        return l_system

    next_iteration_l_system = []
    for variable in l_system:
        if variable in rules:
            next_iteration_l_system.extend(rules[variable])
        else:
            next_iteration_l_system.append(variable)

    return apply_production_rules(next_iteration_l_system, rules, n_iterations - 1)
