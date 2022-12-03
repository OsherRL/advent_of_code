from functools import reduce

test_input = open('test_input', 'r').read()
actual_input = open('actual_input', 'r').read()
problem_input = actual_input


def problem_1():
    return sum(map(lambda a: sum(map(lambda b: ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(b), set(a[:len(a) // 2]).intersection(set(a[len(a) // 2:])))), problem_input.splitlines()))


def problem_2():
    return sum(map(lambda x: sum(map(lambda y: ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(y), x)), map(lambda a: reduce(lambda b, c: b.intersection(c), a), [map(set, problem_input.splitlines()[i:i + 3]) for i in range(0, len(problem_input.splitlines()), 3)])))


if __name__ == "__main__":
    print('Day 3, Problem 1, Solution: ', problem_1())
    print('Day 3, Problem 2, Solution: ', problem_2())
