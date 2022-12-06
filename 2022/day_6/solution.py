test_input = open('test_input', 'r').read()
actual_input = open('actual_input', 'r').read()
problem_input = actual_input


def problem_1():
    return [len(problem_input[i-3:i+1]) == len(set(problem_input[i-3:i+1])) for i in range(3, len(problem_input))].index(True) + 4


def problem_2():
    return [len(problem_input[i - 13:i + 1]) == len(set(problem_input[i - 13:i + 1])) for i in range(13, len(problem_input))].index(True) + 14


if __name__ == "__main__":
    print('Day X, Problem 1, Solution: ', problem_1())
    print('Day X, Problem 2, Solution: ', problem_2())
