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
def apply_production_rules(l_systems, rules, n_iterations):
    if isinstance(l_systems, str):
        l_systems = list(l_systems)

    for counter in range(n_iterations):
        l_systems_cp = l_systems.copy()
        l_systems.clear()
        for l_system in l_systems_cp:
            l_systems.extend(apply_rules(l_system, rules, 0))

    return l_systems


def apply_rules(string, rules, start_index):
    new_string = []
    for index in range(start_index, len(string)):
        variable = string[index]
        if variable in rules:
            l_system_list = []
            for rule in rules[variable]:
                string_list = apply_rules(string, rules, index + 1)
                string_a = new_string.copy()
                string_a.extend(rule)
                l_system_list.extend(append_list(string_a, string_list))
            return l_system_list
        else:
            new_string.append(variable)

    return new_string


def append_list(prefix, string_list):
    final_list = []
    for string in string_list:
        prefix.extend(string)
        final_list.append(prefix)

    if final_list == []:
        return prefix
    return final_list
