from dataclasses import dataclass


@dataclass
class Term:
    pass


@dataclass
class Variable(Term):
    name: str

    def __str__(self):
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