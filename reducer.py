from lambda_term import Term


class Reducer:

    def __init__(self, expression: Term):
        self._expression = expression

    def reduce_once(self) -> 'Reducer':
        return self

    def expression(self) -> Term:
        return self._expression