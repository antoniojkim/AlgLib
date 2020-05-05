# -*- coding: utf-8 -*-


def wf_brackets(string):
    """
    Given a string containing just the characters: '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
        Note: an empty string is also considered valid

    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    """
    bracket_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    stack = []
    for c in string:
        if c in bracket_pairs.keys():
            stack.append(c)
        elif c in bracket_pairs.values():
            if len(stack) == 0 or bracket_pairs[stack[-1]] != c:
                return False

            stack.pop()

    if len(stack) > 0:
        return False

    return True
