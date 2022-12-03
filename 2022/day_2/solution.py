test_input = open('test_input', 'r').read()
actual_input = open('actual_input', 'r').read()
problem_input = actual_input

problem_1_outcomes = {
    ('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3,
    ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
    ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6
}


def problem_1():
    return sum([problem_1_outcomes[tuple(i.split())] for i in problem_input.splitlines()])


problem_2_outcomes = {
    ('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
    ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
    ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7
}


def problem_2():
    return sum([problem_2_outcomes[tuple(i.split())] for i in problem_input.splitlines()])


if __name__ == "__main__":
    print('Day2, Problem 1, Solution: ', problem_1())
    print('Day2, Problem 2, Solution: ', problem_2())
