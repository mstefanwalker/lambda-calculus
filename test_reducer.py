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