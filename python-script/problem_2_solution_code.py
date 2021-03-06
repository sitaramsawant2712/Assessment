"""
2.	Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering
    the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    (Answer: 4613732) (solution code attached: problem_2_solution_code.py)

"""


def fibonacci_even_value(upper):
    '''
    @description: Fibonacci sequence whose values do not exceed upper limit. calculate the sum of the even-value.
    '''
    total = 0
    x, y = 0, 1
    while y < upper:
        x, y = y, x + y
        if x % 2:
            continue
        total += x
    return total


if __name__ == '__main__':
    upper = int(input("Enter upper range limit:"))
    total = fibonacci_even_value(upper)
    output = "Sum of the even-value of Fibonacci sequence less then {0}. \n(Answer: {1})".format(upper, total)
    print(output)
