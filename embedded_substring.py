import sys

import termcolor


def match(target, patterns):
    """
    :param patterns: the patterns to search for within the target string
    :type patterns: list
    :param target: the string to search within
    :type target: str
    """
    spans = []
    current_index = 0
    for pattern in patterns:
        i = target.find(pattern, current_index)

        if i < 0:
            break
        else:
            end = i + len(pattern)
            spans.append(range(i, end))
            current_index = end

    if len(spans) == len(patterns):
        return spans
    else:
        return None


def main(target, patterns):
    """
    This method returns the result of the complete process. It can be useful if used from the python console or in a
    library
    :param target: The string to search inside
    :type target: str
    :param patterns: The substring to search for
    :type patterns: list
    :return: The string with the substring bolded highlighted in red
    """
    input_len = len(target)

    matches = match(target, patterns)
    if matches is None:
        print('No complete matches found', file=sys.stderr)
        return

    string_builder = []
    current_end = 0

    def colored(s):
        """
        wrapper around termcolor.colored, with program default colors and attributes
        :param s: the string to color
        :type s: str
        :rtype: str
        """
        return termcolor.colored(s, color='red', attrs=['bold'])

    for m in matches:
        if m.start == 0 or m.start == current_end:
            string_builder.append(colored(target[m.start:m.stop]))
            current_end = m.stop
        else:
            string_builder.append(target[current_end:m.start])
            string_builder.append(colored(target[m.start:m.stop]))
            current_end = m.stop

    if current_end != input_len:
        string_builder.append(target[current_end:])

    return ''.join(string_builder)


if __name__ == '__main__':
    queries = sys.argv[1:]
    if len(queries) == 1:
        queries = [char for char in queries[0]]
        # Strip of placeholder characters
        while True:
            try:
                queries.remove('_')
            except ValueError as _:
                break

    result = main(str(sys.stdin.read()), queries)
    print(result)
