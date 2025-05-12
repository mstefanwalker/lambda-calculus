from reducer import Reducer
from lambda_term import Term, Variable, Abstraction, Application


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
    assert str(expression) == str(Reducer(expression).expression())


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
    assert str(Reducer(expression).reduce_once().expression()) == str(expected)