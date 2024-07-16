"""
Create a lambda function to calculate the factorial of a number.
"""

Factorial_number = lambda n: 1 if n == 0 else n * Factorial_number(n - 1)
result = Factorial_number(5)  # result = factorial(n)
print(result)


"""
`Factorial_number = lambda n: 1 if n == 0 else n * Factorial_number(n - 1)`
Execution:
    1) `n` is the parameter of the lambda function.
    2) Condition : `1 if n == 0`
        Agar `n` zero hai toh factorial `1` return karo(Base Case).
    3) Else part : `n * Factorial_number(n - 1)`
        Agar `n` zero nahi hai toh `n` ko `factorial_number(n - 1)` ke saath multiply karo(recursive call).
Step-By_Step Execution :
    1) `result = Factorial_number(5)`
            - `n` is 5, which is not `0`
        - Calculate : `5 * Factorial_number(4)`
    2) First Recursive Call : 
        `Factorial_number(4)`
        - `n` is `4`, Which is not `0`
        - Calculate : `4 * Factorial_number(3)`
    3) Second Recursive Call :
        `Factorial_number(3)`
        - `n` is 3 which is not `0`
        - Calculate : `3 * Factorial_number(2)`
    4) Third Recursive Call :
        `Factorial_number(2)`
        - `n` is 2 which is not `0`
        - Calculate : `2 * Factorial_number(1)`
    5) Forth Recursive Call :
        `Factorial_number(1)`
        - `n` is 1 which is not `0`
        - Calculate : `1 * Factorial_number(0)`
    6) Base Case :
        `Factorial_number(0)`
        - `n` is 0 which is match base case
        - return `1`
Combining the result :
    1) `Factorial_number(0) return 1`
    2) `Factorial_number(1) return 1 * 1 = 1`
    3) `Factorial_number(2) return 2 * 1 = 2`
    4) `Factorial_number(3) return 3 * 2 = 6`
    5) `Factorial_number(4) return 4 * 6 = 24`
    6) `Factorial_number(5) return 5 * 24 = 120`
"""