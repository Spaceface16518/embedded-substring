import sys

from termcolor import cprint


def match(target, substring):
    indices = []
    current_sub = 0
    sub_length = len(substring)
    for i, char in enumerate(target):
        if current_sub >= sub_length:
            break
        if char == substring[current_sub]:
            indices.append(i)
            current_sub += 1
    if len(indices) == sub_length:
        return indices
    else:
        return None


if __name__ == '__main__':
    input_str = str(sys.stdin.read())
    find_str = ''.join(sys.argv[1:])
    matches = match(input_str, find_str)

    for i, char in enumerate(input_str):
        if i in matches:
            cprint(char, color='red', attrs=['bold'], end='')
        else:
            print(char, end='')
