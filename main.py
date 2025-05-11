from lambda_term import Term, Variable, Abstraction, Application


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


if __name__ == "__main__":
    main()
