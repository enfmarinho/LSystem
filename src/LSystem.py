from alphabet import ALPHABET


# Check if l_system string contains only valid characters, i.e. characters in the alphabet
def validate(l_system):
    for char in l_system:
        if char not in ALPHABET:
            return False

    return True


def check_rec(axiom, string, rules, n_iterations):
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


def check(axiom, string, rules, n_iterations):
    stack = []
    stack.extend(reversed(axiom))

    nodes_heights = []
    for count in range(len(stack)):
        nodes_heights.append(0)

    max_height_reached = 0
    string_idx = 0
    while stack:
        top = stack.pop()
        top_height = nodes_heights.pop()

        if top in rules and top_height < n_iterations:
            stack.extend(reversed(rules[top]))
            for count in range(len(rules[top])):
                nodes_heights.append(top_height + 1)
            max_height_reached = max(max_height_reached, top_height + 1)
        elif top == string[string_idx]:
            string_idx += 1
        else:
            return False

    # Check if got to the asked tree height and to the end of the string
    return (
        max_height_reached == n_iterations or all_constants(string, rules)
    ) and string_idx == len(string)


def all_constants(string, rules):
    for variable in string:
        if variable in rules:
            return False

    return True


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
