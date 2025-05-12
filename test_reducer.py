from reducer import Reducer
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


def test_expression_is_unmodified():
    expression: Term = Application(
        Abstraction(
            Variable('x'),
            Application(
                Variable('x'),
                Variable('b'),
            )
        ),
        Variable('E')
    )
    assert expression == Reducer(expression).expression()


def test_expression_is_reduced_once():
    expression: Term = Application(
        Abstraction(
            Variable('x'),
            Application(
                Variable('x'),
                Variable('b'),
            )
        ),
        Variable('E')
    )
    expected: Term = Application(
        Variable('E'),
        Variable('b')
    )
    assert Reducer(expression).reduce_once().expression() == expected


def test_deep_abstractions_reduce():
    true: Term = Abstraction(
        Variable('a'),
        Abstraction(
            Variable('b'),
            Variable('a'),
        ),
    )
    if_then_else: Term = Application(
        Application(
            Variable('X'),
            Variable('1'),
        ),
        Variable('0'),
    )
    if_true_then_1: Term = Application(
        Abstraction(
            Variable('X'),
            if_then_else
        ),
        true
    )
    expected: Term = Variable('1')
    reduced: Term = Reducer(if_true_then_1).reduce_once().reduce_once().reduce_once().expression()
    assert reduced == expected