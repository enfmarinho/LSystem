import LSystem as ls


def test_validate():
    assert ls.validate("F-fbFg-f")
    assert ls.validate("FbF-f+rF[--gFTFF]FF")
    assert ls.validate("FbF")
    assert not ls.validate("F-fbFg-fj")
    assert not ls.validate("/")
    assert not ls.validate("  F-fbFg-f")


def test_check_and_apply_production_rules():
    rules = {}
    rules["F"] = "b"

    assert ls.check("FF", "bb", rules, 3)
    assert ls.apply_production_rules("FF", rules, 3) == [list("bb")]

    assert ls.check("FbF", "bbb", rules, 1)
    assert ls.apply_production_rules("FbF", rules, 1) == [list("bbb")]

    rules["b"] = "F"
    assert not ls.check("FF", "bb", rules, 4)
    assert ls.apply_production_rules("FF", rules, 4) == [list("FF")]

    assert ls.check("FF", "bb", rules, 5)
    assert ls.apply_production_rules("FF", rules, 5) == [list("bb")]

    rules["b"] = "r"
    rules["f"] = "F"
    rules["-"] = "+"
    rules["+"] = "-"
    assert ls.check("F-fbFg-f", "r+rrrg+r", rules, 3)
    assert ls.apply_production_rules("F-fbFg-f", rules, 3) == [list("r+rrrg+r")]

    rules.clear()
    rules["F"] = ["+f"]
    assert ls.check("F", "+f", rules, 1)
    assert ls.apply_production_rules("F", rules, 5) == [list("+f")]

    rules["+"] = "-"
    rules["-"] = "+"
    assert ls.check("F", "-f", rules, 2)
    assert ls.apply_production_rules("F", rules, 2) == [list("-f")]

    assert not ls.check("F", "-f", rules, 3)
    assert ls.apply_production_rules("F", rules, 3) == [list("+f")]

    rules.clear()
    rules["F"] = ["b", "r"]
    assert ls.check("Ff", "bf", rules, 2)
    assert ls.check("Ff", "rf", rules, 3)
    assert ls.apply_production_rules("Ff", rules, 1) == [list("bf"), list("rf")]
    assert ls.apply_production_rules("Ff", rules, 3) == [list("bf"), list("rf")]


def main():
    test_validate()
    test_check_and_apply_production_rules()

    print("Passed all tests!")


if __name__ == "__main__":
    main()
