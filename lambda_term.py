from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Term:
    def copy(self):
        return deepcopy(self)


@dataclass
class Variable(Term):
    name: str
    variant: int = 0

    def __str__(self):
        if self.variant > 0:
            return f'{self.name}{self.variant}'
        else:
            return self.name


@dataclass
class Abstraction(Term):
    input: Variable
    body: Term

    def __str__(self):
        return f"(λ{self.input}.{self.body})"


@dataclass
class Application(Term):
    function: Term
    argument: Term

    def __str__(self):
        return f"({self.function}{self.argument})"