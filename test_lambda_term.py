from lambda_term import Term, Variable, Abstraction, Application


def test_variable_equality():
    assert Variable('a') == Variable('a')
    assert Variable('a') != Variable('b')


def test_abstraction_equality():
    assert Abstraction(Variable('a'), Variable('b')) == Abstraction(Variable('a'), Variable('b'))
    assert Abstraction(Variable('a'), Variable('x')) != Abstraction(Variable('a'), Variable('y'))


def test_application_equality():
    assert Application(Variable('a'), Variable('b')) == Application(Variable('a'), Variable('b'))
    assert Application(Variable('a'), Variable('x')) != Application(Variable('a'), Variable('y'))