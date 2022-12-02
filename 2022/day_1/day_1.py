test_input = open('test_input', 'r').read()
actual_input = open('actual_input', 'r').read()
problem_input = actual_input


def problem_1():
    return max([sum(map(int, i.splitlines())) for i in problem_input.split('\n\n')])


def problem_2():
    return sum(sorted([sum(map(int, i.splitlines())) for i in problem_input.split('\n\n')], reverse=True)[:3])


if __name__ == "__main__":
    print('Day 1, Problem 1, Solution: ', problem_1())
    print('Day 1, Problem 2, Solution: ', problem_2())
