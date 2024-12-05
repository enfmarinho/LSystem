from alphabet import ALPHABET


# Check if string contains only valid characters, i.e. characters in the alphabet
def validate(string):
    for char in string:
        if char not in ALPHABET:
            return False

    return True


def apply_production_rules(l_system, rules, n_iterations):
    if n_iterations == 0:
        return l_system

    # TODO probably it would be more efficient to use a list of chars instead of strings, since strings are immutable
    next_iteration_l_system = ""
    for char in l_system:
        if char in rules:
            next_iteration_l_system += rules[char]
        else:
            next_iteration_l_system += char

    return apply_production_rules(next_iteration_l_system, rules, n_iterations - 1)
