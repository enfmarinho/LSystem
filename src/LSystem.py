from alphabet import ALPHABET


# Check if l_system string contains only valid characters, i.e. characters in the alphabet
def validate(l_system):
    for char in l_system:
        if char not in ALPHABET:
            return False

    return True

def check(axiom, string, rules, n_iterations):
    stack = []
    stack.extend(reversed(axiom))

    nodes_height = []
    for count in range(len(stack)):
        nodes_height.append(0)

    max_height_reached = 0
    string_idx = 0
    while stack:
        top = stack.pop()
        top_height = nodes_height.pop()

        if top in rules and top_height < n_iterations:
            stack.extend(reversed(rules[top]))
            for count in range(len(rules[top])):
                nodes_height.append(top_height + 1)
            max_height_reached = max(max_height_reached, top_height + 1)
        elif top == string[string_idx]:
            string_idx += 1
        else:
            return False

    # Check if got to the asked tree height and to the end of the string
    return (max_height_reached == n_iterations or all_constants(string, rules)) and string_idx == len(string)


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
