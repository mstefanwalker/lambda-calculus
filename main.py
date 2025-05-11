from lambda_term import Term, Variable, Abstraction, Application


def main():
    print("Hello from lambda-calculus!")
    expression: Term = Application(Abstraction(Variable('a'), Variable('b')), Variable('c'))
    print(f"Expression: {expression}")


if __name__ == "__main__":
    main()
