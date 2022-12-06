import re
from functools import reduce
from itertools import zip_longest

test_input = open('test_input', 'r').read()
actual_input = open('actual_input', 'r').read()
problem_input = actual_input


def problem_1():
    return ''.join(list(map(list.pop, list(reduce(lambda stt, ins:[c[:-ins[0]] if ins[1] == i + 1 else c + list(reversed(stt[ins[1]-1][-ins[0]:])) if ins[2] == i + 1 else c for i, c in enumerate(stt)], list(map(lambda inst: list(map(int, re.findall(r' (\d+)', inst))), list(map(str.splitlines, problem_input.split('\n\n')))[1])), list(map(lambda stack: list(reversed(list(filter(lambda entry: bool(entry and entry.strip()), stack)))), zip_longest(*map(lambda row: re.findall(r'\[([a-zA-Z ])\]', re.sub(r'(\]  )', '] [ ]', row).replace('    ', '[ ] ')), list(map(str.splitlines, problem_input.split('\n\n')))[0][:-1])))))))))


def problem_2():
    return ''.join(list(map(list.pop, list(reduce(lambda stt, ins:[c[:-ins[0]] if ins[1] == i + 1 else c + stt[ins[1]-1][-ins[0]:] if ins[2] == i + 1 else c for i, c in enumerate(stt)], list(map(lambda inst: list(map(int, re.findall(r' (\d+)', inst))), list(map(str.splitlines, problem_input.split('\n\n')))[1])), list(map(lambda stack: list(reversed(list(filter(lambda entry: bool(entry and entry.strip()), stack)))), zip_longest(*map(lambda row: re.findall(r'\[([a-zA-Z ])\]', re.sub(r'(\]  )', '] [ ]', row).replace('    ', '[ ] ')), list(map(str.splitlines, problem_input.split('\n\n')))[0][:-1])))))))))


if __name__ == "__main__":
    print('Day X, Problem 1, Solution: ', problem_1())
    print('Day X, Problem 2, Solution: ', problem_2())
