from alphabet import ALPHABET


# Check if string contains only valid characters, i.e. characters in the alphabet
def validate(string):
    for char in string:
        if char not in ALPHABET:
            return False

    return True


def apply_production_rules(l_system, n_iterations):
    if n_iterations == 0:
        return l_system

    # TODO make the substitutions
    next_iteration_l_system = l_system

    return apply_production_rules(next_iteration_l_system, n_iterations - 1)
