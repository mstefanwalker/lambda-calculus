from lambda_term import Term, Variable, Abstraction, Application
from reducer import Reducer


def main():
    print("Hello from lambda-calculus!")

    # ====================
    #      Reduction
    # ====================
    print()
    expression: Term = Application(
        Abstraction(
            Variable('x'),
            Application(
                Variable('x'),
                Variable('b'),
            ),
        ),
        Variable('E')
    )
    print(f"Expression   {expression}")
    reduced_once = Reducer(expression).reduce_once().expression()
    print(f"Reduced      {reduced_once}")

    # ====================
    #    True and False
    # ====================
    print()
    true: Term = Abstraction(
        Variable('a'),
        Abstraction(
            Variable('b'),
            Variable('a'),
        ),
    )
    print(f"True             {true}")
    false: Term = Abstraction(
        Variable('a'),
        Abstraction(
            Variable('b'),
            Variable('b'),
        ),
    )
    print(f"False            {false}")
    if_then_else: Term = Application(
        Application(
            Variable('X'),
            Variable('1'),
        ),
        Variable('0'),
    )
    print(f"If/Then/Else     {if_then_else}")
    if_true_then_1: Term = Application(
        Abstraction(
            Variable('X'),
            if_then_else,
        ),
        true,
    )
    print(f"If True Then 1   {if_true_then_1}")
    reducer = Reducer(if_true_then_1)
    print(f"Reduction 1      {reducer.reduce_once().expression()}")
    print(f"Reduction 2      {reducer.reduce_once().expression()}")
    print(f"Reduction 3      {reducer.reduce_once().expression()}")

    # ====================
    #     Logical NOT
    # ====================
    print()
    logic_not_concept: Term = Application(
        Application(
            Variable('X'),
            Variable('0'),
        ),
        Variable('1'),
    )
    print(f"logic NOT concept        {logic_not_concept}")
    logic_not_true_illustrative: Term = Application(
        Abstraction(
            Variable('X'),
            Application(
                Application(
                    Variable('X'),
                    Variable('0'),
                ),
                Variable('1'),
            )
        ),
        true
    )
    print(f"NOT True (0 and 1 out)   {logic_not_true_illustrative}")
    reducer = Reducer(logic_not_true_illustrative)
    print(f"Reduction 1              {reducer.reduce_once().expression()}")
    print(f"Reduction 2              {reducer.reduce_once().expression()}")
    print(f"Reduction 3              {reducer.reduce_once().expression()}")
    logic_not: Term = Application(
        Application(
            Variable('X'),
            false
        ),
        true
    )
    print(f"(concept)                {logic_not_concept}")
    print(f"True/False output        {logic_not}")
    logic_not_true: Term = Application(
        Abstraction(
            Variable('X'),
            Application(
                Application(
                    Variable('X'),
                    false
                ),
                true
            )
        ),
        true
    )
    print(f"NOT True (full output)   {logic_not_true}")
    reducer = Reducer(logic_not_true)
    print(f"Reduction 1              {reducer.reduce_once().expression()}")
    print(f"Reduction 2              {reducer.reduce_once().expression()}")
    print(f"Reduction 3              {reducer.reduce_once().expression()}")
    

if __name__ == "__main__":
    main()
