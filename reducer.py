from unittest import case

from lambda_term import Term, Variable, Abstraction, Application


class Reducer:

    def __init__(self, expression: Term):
        self._expression = expression

    def reduce_once(self) -> 'Reducer':
        self._expression = self._reduce_once(self._expression)
        return self

    @staticmethod
    def _reduce_once(term: Term) -> Term:
        match term:
            case Variable():
                pass
            case Abstraction():
                pass
            case Application():
                function = term.function
                argument = term.argument
                match function:
                    case Abstraction():
                        return Reducer._replace(function.body, function.input, argument)
                    case Application():
                        return Application(
                            Reducer._reduce_once(function),
                            argument,
                        )
            case _:
                pass
        return term

    @staticmethod
    def _replace(term: Term, variable: Variable, replace: Term) -> Term:
        match term:
            case Variable():
                if term == variable:
                    return replace
                else:
                    return term
            case Abstraction():
                if term.input == variable:  # we've got a naming conflict!
                    new_input = Reducer._variate(term.input)
                    new_body = Reducer._change(term.body, term.input, new_input)
                    return Abstraction(
                        new_input,
                        Reducer._replace(new_body, variable, replace)
                    )
                else:
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

    @staticmethod
    def _change(term: Term, old: Variable, new: Variable) -> Term:
        match term:
            case Variable():
                if term == old:
                    return new
                else:
                    return term
            case Abstraction():
                return Abstraction(
                    term.input,
                    Reducer._change(term.body, old, new),
                )
            case Application():
                return Application(
                    Reducer._change(term.function, old, new),
                    Reducer._change(term.argument, old, new),
                )
            case _:
                return term

        return term

    @staticmethod
    def _variate(variable: Variable) -> Variable:
        return Variable(
            variable.name,
            variable.variant + 1,
        )

    def expression(self) -> Term:
        return Reducer._remove_variation(self._expression)

    @staticmethod
    def _remove_variation(term: Term) -> Term:
        match term:
            case Variable():
                return Variable(term.name)
            case Abstraction():
                return Abstraction(
                    Variable(term.input.name),
                    Reducer._remove_variation(term.body)
                )
            case Application():
                return Application(
                    Reducer._remove_variation(term.function),
                    Reducer._remove_variation(term.argument),
                )
            case _:
                return term