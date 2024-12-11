from alphabet import ALPHABET


# Check if l_system string contains only valid characters, i.e. characters in the alphabet
def validate(l_system):
    for char in l_system:
        if char not in ALPHABET:
            return False

    return True


def check(l_system, string, rules, n_iterations):
    stack = []
    las_sub_stack = []
    for variable in l_system:
        stack.append(variable)
        las_sub_stack.append(0)

    string_idx = 0
    counter = 0
    max_counter = 0
    while stack:
        t = stack.pop()
        last_sub = las_sub_stack.pop()

        if string_idx >= len(string):
            return False
        elif t in rules and counter <= n_iterations:
            if len(stack) > last_sub:
                max_counter = max(max_counter, counter)
                counter += 1
            elif last_sub <= len(stack):
                max_counter = max(max_counter, counter)
                counter -= 1

            last_sub = len(stack)
            for variable in reversed(rules[t]):
                stack.append(variable)
                las_sub_stack.append(last_sub)

        elif string[string_idx] == t:
            string_idx += 1
        else:
            return False

    return string_idx == len(string) and max_counter == n_iterations


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
