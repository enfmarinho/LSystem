from alphabet import ALPHABET


# Check if l_system string contains only valid characters, i.e. characters in the alphabet
def validate(l_system):
    for char in l_system:
        if char not in ALPHABET:
            return False

    return True


def insert_string_in_list(list, string):
    for char in string:
        list.append(char)


# l_system is a list of chars instead of string because strings are
# immutable, which would cause a lot of memory copies when dealing with
def apply_production_rules(l_system, rules, n_iterations):
    if n_iterations == 0:
        return l_system

    next_iteration_l_system = []
    for char in l_system:
        if char in rules:
            insert_string_in_list(next_iteration_l_system, rules[char])
        else:
            next_iteration_l_system.append(char)

    return apply_production_rules(next_iteration_l_system, rules, n_iterations - 1)
