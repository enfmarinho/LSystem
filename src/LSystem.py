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
    stack_height_after_sub = -1

    max_height_reached = 0
    curr_height = 0  
    sidx = 0 # string current index
    while stack:
        top = stack.pop()

        if top in rules and curr_height < n_iterations:
            stack.extend(reversed(rules[top]))
            # add_to_stack(stack, rules[top])
            stack_height_after_sub = len(stack)
            curr_height += 1
            max_height_reached = max(max_height_reached, curr_height)
        elif top == string[sidx]:
            sidx += 1
        else:
            return False

        if len(stack) < stack_height_after_sub:
            curr_height -= 1
            curr_height = min(curr_height, 0)

    # Check if got to the asked tree height and to the end of the string
    return (max_height_reached == n_iterations or all_terminal_nodes(string, rules)) and sidx == len(string)


def all_terminal_nodes(string, rules):
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
