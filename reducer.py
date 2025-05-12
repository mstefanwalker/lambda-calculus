from unittest import case

from lambda_term import Term, Variable, Abstraction, Application


class Reducer:

    def __init__(self, expression: Term):
        self._expression = expression

    def reduce_once(self) -> 'Reducer':
        expression = self._expression
        match expression:
            case Variable():
                pass
            case Abstraction():
                pass
            case Application():
                function = expression.function
                argument = expression.argument
                if isinstance(function, Abstraction):
                    result = self._replace(function.body, function.input, argument)
                    self._expression = result
            case _:
                pass
        return self

    @staticmethod
    def _replace(term: Term, variable: Variable, replace: Term) -> Term:
        match term:
            case Variable():
                if term.name == variable.name:
                    return replace
                else:
                    return term
            case Abstraction():
                return Abstraction(
                    term.input,
                    Reducer._replace(term.body, variable, replace),
                )
            case Application():
                return Application(
                    Reducer._replace(term.function, variable, replace),
                    Reducer._replace(term.argument, variable, replace),
                )
            case _:
                return term

    def expression(self) -> Term:
        return self._expression