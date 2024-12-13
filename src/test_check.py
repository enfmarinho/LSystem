import LSystem as ls

def main():
    rules = {}
    rules['F'] = "b"

    assert ls.check("FF", "bb", rules, 3)
    assert ls.check("FbF", "bbb", rules, 1)

    rules['b'] = 'F'
    assert not ls.check("FF", "bb", rules, 4)
    assert ls.check("FF", "bb", rules, 5)

    rules['b'] = 'r'
    rules['f'] = 'F'
    rules['-'] = '+'
    rules['+'] = '-'
    assert ls.check("F-fbFg-f", "r+rrrg+r", rules, 3)

    rules.clear()
    rules['F'] = '+f'
    assert ls.check("F", "+f", rules, 1)


    rules['+'] = '-'
    rules['-'] = '+'
    assert ls.check("F", "-f", rules, 2)


if __name__ == "__main__":
    main()
