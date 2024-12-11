from alphabet import ALPHABET


# Check if l_system string contains only valid characters, i.e. characters in the alphabet
def validate(l_system):
    for char in l_system:
        if char not in ALPHABET:
            return False

    return True


def check(l_system, string, rules, n_iterations):
    stack = []
    stack.extend(l_system[::-1])

    string_idx = 0
    last_sub = 0
    counter = 0
    while stack:
        t = stack.pop()
        if string_idx >= len(string):
            return False
        elif t in rules and counter < n_iterations:
            if len(stack) > last_sub:
                counter += 1
            stack.extend(rules[t][::-1])
            last_sub = len(stack)
        elif string[string_idx] == t:
            string_idx += 1
        else:
            return False

    return string_idx == len(string) and counter == n_iterations


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
