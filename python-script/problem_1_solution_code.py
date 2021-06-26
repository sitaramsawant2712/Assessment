"""
1.	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    (Answer: 233168) (solution code attached: problem_1_solution_code.py)
"""


def natural_number_multi_three_and_five(lower, upper):
    '''
    @description : Calculate the sum of all the multiples of 3 or 5 as per given param.
    '''

    sum_of_multiple = 0
    for i in range(lower, upper):
        if (i % 3 == 0) or (i % 5 == 0):
            sum_of_multiple += i
    return sum_of_multiple


if __name__ == '__main__':
    lower = int(input("Enter lower range limit:"))
    upper = int(input("Enter upper range limit:"))
    sum_of_multiple = natural_number_multi_three_and_five(lower, upper)
    output = "Sum of all the multiples of 3 or 5 below {0}. \n(Answer : {1})".format(upper, sum_of_multiple)
    print(output)
