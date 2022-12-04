test_input = open('test_input', 'r').read()
actual_input = open('actual_input', 'r').read()
problem_input = actual_input


def problem_1():
    return sum(map(lambda pair: 1 if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]) else 0, map(lambda line: list(map(lambda asmt: set(range(int(asmt.split('-')[0]), int(asmt.split('-')[1]) + 1)), line.split(','))), problem_input.splitlines())))


def problem_2():
    return sum(map(lambda pair: min(len(pair[0].intersection(pair[1])), 1), map(lambda line: list(map(lambda asmt: set(range(int(asmt.split('-')[0]), int(asmt.split('-')[1]) + 1)), line.split(','))), problem_input.splitlines())))


if __name__ == "__main__":
    print('Day 4, Problem 1, Solution: ', problem_1())
    print('Day 4, Problem 2, Solution: ', problem_2())
