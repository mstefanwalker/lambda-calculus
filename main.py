from lambda_term import Term, Variable, Abstraction, Application
from reducer import Reducer


def main():
    print("Hello from lambda-calculus!")
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
    print(f"Expression: {expression}")
    reduced_once = Reducer(expression).reduce_once().expression()
    print(f"Reduced: {reduced_once}")


if __name__ == "__main__":
    main()
